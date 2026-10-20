# Peer

**Framework**: TabletopKit  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

**Availability**:
- visionOS 2.0+

## Declaration

```swift
associatedtype Peer : Hashable, Identifiable where Self.Peer.ID == UUID
```

## See Also

### Managing network session peers
- [func peerJoinedGame(Self.Peer.ID)](./peerjoinedgame%28_%29.md)
- [func peerLeftGame(Self.Peer.ID)](./peerleftgame%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopnetworksessioncoordinator/peer)*