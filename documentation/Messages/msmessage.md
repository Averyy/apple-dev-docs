# MSMessage

**Framework**: Messages  
**Kind**: class

A custom message object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class MSMessage
```

#### Overview

Use the [`MSMessage`](msmessage.md) class to create custom message objects. To create interactive messages that can be updated by the conversation’s participants, instantiate a message with a session using the [`init(session:)`](msmessage/init(session:).md) method. Otherwise, instantiate the message using the [`init()`](msmessage/init().md) method.

## Topics

### Creating Messages
- [init()](msmessage/init.md)
  Initializes a new message that is not part of a session.
- [init(session: MSSession)](msmessage/init(session:).md)
  Initializes a new message that is part of the provided session.
### Message Properties
- [var accessibilityLabel: String?](msmessage/accessibilitylabel.md)
  A localized string that describes the message.
- [var error: (any Error)?](msmessage/error.md)
  An error object describing why the system failed to send the message.
- [var isPending: Bool](msmessage/ispending.md)
  A Boolean value that indicates whether the message is pending or whether it has been sent or received.
- [var layout: MSMessageLayout?](msmessage/layout.md)
  A layout object that defines the message’s appearance.
- [var senderParticipantIdentifier: UUID](msmessage/senderparticipantidentifier.md)
  A UUID identifying the participant that sent the message.
- [var session: MSSession?](msmessage/session.md)
  The session that this message belongs to.
- [var shouldExpire: Bool](msmessage/shouldexpire.md)
  A Boolean value that determines whether the message should expire after being read.
- [var summaryText: String?](msmessage/summarytext.md)
  A succinct description of the message.
- [var url: URL?](msmessage/url.md)
  A URL that encodes data to be transmitted with the message.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class MSSession](mssession.md)
  A session object used to create and update messages.
- [class MSMessageLayout](msmessagelayout.md)
  An abstract base class that defines the appearance of [`MSMessage`](msmessage.md) objects in the conversation transcript.
- [class MSMessageTemplateLayout](msmessagetemplatelayout.md)
  A template-based layout for custom messages.
- [class MSMessageLiveLayout](msmessagelivelayout.md)
  A layout that provides a custom, interactive view inside the transcript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessage)*