# sendMessage(_:)

**Framework**: TelephonyMessagingKit  
**Kind**: method

Sends an SMS message to the given destination.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
final func sendMessage(_ message: SMSMessage) async throws
```

#### Discussion

> **Note**: - [`TelephonyMessagingSession.Error.invalidSession`](telephonymessagingsession/error/invalidsession.md) if the session isn’t valid.

## Parameters

- `message`: The SMS message to send.

## See Also

- [struct SMSMessage](smsmessage.md)
  A structure that contains the data of an SMS message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/smsservice/sendmessage(_:))*