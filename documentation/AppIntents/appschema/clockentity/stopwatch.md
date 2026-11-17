# stopwatch

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for a stopwatch.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var stopwatch: some AppSchemaEntity { get }
```

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `clock` domain and its content matches the `stopwatch` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .clock.stopwatch)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `stopwatch` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `clock_stopwatch` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .clock.stopwatch)
struct StopwatchEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more stopwatch entities, unless you provide another.
    static let defaultQuery = StopwatchEntityQuery()

    // MARK: Entity properties

    /// The unique identifier for the stopwatch entity.
    let id: <#Identifiable.ID#>

    var laps: [Duration]

    var startTime: Date

    var pauseTime: Date?

    var state: <#StopwatchState#>

    /// The details the system shows to identify the stopwatch entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more stopwatch entities by their identifiers.
    struct StopwatchEntityQuery: EntityQuery {
        func entities(for identifiers: [StopwatchEntity.ID]) async throws -> [StopwatchEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Properties of the stopwatch entity

Each property in the code listing above describes a facet of the entity your app provides to the system. The following table describes what each property represents.

| Property | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `laps` | `[Duration]` | Swift | Laps |
| `startTime` | `Date` | Foundation | Start Time |
| `pauseTime` | `Date?` | Foundation | Pause Time |
| `state` | `@AppEnum(schema: .clock.stopwatchState)` | Your app | State `StopwatchState` is a placeholder name for a type that conforms to the [`stopwatchState`](../clockenum/stopwatchstate.md) enum schema, which your app defines and implements. |


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/clockentity/stopwatch)*