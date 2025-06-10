# sendMessage(_:)

**Framework**: TelephonyMessagingKit  
**Kind**: method

Sends an MMS message to the given destination.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
final func sendMessage(_ message: MMSMessage) async throws
```

#### Discussion

If the [`totalSize`](mmsmessage/totalsize.md) exceeds `MMSConfiguration/maximumMessageSize`, this call fails with [`MMSService.Error.maximumSizeExceeded`](mmsservice/error/maximumsizeexceeded.md).

> **Note**: - [`MMSService.Error`](mmsservice/error.md) if sending the message fails.

## Parameters

- `message`: The MMS message to send.

## See Also

- [struct MMSMessage](mmsmessage.md)
  A structure that contains the data of an MMS message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmsservice/sendmessage(_:))*