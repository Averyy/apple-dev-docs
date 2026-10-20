# sendMessage(_:)

**Framework**: TelephonyMessagingKit  
**Kind**: method  
**Role**: Instance Method

Sends an MMS message to the given destination.

**Availability**:
- iOS 26.0+

## Declaration

```swift
final func sendMessage(_ message: MMSMessage) async throws
```

#### Discussion

If the [`totalSize`](../mmsmessage/totalsize.md) exceeds [`maximumMessageSize`](./configuration/maximummessagesize.md), this call fails with [`MMSService.Error.maximumSizeExceeded`](./error/maximumsizeexceeded.md).

> **Throws**:
>
> - [`MMSService.Error`](./error.md) if sending the message fails.

## Parameters

- `message`: The MMS message to send.

## See Also

### Sending messages
- [struct MMSMessage](../mmsmessage.md)
  A structure that contains the data of an MMS message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmsservice/sendmessage(_:))*