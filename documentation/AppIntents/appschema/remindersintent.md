# AppSchema.RemindersIntent

**Framework**: App Intents  
**Kind**: protocol

Identifies intent schemas in the reminders domain.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol RemindersIntent : AppSchema.Kind
```

## Topics

### Instance Properties
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
- [var updateReminder: some AppSchemaIntent](appschema/remindersintent/updatereminder.md)
  An intent schema that updates a reminder.
- [var updateSection: some AppSchemaIntent](appschema/remindersintent/updatesection.md)
  An intent schema that updates a reminder list section.

## Relationships

### Inherits From
- [AppSchema.Kind](appschema/kind.md)
### Conforming Types
- [AppSchema.Intent](appschema/intent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/remindersintent)*