# MSCriticalMessage

**Framework**: Messages  
**Kind**: struct

A message for critical communications.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+

## Declaration

```swift
struct MSCriticalMessage
```

#### Overview

Create and send time-sensitive messages that require immediate attention. Critical messages can bypass certain system restrictions to ensure delivery of urgent information.

## Topics

### Creating a message
- [init(messageText: String)](mscriticalmessage/init(messagetext:).md)
  Initializer
### Accessing message content
- [var messageText: String](mscriticalmessage/messagetext.md)
  The text of the critical message.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Sending SMS messages from an app](critical-messaging-api.md)
  Send critical messages from inside your app using the Critical Messaging API.
- [class MSCriticalSMSMessenger](mscriticalsmsmessenger.md)
  The user interface for the Critical Messaging API.
- [struct MSRecipient](msrecipient.md)
  A structure that describes the recipient of a critical message.
- [enum MSCriticalMessagingAuthorizationStatus](mscriticalmessagingauthorizationstatus.md)
  Values that describe the authorization status for the Critical Messaging API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/mscriticalmessage)*