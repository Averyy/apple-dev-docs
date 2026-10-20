# MSCriticalSMSMessenger

**Framework**: Messages  
**Kind**: class  
**Role**: Class

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
- [var maximumCriticalMessagingRecipients: Int](./mscriticalsmsmessenger/maximumcriticalmessagingrecipients.md)
  An integer that defines the maximum number of recipients to which the framework can send messages at one time.
### Requesting authorization
- [func requestAuthorization(for: [MSRecipient]) async throws -> [MSRecipient : MSCriticalMessagingAuthorizationStatus]](./mscriticalsmsmessenger/requestauthorization%28for%29.md)
  Requests a person’s authorization to send messages to the provided recipients.
### Checking authorization status
- [func checkAuthorizationStatus(for: [MSRecipient]) async throws -> [MSRecipient : MSCriticalMessagingAuthorizationStatus]](./mscriticalsmsmessenger/checkauthorizationstatus%28for%29.md)
  Confirms the current authorization status for sending critical messages from this app.
### Sending critical messages
- [func send(MSCriticalMessage, to: MSRecipient) async throws -> Bool](./mscriticalsmsmessenger/send%28_,to%29.md)
  Sends a critical message to the specified recipient.
### Instance Methods
- [init()](./mscriticalsmsmessenger/init%28%29.md)
  Creates an instance of the critical messenger object.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Critical messages
- [Sending SMS messages from an app](./critical-messaging-api.md)
  Send critical messages from inside your app using the Critical Messaging API.
- [struct MSRecipient](./msrecipient.md)
  A structure that describes the recipient of a critical message.
- [struct MSCriticalMessage](./mscriticalmessage.md)
  A message for critical communications.
- [enum MSCriticalMessagingAuthorizationStatus](./mscriticalmessagingauthorizationstatus.md)
  Values that describe the authorization status for the Critical Messaging API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/mscriticalsmsmessenger)*