# AppSchema.RemindersIntent

**Framework**: App Intents  
**Kind**: protocol

Identifies intent schemas in the reminders domain.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
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
- [var updateReminder: some AppSchemaIntent](appschema/remindersintent/updatereminder.md)
  An intent schema that updates a reminder.

## Relationships

### Inherits From
- [AppSchema.Kind](appschema/kind.md)
### Conforming Types
- [AppSchema.Intent](appschema/intent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/remindersintent)*