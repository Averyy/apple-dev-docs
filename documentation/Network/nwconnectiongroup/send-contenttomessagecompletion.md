# send(content:to:message:completion:)

**Framework**: Network  
**Kind**: method

Sends data to the entire group, or to a specific member of the group.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@preconcurrency
final func send(content: Data?, to: NWEndpoint? = nil, message: NWConnectionGroup.Message = .default, completion: @escaping (NWError?) -> Void)
```

## Parameters

- `content`: The data to send.
- `to`: An optional endpoint that specifies a member of the group that receives the data. If the endpoint is  , the data will be sent to the entire group.
- `message`: The metadata that defines how the message is sent.
- `completion`: A completion that notifies you when the connection group has processed and sent the data.

## See Also

- [func setReceiveHandler(maximumMessageSize: Int, rejectOversizedMessages: Bool, handler: ((NWConnectionGroup.Message, Data?, Bool) -> Void)?)](nwconnectiongroup/setreceivehandler(maximummessagesize:rejectoversizedmessages:handler:).md)
  Sets a handler that receives inbound messages from members of the group.
- [NWConnectionGroup.Message](nwconnectiongroup/message.md)
  An object that represents a message that you send or receive within a group, and that contains protocol metadata and send properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnectiongroup/send(content:to:message:completion:))*