# AppSchema.MailEntity

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

Identifies entity schemas in the mail domain.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
protocol MailEntity : AppSchema.Kind
```

## Topics

### Instance Properties
- [var account: some AppSchemaEntity](./mailentity/account.md)
  An entity schema for an account.
- [var draft: some AppSchemaEntity](./mailentity/draft.md)
  An entity schema for a draft.
- [var mailbox: some AppSchemaEntity](./mailentity/mailbox.md)
  An entity schema for a mailbox.
- [var message: some AppSchemaEntity](./mailentity/message.md)
  An entity schema for a message.
- [var thread: some AppSchemaEntity](./mailentity/thread.md)
  An entity schema for a thread.

## Relationships

### Inherits From
- [AppSchema.Kind](./kind.md)
### Conforming Types
- [AppSchema.Entity](./entity.md)

## See Also

### Content and parameter types
- [var account: some AppSchemaEntity](./mailentity/account.md)
  An entity schema for an account.
- [var draft: some AppSchemaEntity](./mailentity/draft.md)
  An entity schema for a draft.
- [var mailbox: some AppSchemaEntity](./mailentity/mailbox.md)
  An entity schema for a mailbox.
- [var message: some AppSchemaEntity](./mailentity/message.md)
  An entity schema for a message.
- [var thread: some AppSchemaEntity](./mailentity/thread.md)
  An entity schema for a thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/mailentity)*