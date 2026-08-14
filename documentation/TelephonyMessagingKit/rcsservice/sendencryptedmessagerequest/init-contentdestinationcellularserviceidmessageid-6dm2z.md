# init(content:destination:cellularServiceID:messageID:)

**Framework**: TelephonyMessagingKit  
**Kind**: init

Creates a new send encrypted message request with the given parameters.

**Availability**:
- iOS 26.5+

## Declaration

```swift
init(content: RCSMessage.Text, destination: RCSHandle, cellularServiceID: CellularServiceID, messageID: RCSMessageID)
```

## Parameters

- `content`: The content of the message to send, as an instance of [`RCSMessage.Text`](rcsmessage/text.md).
- `destination`: The destination handle to send the message to.
- `cellularServiceID`: The service identifier to use for the message.
- `messageID`: The message identifier to use for the message.

## See Also

- [init(content: RCSMessage.GeolocationPush, destination: RCSHandle, cellularServiceID: CellularServiceID, messageID: RCSMessageID)](rcsservice/sendencryptedmessagerequest/init(content:destination:cellularserviceid:messageid:)-3ox0y.md)
  Creates a new send encrypted message request with the given parameters.
- [init(content: RCSMessage.FileTransfer, destination: RCSHandle, cellularServiceID: CellularServiceID, messageID: RCSMessageID)](rcsservice/sendencryptedmessagerequest/init(content:destination:cellularserviceid:messageid:)-jqfv.md)
  Creates a new send encrypted message request with the given parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/sendencryptedmessagerequest/init(content:destination:cellularserviceid:messageid:)-6dm2z)*