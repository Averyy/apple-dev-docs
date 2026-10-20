# AppSchema.RemindersEnum

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

Identifies enum schemas in the reminders domain.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
protocol RemindersEnum : AppSchema.Kind
```

## Topics

### Instance Properties
- [var listType: some AppSchemaEnum](./remindersenum/listtype.md)
  An enum schema for a list type parameter.
- [var locationTriggerEvent: some AppSchemaEnum](./remindersenum/locationtriggerevent.md)
  An enum schema for a location trigger event parameter.

## Relationships

### Inherits From
- [AppSchema.Kind](./kind.md)
### Conforming Types
- [AppSchema.Enum](./enum.md)

## See Also

### Types for static parameters
- [var listType: some AppSchemaEnum](./remindersenum/listtype.md)
  An enum schema for a list type parameter.
- [var locationTriggerEvent: some AppSchemaEnum](./remindersenum/locationtriggerevent.md)
  An enum schema for a location trigger event parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/remindersenum)*