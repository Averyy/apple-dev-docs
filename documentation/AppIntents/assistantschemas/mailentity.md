# AssistantSchemas.MailEntity

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

Assistant schema conformance for app entities that describe email.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
protocol MailEntity : AssistantSchemas.Model
```

## Topics

### Instance Properties
- [var account: some AssistantSchemas.Entity](./mailentity/account.md)
  The app entity describes an email account.
- [var draft: some AssistantSchemas.Entity](./mailentity/draft.md)
  The app entity describes an email draft.
- [var mailbox: some AssistantSchemas.Entity](./mailentity/mailbox.md)
  The app entity describes an email mailbox.
- [var message: some AssistantSchemas.Entity](./mailentity/message.md)
  The app entity describes an email message.

## Relationships

### Inherits From
- [AssistantSchemas.Model](./model.md)
### Conforming Types
- [AssistantSchema.EntitySchema](../assistantschema/entityschema.md)
- [AssistantSchemas.EntitySchema](./entityschema.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/mailentity)*