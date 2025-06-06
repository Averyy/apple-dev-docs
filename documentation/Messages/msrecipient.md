# MSRecipient

**Framework**: Messages  
**Kind**: struct

A structure that describes the recipient of a critical message.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+

## Declaration

```swift
struct MSRecipient
```

## Topics

### Creating recipients
- [init(phoneNumber: String)](msrecipient/init(phonenumber:).md)
  Creates a new critical message recipient with the provided phone number.
### Properties
- [var phoneNumber: String](msrecipient/phonenumber.md)
  The phone number of a critical message recipient.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Sending SMS messages from an app](critical-messaging-api.md)
  Send critical messages from inside your app using the Critical Messaging API.
- [class MSCriticalSMSMessenger](mscriticalsmsmessenger.md)
  The user interface for the Critical Messaging API.
- [struct MSCriticalMessage](mscriticalmessage.md)
  MSCriticalMessage A simple struct to encapsulate the message string.
- [enum MSCriticalMessagingAuthorizationStatus](mscriticalmessagingauthorizationstatus.md)
  Values that describe the authorization status for the Critical Messaging API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msrecipient)*