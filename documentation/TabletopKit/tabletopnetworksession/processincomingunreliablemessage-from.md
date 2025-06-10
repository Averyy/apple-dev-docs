# processIncomingUnreliableMessage(_:from:)

**Framework**: TabletopKit  
**Kind**: method

Pass incoming messages from the unreliable channel to the game.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
func processIncomingUnreliableMessage(_ message: Data, from sender: TabletopNetworkSession<Coordinator>.Peer)
```

## Parameters

- `message`: The incoming message
- `sender`: The peer that sent the message


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopnetworksession/processincomingunreliablemessage(_:from:))*