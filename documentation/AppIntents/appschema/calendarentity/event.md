# event

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for an event.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var event: some AppSchemaEntity { get }
```

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `calendar` domain and its content matches the `event` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .calendar.event)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `event` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `calendar_event` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .calendar.event)
struct EventEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more event entities, unless you provide another.
    static let defaultQuery = EventEntityQuery()

    // MARK: Entity properties

    /// The unique identifier for the event entity.
    let id: <#Identifiable.ID#>

    var calendar: <#CalendarEntity#>

    var title: String

    var startDate: Date

    var endDate: Date

    var isAllDay: Bool

    var recurrence: Calendar.RecurrenceRule?

    var note: AttributedString?

    var travelTime: Duration?

    var location: <#EventLocation#>?

    var virtualLocation: URL?

    var status: <#EventEntityStatus#>?

    var alarms: [<#EventAlarm#>]

    var organizers: [IntentPerson]

    var attendees: [<#AttendeeEntity#>]

    /// The details the system shows to identify the event entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more event entities by their identifiers.
    struct EventEntityQuery: EntityQuery {
        func entities(for identifiers: [EventEntity.ID]) async throws -> [EventEntity] {
            <#code#>
        }
    }
}
```

Define a `@UnionValue` enumeration for the `location` property, as in the following example, by typing the first few characters of `calendar_location` in Xcode and selecting it from the code-completion suggestions.

```swift
@UnionValue
enum EventLocation {
    case place(GeoToolbox.PlaceDescriptor)
    case address(String)
}
```

Define a `@UnionValue` enumeration for the `alarms` property, as in the following example, by typing the first few characters of `calendar_eventAlarm` in Xcode and selecting it from the code-completion suggestions.

```swift
@UnionValue
enum EventAlarm {
    case duration(Duration)
    case date(Date)
}
```

> 💡 **Tip**: Keep the cases that your app supports and remove the rest.

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Properties of the event entity

Each property in the code listing above describes a facet of the entity your app provides to the system. The following table describes what each property represents.

| Property | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `calendar` | `@AppEntity(schema: .calendar.calendar)` | Your app | Calendar `CalendarEntity` is a placeholder name for a type that conforms to the [`calendar`](./calendar.md) entity schema, which your app defines and implements. |
| `title` | `String` | Swift | Title |
| `startDate` | `Date` | Foundation | Start Date |
| `endDate` | `Date` | Foundation | End Date |
| `isAllDay` | `Bool` | Swift | Is All Day |
| `recurrence` | `Calendar.RecurrenceRule?` | Foundation | Recurrence |
| `note` | `AttributedString?` | Foundation | Note |
| `travelTime` | `Duration?` | Swift | Travel Time |
| `location` | `@UnionValue?` | Your app | Location `EventLocation` is a placeholder name for the `@UnionValue` type your app defines, as shown in the example above the table. |
| `virtualLocation` | `URL?` | Foundation | Virtual Location |
| `status` | `@AppEnum(schema: .calendar.eventStatus)?` | Your app | Status `EventEntityStatus` is a placeholder name for a type that conforms to the [`eventStatus`](../calendarenum/eventstatus.md) enum schema, which your app defines and implements. |
| `alarms` | `[@UnionValue]` | Your app | Alarms `EventAlarm` is a placeholder name for the `@UnionValue` type your app defines, as shown in the example above the table. |
| `organizers` | `[IntentPerson]` | App Intents | Organizers |
| `attendees` | `[@AppEntity(schema: .calendar.attendee)]` | Your app | Attendees `AttendeeEntity` is a placeholder name for a type that conforms to the [`attendee`](./attendee.md) entity schema, which your app defines and implements. |

## See Also

### Content and parameter types
- [var attendee: some AppSchemaEntity](./attendee.md)
  An entity schema for an attendee.
- [var calendar: some AppSchemaEntity](./calendar.md)
  An entity schema for a calendar.
- [AppSchema.CalendarEntity](../calendarentity.md)
  Identifies entity schemas in the calendar domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/calendarentity/event)*