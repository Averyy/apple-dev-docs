# updateReminder

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that updates a reminder.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var updateReminder: some AppSchemaIntent { get }
```

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `reminders` domain and one of your app’s actions matches the `updateReminder` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent(schema: .reminders.updateReminder)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `updateReminder` schema. You can create a type that conforms to the schema by adding the `@AppIntent` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `reminders_updateReminder` and select it from the code-completion suggestions:

```swift
@AppIntent(schema: .reminders.updateReminder)
struct UpdateReminderIntent {
    /// The reminder to update
    var target: <#ReminderEntity#>

    /// The new title for the reminder
    var title: String?

    /// The new note for the reminder
    var note: AttributedString?

    /// The new tags for the reminder
    var tags: Set<String>?

    /// The new urls for the reminder
    var urls: [URL]?

    /// The new due date for the reminder
    var dueDate: DateComponents?

    /// The new recurrence for the reminder
    var recurrence: Calendar.RecurrenceRule?

    /// The new is completed for the reminder
    var isCompleted: Bool?

    /// The new is flagged for the reminder
    var isFlagged: Bool?

    /// The new list for the reminder
    var list: <#ListEntity#>?

    /// The new location for the reminder
    var locationTrigger: <#LocationTriggerEntity#>?

    func perform() async throws -> some ReturnsValue<<#ReminderEntity#>> {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Parameters for the update-reminder intent

Each parameter in the code listing above plays a specific role when your app performs this action. The following table describes what each parameter represents and any behavior to account for when you set it.

| Parameter | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `target` | `@AppEntity(schema: .reminders.reminder)` | Your app | The reminder to update `ReminderEntity` is a placeholder name for a type that conforms to the [`reminder`](../remindersentity/reminder.md) entity schema, which your app defines and implements. |
| `title` | `String?` | Swift | The new title for the reminder |
| `note` | `AttributedString?` | Foundation | The new note for the reminder |
| `tags` | `Set<String>?` | Swift | The new tags for the reminder |
| `urls` | `[URL]?` | Foundation | The new urls for the reminder |
| `dueDate` | `DateComponents?` | Foundation | The new due date for the reminder |
| `recurrence` | `Calendar.RecurrenceRule?` | Foundation | The new recurrence for the reminder |
| `isCompleted` | `Bool?` | Swift | The new is completed for the reminder |
| `isFlagged` | `Bool?` | Swift | The new is flagged for the reminder |
| `list` | `@AppEntity(schema: .reminders.list)?` | Your app | The new list for the reminder `ListEntity` is a placeholder name for a type that conforms to the [`list`](../remindersentity/list.md) entity schema, which your app defines and implements. |
| `locationTrigger` | `@AppEntity(schema: .reminders.locationTrigger)?` | Your app | The new location for the reminder `LocationTriggerEntity` is a placeholder name for a type that conforms to the [`locationTrigger`](../remindersentity/locationtrigger.md) entity schema, which your app defines and implements. |

## See Also

### Actions
- [var createList: some AppSchemaIntent](./createlist.md)
  An intent schema that creates a new reminder list.
- [var createReminder: some AppSchemaIntent](./createreminder.md)
  An intent schema that creates a new reminder.
- [var createSection: some AppSchemaIntent](./createsection.md)
  An intent schema that creates a new reminder list section.
- [var deleteReminders: some AppSchemaIntent](./deletereminders.md)
  An intent schema that deletes reminders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/remindersintent/updatereminder)*