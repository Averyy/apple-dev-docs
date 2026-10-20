# sendMessage(_:to:completion:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func sendMessage(_ message: Data, to: Set<Self.Peer>, completion: @escaping (TabletopSendMessageResult) -> Void)
```

## See Also

### Sending messages between peers
- [func sendMessageUnreliably(Data, to: Set<Self.Peer>, completion: (TabletopSendMessageResult) -> Void)](./sendmessageunreliably%28_,to,completion%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopnetworksessioncoordinator/sendmessage(_:to:completion:))*