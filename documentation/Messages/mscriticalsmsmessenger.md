# MSCriticalSMSMessenger

**Framework**: Messages  
**Kind**: class

The user interface for the Critical Messaging API.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+

## Declaration

```swift
@objc
class MSCriticalSMSMessenger
```

## Topics

### Determining the maximum allowed recipients
- [var maximumCriticalMessagingRecipients: Int](mscriticalsmsmessenger/maximumcriticalmessagingrecipients.md)
  An integer that defines the maximum number of recipients to which the framework can send messages at one time.
### Requesting authorization
- [func requestAuthorization(for: [MSRecipient]) async throws -> [MSRecipient : MSCriticalMessagingAuthorizationStatus]](mscriticalsmsmessenger/requestauthorization(for:).md)
  Requests a person’s authorization to send messages to the provided recipients.
### Checking authorization status
- [func checkAuthorizationStatus(for: [MSRecipient]) async throws -> [MSRecipient : MSCriticalMessagingAuthorizationStatus]](mscriticalsmsmessenger/checkauthorizationstatus(for:).md)
  Confirms the current authorization status for sending critical messages from this app.
### Sending critical messages
- [func send(MSCriticalMessage, to: MSRecipient) async throws -> Bool](mscriticalsmsmessenger/send(_:to:).md)
  Sends a critical message to the specified recipient.
### Instance Methods
- [init()](mscriticalsmsmessenger/init.md)
  Creates an instance of the critical messenger object.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Sending SMS messages from an app](critical-messaging-api.md)
  Send critical messages from inside your app using the Critical Messaging API.
- [struct MSRecipient](msrecipient.md)
  A structure that describes the recipient of a critical message.
- [struct MSCriticalMessage](mscriticalmessage.md)
  MSCriticalMessage A simple struct to encapsulate the message string.
- [enum MSCriticalMessagingAuthorizationStatus](mscriticalmessagingauthorizationstatus.md)
  Values that describe the authorization status for the Critical Messaging API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/mscriticalsmsmessenger)*