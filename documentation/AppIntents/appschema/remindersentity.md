# AppSchema.RemindersEntity

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

Identifies entity schemas in the reminders domain.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
protocol RemindersEntity : AppSchema.Kind
```

## Topics

### Instance Properties
- [var group: some AppSchemaEntity](./remindersentity/group.md)
  An entity schema for a group.
- [var list: some AppSchemaEntity](./remindersentity/list.md)
  An entity schema for a list.
- [var locationTrigger: some AppSchemaEntity](./remindersentity/locationtrigger.md)
  An entity schema for a location trigger.
- [var reminder: some AppSchemaEntity](./remindersentity/reminder.md)
  An entity schema for a reminder.
- [var section: some AppSchemaEntity](./remindersentity/section.md)
  An entity schema for a section.

## Relationships

### Inherits From
- [AppSchema.Kind](./kind.md)
### Conforming Types
- [AppSchema.Entity](./entity.md)

## See Also

### Content and parameter types
- [var group: some AppSchemaEntity](./remindersentity/group.md)
  An entity schema for a group.
- [var list: some AppSchemaEntity](./remindersentity/list.md)
  An entity schema for a list.
- [var locationTrigger: some AppSchemaEntity](./remindersentity/locationtrigger.md)
  An entity schema for a location trigger.
- [var reminder: some AppSchemaEntity](./remindersentity/reminder.md)
  An entity schema for a reminder.
- [var section: some AppSchemaEntity](./remindersentity/section.md)
  An entity schema for a section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/remindersentity)*