# sendMessage(_:to:using:messageID:)

**Framework**: TelephonyMessagingKit  
**Kind**: method

Sends a reaction message to a specified destination.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
final func sendMessage(_ content: RCSMessage.Reaction, to destination: RCSHandle, using cellularServiceID: CellularServiceID, messageID: RCSMessageID) async throws
```

#### Discussion

> **Note**:  If the reaction content is not a valid emoji sequence, this method throws [`RCSService.Error.invalidArgument`](rcsservice/error/invalidargument.md).

## Parameters

- `content`: The content of the message to send, as an instance of [`RCSMessage.Reaction`](rcsmessage/reaction.md).
- `destination`: The destination handle to send the message to.
- `cellularServiceID`: The service identifier to use for the message.
- `messageID`: The message identifier to use for the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/sendmessage(_:to:using:messageid:)-6kuet)*