# updateEvent

**Framework**: App Intents  
**Kind**: property

An intent schema that updates a calendar event.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var updateEvent: some AppSchemaIntent { get }
```

#### Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `calendar` domain and one of your app’s actions matches the `updateEvent` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent( .calendar.updateEvent)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `updateEvent` schema:

```swift
@AppIntent(schema: .calendar.updateEvent)
struct UpdateEventIntent {
    var event: <#EventEntity#>
    var title: String?
    var attendees: [<#AttendeeEntity#>]?
    var startDate: Date?
    var endDate: Date?
    var isAllDay: Bool?
    var calendar: <#CalendarEntity#>?
    var recurrence: Calendar.RecurrenceRule?
    var note: String?
    var location: <#EventLocation#>?
    var span: <#EventSpan#>?

    func perform() async throws -> some ReturnsValue<<#EventEntity#>> {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var createEvent: some AppSchemaIntent](appschema/calendarintent/createevent.md)
  An intent schema that creates a calendar event.
- [AppSchema.CalendarIntent](appschema/calendarintent.md)
  Identifies intent schemas in the calendar domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/calendarintent/updateevent)*