# setReceiveHandler(maximumMessageSize:rejectOversizedMessages:handler:)

**Framework**: Network  
**Kind**: method

Sets a handler that receives inbound messages from members of the group.

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
final func setReceiveHandler(maximumMessageSize: Int = Int.max, rejectOversizedMessages: Bool = true, handler: ((NWConnectionGroup.Message, Data?, Bool) -> Void)?)
```

## See Also

- [func send(content: Data?, to: NWEndpoint?, message: NWConnectionGroup.Message, completion: (NWError?) -> Void)](nwconnectiongroup/send(content:to:message:completion:).md)
  Sends data to the entire group, or to a specific member of the group.
- [NWConnectionGroup.Message](nwconnectiongroup/message.md)
  An object that represents a message that you send or receive within a group, and that contains protocol metadata and send properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnectiongroup/setreceivehandler(maximummessagesize:rejectoversizedmessages:handler:))*