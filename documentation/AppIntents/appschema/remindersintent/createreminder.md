# createReminder

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that creates a new reminder.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var createReminder: some AppSchemaIntent { get }
```

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `reminders` domain and one of your app’s actions matches the `createReminder` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent(schema: .reminders.createReminder)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `createReminder` schema. You can create a type that conforms to the schema by adding the `@AppIntent` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `reminders_createReminder` and select it from the code-completion suggestions:

```swift
@AppIntent(schema: .reminders.createReminder)
struct CreateReminderIntent {
    /// The title of the reminder.
    var title: String

    /// The list of the reminder.
    var list: <#ListEntity#>?

    /// The note of the reminder.
    var note: AttributedString?

    /// A boolean value indicating whether the reminder is flagged.
    var isFlagged: Bool?

    /// The images of the reminder.
    var images: [IntentFile]

    /// The tags of the reminder.
    var tags: Set<String>

    /// The URLs of the reminder.
    var urls: [URL]

    /// The due date of the reminder.
    var dueDate: DateComponents?

    /// The recurrence of the reminder.
    var recurrence: Calendar.RecurrenceRule?

    /// The location of the reminder.
    var locationTrigger: <#LocationTriggerEntity#>?

    /// The section of the reminder.
    var section: <#SectionEntity#>?

    func perform() async throws -> some ReturnsValue<<#ReminderEntity#>> {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Parameters for the create-reminder intent

Each parameter in the code listing above plays a specific role when your app performs this action. The following table describes what each parameter represents and any behavior to account for when you set it.

| Parameter | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `title` | `String` | Swift | The title of the reminder. |
| `list` | `@AppEntity(schema: .reminders.list)?` | Your app | The list of the reminder. `ListEntity` is a placeholder name for a type that conforms to the [`list`](../remindersentity/list.md) entity schema, which your app defines and implements. |
| `note` | `AttributedString?` | Foundation | The note of the reminder. |
| `isFlagged` | `Bool?` | Swift | A boolean value indicating whether the reminder is flagged. |
| `images` | `[IntentFile]` | App Intents | The images of the reminder. |
| `tags` | `Set<String>` | Swift | The tags of the reminder. |
| `urls` | `[URL]` | Foundation | The URLs of the reminder. |
| `dueDate` | `DateComponents?` | Foundation | The due date of the reminder. |
| `recurrence` | `Calendar.RecurrenceRule?` | Foundation | The recurrence of the reminder. |
| `locationTrigger` | `@AppEntity(schema: .reminders.locationTrigger)?` | Your app | The location of the reminder. `LocationTriggerEntity` is a placeholder name for a type that conforms to the [`locationTrigger`](../remindersentity/locationtrigger.md) entity schema, which your app defines and implements. |
| `section` | `@AppEntity(schema: .reminders.section)?` | Your app | The section of the reminder. `SectionEntity` is a placeholder name for a type that conforms to the [`section`](../remindersentity/section.md) entity schema, which your app defines and implements. |

## See Also

### Actions
- [var createList: some AppSchemaIntent](./createlist.md)
  An intent schema that creates a new reminder list.
- [var createSection: some AppSchemaIntent](./createsection.md)
  An intent schema that creates a new reminder list section.
- [var deleteReminders: some AppSchemaIntent](./deletereminders.md)
  An intent schema that deletes reminders.
- [var updateReminder: some AppSchemaIntent](./updatereminder.md)
  An intent schema that updates a reminder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/remindersintent/createreminder)*