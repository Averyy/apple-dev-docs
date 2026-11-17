# attendee

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for an attendee.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var attendee: some AppSchemaEntity { get }
```

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `calendar` domain and its content matches the `attendee` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .calendar.attendee)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `attendee` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `calendar_attendee` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .calendar.attendee)
struct AttendeeEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more attendee entities, unless you provide another.
    static let defaultQuery = AttendeeEntityQuery()

    // MARK: Entity properties

    /// The unique identifier for the attendee entity.
    let id: <#Identifiable.ID#>

    var person: IntentPerson

    var status: <#ParticipantStatus#>?

    var isAttendanceOptional: Bool

    var type: <#AttendeeType#>?

    /// The details the system shows to identify the attendee entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more attendee entities by their identifiers.
    struct AttendeeEntityQuery: EntityQuery {
        func entities(for identifiers: [AttendeeEntity.ID]) async throws -> [AttendeeEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Properties of the attendee entity

Each property in the code listing above describes a facet of the entity your app provides to the system. The following table describes what each property represents.

| Property | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `person` | `IntentPerson` | App Intents | Person |
| `status` | `@AppEnum(schema: .calendar.attendeeStatus)?` | Your app | Status `ParticipantStatus` is a placeholder name for a type that conforms to the [`attendeeStatus`](../calendarenum/attendeestatus.md) enum schema, which your app defines and implements. |
| `isAttendanceOptional` | `Bool` | Swift | Is Attendance Optional |
| `type` | `@AppEnum(schema: .calendar.attendeeType)?` | Your app | Type `AttendeeType` is a placeholder name for a type that conforms to the [`attendeeType`](../calendarenum/attendeetype.md) enum schema, which your app defines and implements. |

## See Also

### Content and parameter types
- [var calendar: some AppSchemaEntity](./calendar.md)
  An entity schema for a calendar.
- [var event: some AppSchemaEntity](./event.md)
  An entity schema for an event.
- [AppSchema.CalendarEntity](../calendarentity.md)
  Identifies entity schemas in the calendar domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/calendarentity/attendee)*