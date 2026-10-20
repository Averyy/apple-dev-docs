# processIncomingUnreliableMessage(_:from:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Instance Method

Pass incoming messages from the unreliable channel to the game.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
func processIncomingUnreliableMessage(_ message: Data, from sender: TabletopNetworkSession<Coordinator>.Peer)
```

## Parameters

- `message`: The incoming message
- `sender`: The peer that sent the message

## See Also

### Receiving messages from peers
- [func processIncomingMessage(Data, from: TabletopNetworkSession<Coordinator>.Peer)](./processincomingmessage%28_,from%29.md)
  Pass incoming messages from the reliable channel to the game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopnetworksession/processincomingunreliablemessage(_:from:))*