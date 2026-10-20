# receiveMessage(using:messageID:)

**Framework**: TelephonyMessagingKit  
**Kind**: method  
**Role**: Instance Method

Retrieves an MMS message that matches the given identifiers.

**Availability**:
- iOS 26.0+ - Deprecated in 26.1

> **Deprecated**: Use IncomingMessageNotification.message instead.

## Declaration

```swift
final func receiveMessage(using cellularServiceID: CellularServiceID, messageID: MMSMessageID) async throws -> MMSMessage
```

#### Return Value

The message matching the specified identifiers.

#### Discussion

You get the `cellularServiceID` and `messageID` from an [`MMSService.IncomingMessageNotification`](./incomingmessagenotification.md) that you receive from the [`incomingMessageNotifications`](./incomingmessagenotifications.md) asynchronous sequence.

> **Throws**: [`TelephonyMessagingSession.Error.invalidSession`](../telephonymessagingsession/error/invalidsession.md) if the session is no longer valid.

## Parameters

- `cellularServiceID`: The service identifier to use for this request.
- `messageID`: The message identifier for the target message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmsservice/receivemessage(using:messageid:))*