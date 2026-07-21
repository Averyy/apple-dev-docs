# sendMessage(_:to:using:messageID:)

**Framework**: TelephonyMessagingKit  
**Kind**: method

Sends a custom reaction message to a specified destination.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
final func sendMessage(_ content: RCSMessage.CustomReaction, to destination: RCSHandle, using cellularServiceID: CellularServiceID, messageID: RCSMessageID) async throws
```

## Parameters

- `content`: The content of the message to send, as an instance of [`RCSMessage.CustomReaction`](rcsmessage/customreaction.md).
- `destination`: The destination handle to send the message to.
- `cellularServiceID`: The service identifier to use for the message.
- `messageID`: The message identifier to use for the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/sendmessage(_:to:using:messageid:)-8213t)*