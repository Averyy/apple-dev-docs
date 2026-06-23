# updateReminder

**Framework**: App Intents  
**Kind**: property

An intent schema that updates a reminder.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var updateReminder: some AppSchemaIntent { get }
```

#### Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `reminders` domain and one of your app’s actions matches the `updateReminder` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent( .reminders.updateReminder)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `updateReminder` schema:

```swift
@AppIntent(schema: .reminders.updateReminder)
struct UpdateReminderIntent {
    var target: <#ReminderEntity#>
    var title: String?
    var note: AttributedString?
    var images: [IntentFile]?
    var subtasks: [<#ReminderEntity#>]?
    var tags: Set<String>?
    var urls: [URL]?
    var dueDate: DateComponents?
    var recurrence: Calendar.RecurrenceRule?
    var isCompleted: Bool?
    var isFlagged: Bool?
    var list: <#ListEntity#>?
    var section: <#SectionEntity#>?
    var locationTrigger: <#LocationTriggerEntity#>?

    func perform() async throws -> some ReturnsValue<<#ReminderEntity#>> {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var createList: some AppSchemaIntent](appschema/remindersintent/createlist.md)
  An intent schema that creates a new reminder list.
- [var createReminder: some AppSchemaIntent](appschema/remindersintent/createreminder.md)
  An intent schema that creates a new reminder.
- [var createSection: some AppSchemaIntent](appschema/remindersintent/createsection.md)
  An intent schema that creates a new reminder list section.
- [var deleteReminders: some AppSchemaIntent](appschema/remindersintent/deletereminders.md)
  An intent schema that deletes reminders.
- [var updateGroup: some AppSchemaIntent](appschema/remindersintent/updategroup.md)
  An intent schema that updates a reminder list group.
- [var updateList: some AppSchemaIntent](appschema/remindersintent/updatelist.md)
  An intent schema that updates a reminder list.
- [var updateSection: some AppSchemaIntent](appschema/remindersintent/updatesection.md)
  An intent schema that updates a reminder list section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/remindersintent/updatereminder)*