# processIncomingMessage(_:from:)

**Framework**: TabletopKit  
**Kind**: method

Pass incoming messages from the reliable channel to the game.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func processIncomingMessage(_ message: Data, from sender: TabletopNetworkSession<Coordinator>.Peer)
```

## Parameters

- `message`: The incoming message
- `sender`: The peer that sent the message


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopnetworksession/processincomingmessage(_:from:))*