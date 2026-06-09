# Testing your App Intents code

**Framework**: App Intents Testing

Evaluate intents, entities, and queries, and verify your integration with system features like Spotlight and Siri.

#### Overview

The [`App Intents`](https://developer.apple.com/documentation/AppIntents) framework connects your app to system features like Siri, Spotlight, and Shortcuts. When your App Intents code regresses, those integrations often break silently — people may get wrong results, custom shortcuts fail, or Spotlight search doesn’t find content without any obvious error. The App Intents Testing framework enables you to test your App Intents code, and prevent and catch regressions before they ship.

Writing tests with App Intents Testing works differently from typical unit testing: you create an [`IntentDefinitions`](intentdefinitions.md) instance with your app’s bundle identifier, then use it to look up definitions by their string name — [`AppIntentDefinition`](appintentdefinition.md) for intents, [`AppEntityDefinition`](appentitydefinition.md) for entities, [`AppEnumDefinition`](appenumdefinition.md) for enumerations. Because every type is accessed by name rather than imported directly, your tests run in a UI Testing target that communicates with your app out-of-process through the real App Intents infrastructure. As a result, tests use the same code path that Siri and Shortcuts use, and they run fast enough that you can include them in frequent continuous-integration workflows.

#### Set Up Your Test Target

App Intents Testing runs your intents inside a live app process, so your tests belong in a UI testing bundle rather than a unit test target. Add a new UI Testing target to your Xcode project if you don’t already have one, and make sure it uses the same code signing team as your app.

In your test class, launch the app during setup and create an [`IntentDefinitions`](intentdefinitions.md) instance using your app’s bundle identifier:

```swift
let app = XCUIApplication()
var definitions: IntentDefinitions!

override func setUp() async throws {
    app.launch()
    definitions = IntentDefinitions(
        bundleIdentifier: "com.example.my-app"
    )
}
```

The [`IntentDefinitions`](intentdefinitions.md) instance discovers all intent types, entity types, enums, and queries that your app registers with the system. You use this single entry point throughout your tests to look up definitions by their string name.

#### Run Your First Intent Test

To test an intent, use the [`IntentDefinitions`](intentdefinitions.md) instance you created, and look up the intent under test using the [`intents`](intentdefinitions/intents.md) property. Then, create an intent instance with parameters, run it, and assert the result. The [`AppIntentDefinition`](appintentdefinition.md) type’s [`makeIntent`](appintentdefinition/makeintent.md) property accepts primitive parameters, for example, strings, dates, and Boolean values, and resolves them automatically.

```swift
func testOpenFavorites() async throws {
    let intent = definitions.intent["OpenFavorites"]
    let instance = intent.makeIntent()
    let result = try await instance.run()
    XCTAssertEqual(try result.value.count, 5)
}
```

The [`run()`](anyappintent/run().md) method sends the intent to your running app for processing through the real App Intents infrastructure. The returned [`ResolvedIntentResult`](resolvedintentresult.md) uses dynamic member lookup (`@dynamicMemberLookup`), so you access return-value properties by name — like `result.value.count` or `result.value.title` — without importing your app’s types.

#### Test Entities and Enumerations

[`App entities`](https://developer.apple.com/documentation/AppIntents/app-entities) represent your app’s content and contain information about its data, or concepts related to its data. Think of them like the “nouns” of your app. The system queries your app for entities that match an intent’s parameter, a person’s search in Spotlight, or to understand visible onscreen content. Testing your entities and entity queries confirms that system features like Siri and Spotlight can find the right entities when people ask for them.

Use [`entities(matching:)`](appentitydefinition/entities(matching:).md) on an [`AppEntityDefinition`](appentitydefinition.md) to search entities by string, the same way the system resolves a spoken name. Each result is an [`AnyAppEntity`](anyappentity.md) instance that supports `@dynamicMemberLookup`, so you can read entity properties directly by name as shown in the following example:

```swift
func testFindCalendarByName() async throws {
    let calendarDef = definitions.entities["CalendarEntity"]
    let results = try await calendarDef.entities(matching: "Work")
    XCTAssertFalse(results.isEmpty)
    
    let name: String = try results[0].name
    XCTAssertEqual(name, "Work")
    let colorName: String = try results[0].colorName
    XCTAssertEqual(colorName, "blue")
}
```

To create an entity reference from a known identifier, for example, to pass as a parameter to an intent, use [`makeReference(identifier:)`](appentitydefinition/makereference(identifier:).md):

```swift
let calendar = definitions
    .entities["CalendarEntity"]
    .makeReference(identifier: "work-calendar-id")
```

For enumerations, use [`makeCase(_:)`](appenumdefinition/makecase(_:).md) to construct a typed enum value from its raw string. This is how you pass enum parameters to intents that accept categories or priorities:

```swift
let priority = definitions
    .enums["EventPriority"]
    .makeCase("high")
```

#### Chain Intents and Let Entities Flow From One Intent to Another

Real-world tasks often involve several intents in sequence. A person might want to find a calendar, create an event on it, and then add an attendee — and each step depends on the output of the previous one. Testing these chains of intents confirms that entity references flow correctly between intents.

Continuing the calendar example, start by finding the calendar entity and passing it as a parameter to a `CreateEvent` intent:

```swift
func testCreateEventOnCalendar() async throws {
    let calendarDef = definitions
        .entities["CalendarEntity"]
    let calendars = try await calendarDef
        .entities(matching: "Work")
    let workCalendar = calendars[0]
```

Next, pass the type-erased [`AnyAppEntity`](anyappentity.md) directly as a parameter. App Intents Testing handles the cross-intent entity transfer the same way the system does:

```swift
    let createResult = try await definitions
        .intents["CreateEvent"]
        .makeIntent(
            title: "Sprint Planning",
            calendar: workCalendar
        )
        .run()
```

Then, pass the result entity into a second intent to add an attendee:

```swift
    let event: AnyAppEntity = try createResult.value
    let addResult = try await definitions
        .intents["AddAttendee"]
        .makeIntent(
            event: event,
            email: "jada@example.com"
        )
        .run()
    let count: Int = try addResult.value.attendeeCount
    XCTAssertEqual(count, 1)
}
```

This test verifies the entire workflow end-to-end. If the entity identifier format changes, or if the `AddAttendee` intent doesn’t resolve the event parameter correctly, this test catches it.

#### Use Testing Only Intents for Setup and Teardown

Some tests need the app to be in a specific state before they run — a particular calendar needs to exist, or the database needs to be empty. Rather than relying on UI automation to navigate your app and set up state, create intents specifically for testing that perform app navigation or other setup tasks. Mark these intents with [`isDiscoverable`](https://developer.apple.com/documentation/AppIntents/AppIntent/isDiscoverable) set to `false`, so they don’t appear in Shortcuts or Siri, and wrap them in an `#if DEBUG` block so they’re excluded from release builds:

```swift
#if DEBUG
struct ResetDatabaseIntent: AppIntent {
    static let title: LocalizedStringResource =
        "Reset Database"
    static let isDiscoverable = false

    func perform() async throws -> some IntentResult {
        // Clear all data and insert seed records.
    }
}
#endif
```

Call the testing-only intent at the beginning of your test to guarantee a clean starting state:

```swift
func testEventCreation() async throws {
    try await definitions
        .intents["ResetDatabaseIntent"]
        .makeIntent()
        .run()
    // Now test against known seed data.
}
```

This pattern keeps your tests deterministic without coupling them to navigation paths or UI structure. When the app’s interface changes, your tests continue to pass because they operate entirely using the App Intents framework.

#### Test Transferable Conformance

Making your app entities conform to the [`Transferable`](https://developer.apple.com/documentation/CoreTransferable/Transferable) protocol is a key requirement for your app to support Apple Intelligence and Siri. If an entity doesn’t serialize and transfer to other apps correctly, features like drag and drop, copy and paste, or multi-turn commands for Siri don’t work or produce incorrect results.

First, export an entity to a data representation using `exported(as:)`, then reimport it using `resolved(from:)` on the entity definition:

```swift
func testEventTransferable() async throws {
    let eventDef = definitions.entities["EventEntity"]
    let events = try await eventDef
        .entities(matching: "Design Review")
    let original = events[0]
    
    // Export the entity.
    let exported = try await original.exported(
        as: .json
    )
    
    // Re-import the entity.
    let reimported = try await eventDef.resolved(
        from: exported
    )
    
    // Verify that the full export-reimport flow preserved the title.
    let title: String = try reimported.title
    XCTAssertEqual(title, "Design Review")
```

If the entity drops a property during serialization, or if the `Transferable` conformance doesn’t handle a field correctly, this test fails and indicates what went wrong.

#### Verify Your Spotlight Indexing Code

To let people find your app’s content with Spotlight, your app donates app entities to the Spotlight index. Spotlight indexing bugs can be easy to introduce and hard to notice — a missing attribute or a stale index entry can silently degrade people’s search experience. The [`spotlightQuery(_:)`](appentitydefinition/spotlightquery(_:).md) method lets you test your Spotlight integration directly.

First, query Spotlight for a known entity and verify the results contain the expected data:

```swift
func testEventAppearsInSpotlight() async throws {
    let eventDef = definitions.entities["EventEntity"]
    let results = try await eventDef
        .spotlightQuery("Design Review")
    XCTAssertFalse(results.isEmpty)
    let title: String = try results[0].title
    XCTAssertEqual(title, "Design Review")
}
```

The `spotlightQuery(_:)` method queries the Spotlight index for entities matching the search string and returns the same [`AnyAppEntity`](anyappentity.md) instances you work with elsewhere in your tests.

Pass `nil` to `spotlightQuery(_:)` to retrieve all indexed entities of a given type, which lets you verify that your Spotlight donations result in the expected set of results:

```swift
func testAllEventsIndexed() async throws {
    let eventDef = definitions.entities["EventEntity"]
    let allIndexed = try await eventDef
        .spotlightQuery(nil)
    XCTAssertGreaterThanOrEqual(allIndexed.count, 3)
}
```

#### Test Your Entity Annotations

On-screen awareness lets the system identify entities that are visible in your app’s interface. When someone asks Siri about something they can see onscreen, the system uses entity annotations that you provide to resolve the person’s sometimes ambiguous reference to what they see. For example, a person might say “update this event” when they view a calendar event on screen, and the calendar app provides an entity annotation to let the system resolve the content that “this event” refers to.

To test your entity annotations, use the [`viewAnnotations()`](appentitydefinition/viewannotations().md) method. It returns the entities currently visible in your app, along with their selection state. First, you need to navigate to a specific screen in your app, which is a good use case for the testing-only intents explained in an earlier section. For example, a calendar app might create an intent to navigate to a specific event, then verify the onscreen entities like so:

```swift
func testEventDetailShowsAnnotation() async throws {
    try await definitions
        .intents["NavigateToEvent"]
        .makeIntent(eventId: "design-review-id")
        .run()
    let eventDef = definitions.entities["EventEntity"]
    let annotations = try await eventDef
        .viewAnnotations()
    XCTAssertFalse(annotations.isEmpty)
```

Each [`ViewAnnotation`](viewannotation.md) has an [`entity`](viewannotation/entity.md) property that contains the [`AnyAppEntity`](anyappentity.md) you can inspect and the [`isSelected`](viewannotation/isselected.md) property to indicate whether the entity is currently selected in your app’s UI:

```swift
    let title: String = try annotations[0]
        .entity.title
    XCTAssertEqual(title, "Design Review")
    XCTAssertTrue(annotations[0].isSelected)
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/testing-your-app-intents-code)*