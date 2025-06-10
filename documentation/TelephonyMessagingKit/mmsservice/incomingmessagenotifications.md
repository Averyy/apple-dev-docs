# incomingMessageNotifications

**Framework**: TelephonyMessagingKit  
**Kind**: property

An asynchronous sequence of incoming message notifications produced by the service.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
final var incomingMessageNotifications: some AsyncSequence<MMSService.IncomingMessageNotification, Never> { get throws }
```

#### Discussion

Iterate over this sequence with a `for`-`await`-`in` loop to receive [`MMSService.IncomingMessageNotification`](mmsservice/incomingmessagenotification.md) instances that indicate the arrival of incoming messages.

## See Also

- [func receiveMessage(using: CellularServiceID, messageID: MMSMessageID) async throws -> MMSMessage](mmsservice/receivemessage(using:messageid:).md)
  Retrieves an MMS message that matches the given identifiers.
- [struct CellularServiceID](cellularserviceid.md)
  An opaque identifier that represents the cellular service for which to provide operations.
- [struct MMSMessageID](mmsmessageid.md)
  A structure that represents an MMS message identifier.
- [MMSService.IncomingMessageNotification](mmsservice/incomingmessagenotification.md)
  A structure that contains information about an incoming MMS message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmsservice/incomingmessagenotifications)*