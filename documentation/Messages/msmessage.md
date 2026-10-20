# MSMessage

**Framework**: Messages  
**Kind**: class  
**Role**: Class

A custom message object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class MSMessage
```

```objc
@interface MSMessage : NSObject
```

#### Overview

Use the [`MSMessage`](./msmessage.md) class to create custom message objects. To create interactive messages that can be updated by the conversation’s participants, instantiate a message with a session using the [`init(session:)`](./msmessage/init%28session%29.md) method. Otherwise, instantiate the message using the [`init()`](./msmessage/init%28%29.md) method.

## Topics

### Creating Messages
- [init()](./msmessage/init%28%29.md)
  Initializes a new message that is not part of a session.
- [init(session: MSSession)](./msmessage/init%28session%29.md)
  Initializes a new message that is part of the provided session.
### Message Properties
- [var accessibilityLabel: String?](./msmessage/accessibilitylabel.md)
  A localized string that describes the message.
- [var error: (any Error)?](./msmessage/error.md)
  An error object describing why the system failed to send the message.
- [var isPending: Bool](./msmessage/ispending.md)
  A Boolean value that indicates whether the message is pending or whether it has been sent or received.
- [var layout: MSMessageLayout?](./msmessage/layout.md)
  A layout object that defines the message’s appearance.
- [var senderParticipantIdentifier: UUID](./msmessage/senderparticipantidentifier.md)
  A UUID identifying the participant that sent the message.
- [var session: MSSession?](./msmessage/session.md)
  The session that this message belongs to.
- [var shouldExpire: Bool](./msmessage/shouldexpire.md)
  A Boolean value that determines whether the message should expire after being read.
- [var summaryText: String?](./msmessage/summarytext.md)
  A succinct description of the message.
- [var url: URL?](./msmessage/url.md)
  A URL that encodes data to be transmitted with the message.
### Initializers
- [init?(coder: NSCoder)](./msmessage/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Interactive messages
- [class MSSession](./mssession.md)
  A session object used to create and update messages.
- [class MSMessageLayout](./msmessagelayout.md)
  An abstract base class that defines the appearance of [`MSMessage`](./msmessage.md) objects in the conversation transcript.
- [class MSMessageTemplateLayout](./msmessagetemplatelayout.md)
  A template-based layout for custom messages.
- [class MSMessageLiveLayout](./msmessagelivelayout.md)
  A layout that provides a custom, interactive view inside the transcript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessage)*