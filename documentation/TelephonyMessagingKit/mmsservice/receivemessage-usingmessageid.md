# receiveMessage(using:messageID:)

**Framework**: TelephonyMessagingKit  
**Kind**: method

Retrieves an MMS message that matches the given identifiers.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
final func receiveMessage(using cellularServiceID: CellularServiceID, messageID: MMSMessageID) async throws -> MMSMessage
```

#### Return Value

The message matching the specified identifiers.

#### Discussion

You get the `cellularServiceID` and `messageID` from an [`MMSService.IncomingMessageNotification`](mmsservice/incomingmessagenotification.md) that you receive from the [`incomingMessageNotifications`](mmsservice/incomingmessagenotifications.md) asynchronous sequence.

> **Note**: [`TelephonyMessagingSession.Error.invalidSession`](telephonymessagingsession/error/invalidsession.md) if the session is no longer valid.

## Parameters

- `cellularServiceID`: The service identifier to use for this request.
- `messageID`: The message identifier for the target message.

## See Also

- [struct CellularServiceID](cellularserviceid.md)
  An opaque identifier that represents the cellular service for which to provide operations.
- [struct MMSMessageID](mmsmessageid.md)
  A structure that represents an MMS message identifier.
- [var incomingMessageNotifications: some AsyncSequence<MMSService.IncomingMessageNotification, Never>](mmsservice/incomingmessagenotifications.md)
  An asynchronous sequence of incoming message notifications produced by the service.
- [MMSService.IncomingMessageNotification](mmsservice/incomingmessagenotification.md)
  A structure that contains information about an incoming MMS message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmsservice/receivemessage(using:messageid:))*