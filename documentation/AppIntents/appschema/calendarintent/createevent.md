# createEvent

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that creates a calendar event.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var createEvent: some AppSchemaIntent { get }
```

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `calendar` domain and one of your app’s actions matches the `createEvent` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent(schema: .calendar.createEvent)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `createEvent` schema. You can create a type that conforms to the schema by adding the `@AppIntent` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `calendar_createEvent` and select it from the code-completion suggestions:

```swift
@AppIntent(schema: .calendar.createEvent)
struct CreateEventIntent {
    /// The title of the event.
    var title: String

    /// The start date of the event.
    var startDate: Date

    /// The end date of the event.
    var endDate: Date?

    /// The location of the event. If not provided, the event is not location-based.
    var location: <#EventLocation#>?

    /// The calendar in which to create the event.
    var calendar: <#CalendarEntity#>

    /// A boolean value indicating whether the event is all day.
    var isAllDay: Bool

    /// The recurrence rule for the event. If not provided, the event is not recurring.
    var recurrence: Calendar.RecurrenceRule?

    /// The attendees of the event.
    var attendees: [<#AttendeeEntity#>]

    /// The note associated with the event.
    var note: AttributedString?

    func perform() async throws -> some ReturnsValue<<#EventEntity#>> {
        <#code#>
    }
}
```

Define a `@UnionValue` enumeration for the `location` parameter, as in the following example, by typing the first few characters of `calendar_location` in Xcode and selecting it from the code-completion suggestions.

```swift
@UnionValue
enum EventLocation {
    case place(GeoToolbox.PlaceDescriptor)
    case address(String)
}
```

> 💡 **Tip**: Keep the cases that your app supports and remove the rest.

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Parameters for the create-event intent

Each parameter in the code listing above plays a specific role when your app performs this action. The following table describes what each parameter represents and any behavior to account for when you set it.

| Parameter | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `title` | `String` | Swift | The title of the event. |
| `startDate` | `Date` | Foundation | The start date of the event. |
| `endDate` | `Date?` | Foundation | The end date of the event. |
| `location` | `@UnionValue?` | Your app | The location of the event. If not provided, the event is not location-based. `EventLocation` is a placeholder name for the `@UnionValue` type your app defines, as shown in the example above the table. |
| `calendar` | `@AppEntity(schema: .calendar.calendar)` | Your app | The calendar in which to create the event. `CalendarEntity` is a placeholder name for a type that conforms to the [`calendar`](../calendarentity/calendar.md) entity schema, which your app defines and implements. |
| `isAllDay` | `Bool` | Swift | A boolean value indicating whether the event is all day. |
| `recurrence` | `Calendar.RecurrenceRule?` | Foundation | The recurrence rule for the event. If not provided, the event is not recurring. |
| `attendees` | `[@AppEntity(schema: .calendar.attendee)]` | Your app | The attendees of the event. `AttendeeEntity` is a placeholder name for a type that conforms to the [`attendee`](../calendarentity/attendee.md) entity schema, which your app defines and implements. |
| `note` | `AttributedString?` | Foundation | The note associated with the event. |

## See Also

### Actions
- [var deleteEvent: some AppSchemaIntent](./deleteevent.md)
  An intent schema that deletes a calendar event.
- [var updateEvent: some AppSchemaIntent](./updateevent.md)
  An intent schema that updates a calendar event.
- [AppSchema.CalendarIntent](../calendarintent.md)
  Identifies intent schemas in the calendar domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/calendarintent/createevent)*