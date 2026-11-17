# deleteEvent

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that deletes a calendar event.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var deleteEvent: some AppSchemaIntent { get }
```

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `calendar` domain and one of your app’s actions matches the `deleteEvent` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent(schema: .calendar.deleteEvent)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `deleteEvent` schema. You can create a type that conforms to the schema by adding the `@AppIntent` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `calendar_deleteEvent` and select it from the code-completion suggestions:

```swift
@AppIntent(schema: .calendar.deleteEvent)
struct DeleteEventIntent {
    /// Calendar event to be deleted.
    var entity: <#EventEntity#>

    /// If the event is recurring, specifies whether to delete a single occurrence or multiple.
    var span: <#EventSpan#>?

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Parameters for the delete-event intent

Each parameter in the code listing above plays a specific role when your app performs this action. The following table describes what each parameter represents and any behavior to account for when you set it.

| Parameter | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `entity` | `@AppEntity(schema: .calendar.event)` | Your app | Calendar event to be deleted. `EventEntity` is a placeholder name for a type that conforms to the [`event`](../calendarentity/event.md) entity schema, which your app defines and implements. |
| `span` | `@AppEnum(schema: .calendar.eventSpan)?` | Your app | If the event is recurring, specifies whether to delete a single occurrence or multiple. `EventSpan` is a placeholder name for a type that conforms to the [`eventSpan`](../calendarenum/eventspan.md) enum schema, which your app defines and implements. |

## See Also

### Actions
- [var createEvent: some AppSchemaIntent](./createevent.md)
  An intent schema that creates a calendar event.
- [var updateEvent: some AppSchemaIntent](./updateevent.md)
  An intent schema that updates a calendar event.
- [AppSchema.CalendarIntent](../calendarintent.md)
  Identifies intent schemas in the calendar domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/calendarintent/deleteevent)*