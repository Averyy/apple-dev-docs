# AppSchema.RemindersIntent

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

Identifies intent schemas in the reminders domain.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
protocol RemindersIntent : AppSchema.Kind
```

## Topics

### Instance Properties
- [var createList: some AppSchemaIntent](./remindersintent/createlist.md)
  An intent schema that creates a new reminder list.
- [var createReminder: some AppSchemaIntent](./remindersintent/createreminder.md)
  An intent schema that creates a new reminder.
- [var createSection: some AppSchemaIntent](./remindersintent/createsection.md)
  An intent schema that creates a new reminder list section.
- [var deleteReminders: some AppSchemaIntent](./remindersintent/deletereminders.md)
  An intent schema that deletes reminders.
- [var updateReminder: some AppSchemaIntent](./remindersintent/updatereminder.md)
  An intent schema that updates a reminder.

## Relationships

### Inherits From
- [AppSchema.Kind](./kind.md)
### Conforming Types
- [AppSchema.Intent](./intent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/remindersintent)*