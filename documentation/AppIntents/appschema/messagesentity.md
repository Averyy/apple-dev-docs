# AppSchema.MessagesEntity

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

Identifies entity schemas in the messages domain.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
protocol MessagesEntity : AppSchema.Kind
```

## Topics

### Instance Properties
- [var conversation: some AppSchemaEntity](./messagesentity/conversation.md)
  An entity schema for a conversation.
- [var customAttachment: some AppSchemaEntity](./messagesentity/customattachment.md)
  An entity schema for a custom attachment.
- [var message: some AppSchemaEntity](./messagesentity/message.md)
  An entity schema for a message.
- [var messagePerson: some AppSchemaEntity](./messagesentity/messageperson.md)
  An entity schema for a message person.

## Relationships

### Inherits From
- [AppSchema.Kind](./kind.md)
### Conforming Types
- [AppSchema.Entity](./entity.md)

## See Also

### Content and parameter types
- [var conversation: some AppSchemaEntity](./messagesentity/conversation.md)
  An entity schema for a conversation.
- [var customAttachment: some AppSchemaEntity](./messagesentity/customattachment.md)
  An entity schema for a custom attachment.
- [var message: some AppSchemaEntity](./messagesentity/message.md)
  An entity schema for a message.
- [var messagePerson: some AppSchemaEntity](./messagesentity/messageperson.md)
  An entity schema for a message person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/messagesentity)*