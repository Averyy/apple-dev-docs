# receiveMessage(using:messageID:)

**Framework**: TelephonyMessagingKit  
**Kind**: method

Retrieves an MMS message that matches the given identifiers.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmsservice/receivemessage(using:messageid:))*