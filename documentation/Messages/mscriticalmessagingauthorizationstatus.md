# MSCriticalMessagingAuthorizationStatus

**Framework**: Messages  
**Kind**: enum

Values that describe the authorization status for the Critical Messaging API.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+

## Declaration

```swift
enum MSCriticalMessagingAuthorizationStatus
```

## Topics

### Authorization statuses
- [MSCriticalMessagingAuthorizationStatus.unknown](mscriticalmessagingauthorizationstatus/unknown.md)
  The authorization status is unknown.
- [MSCriticalMessagingAuthorizationStatus.denied](mscriticalmessagingauthorizationstatus/denied.md)
  A person has denied permission to use the Critical Messaging API.
- [MSCriticalMessagingAuthorizationStatus.approved](mscriticalmessagingauthorizationstatus/approved.md)
  A person has approved a request to use the Critical Messaging API.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Sending SMS messages from an app](critical-messaging-api.md)
  Send critical messages from inside your app using the Critical Messaging API.
- [class MSCriticalSMSMessenger](mscriticalsmsmessenger.md)
  The user interface for the Critical Messaging API.
- [struct MSRecipient](msrecipient.md)
  A structure that describes the recipient of a critical message.
- [struct MSCriticalMessage](mscriticalmessage.md)
  MSCriticalMessage A simple struct to encapsulate the message string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/mscriticalmessagingauthorizationstatus)*