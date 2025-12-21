# init(cellularServiceID:handle:messageID:content:)

**Framework**: TelephonyMessagingKit  
**Kind**: init

Initializes an SMS Message for sending to a receipient.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
init(cellularServiceID: CellularServiceID, handle: SMSHandle, messageID: SMSMessageID, content: SMSContent)
```

## Parameters

- `cellularServiceID`: The service identifier to use for the message.
- `handle`: A handle that represents the destination of the message.
- `messageID`: The message identifier to use for this message.
- `content`: The content to send for the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/smsmessage/init(cellularserviceid:handle:messageid:content:))*