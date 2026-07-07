# deleteEvent

**Framework**: App Intents  
**Kind**: property

An intent schema that deletes a calendar event.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var deleteEvent: some AppSchemaIntent { get }
```

#### Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `calendar` domain and one of your app’s actions matches the `deleteEvent` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent( .calendar.deleteEvent)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `deleteEvent` schema:

```swift
@AppIntent(schema: .calendar.deleteEvent)
struct DeleteEventIntent {
    var entity: <#EventEntity#>
    var span: <#EventSpan#>?

    func perform() async throws -> some IntentResult {
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
- [var updateEvent: some AppSchemaIntent](appschema/calendarintent/updateevent.md)
  An intent schema that updates a calendar event.
- [AppSchema.CalendarIntent](appschema/calendarintent.md)
  Identifies intent schemas in the calendar domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/calendarintent/deleteevent)*