# AppSchema.MessagesEntity

**Framework**: App Intents  
**Kind**: protocol

Identifies entity schemas in the messages domain.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol MessagesEntity : AppSchema.Kind
```

## Topics

### Instance Properties
- [var conversation: some AppSchemaEntity](appschema/messagesentity/conversation.md)
  An entity schema for a conversation.
- [var customAttachment: some AppSchemaEntity](appschema/messagesentity/customattachment.md)
  An entity schema for a custom attachment.
- [var message: some AppSchemaEntity](appschema/messagesentity/message.md)
  An entity schema for a message.
- [var messagePerson: some AppSchemaEntity](appschema/messagesentity/messageperson.md)
  An entity schema for a message person.

## Relationships

### Inherits From
- [AppSchema.Kind](appschema/kind.md)
### Conforming Types
- [AppSchema.Entity](appschema/entity.md)

## See Also

- [var conversation: some AppSchemaEntity](appschema/messagesentity/conversation.md)
  An entity schema for a conversation.
- [var customAttachment: some AppSchemaEntity](appschema/messagesentity/customattachment.md)
  An entity schema for a custom attachment.
- [var message: some AppSchemaEntity](appschema/messagesentity/message.md)
  An entity schema for a message.
- [var messagePerson: some AppSchemaEntity](appschema/messagesentity/messageperson.md)
  An entity schema for a message person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/messagesentity)*