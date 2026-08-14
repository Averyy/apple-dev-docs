# GKMatchType

**Framework**: GameKit  
**Kind**: enum

The kind of match managed by Game Center.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum GKMatchType
```

## Topics

### Types
- [GKMatchType.peerToPeer](gkmatchtype/peertopeer.md)
  A peer-to-peer match hosted by Game Center.
- [GKMatchType.hosted](gkmatchtype/hosted.md)
  A match hosted on your private server.
- [GKMatchType.turnBased](gkmatchtype/turnbased.md)
  A turn-based match hosted by Game Center.
### Initializers
- [init?(rawValue: UInt)](gkmatchtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class func maxPlayersAllowedForMatch(of: GKMatchType) -> Int](gkmatchrequest/maxplayersallowedformatch(of:).md)
  Returns the maximum number of players allowed in the match request for a given match type.
- [var minPlayers: Int](gkmatchrequest/minplayers.md)
  The minimum number of players that can join the match.
- [var maxPlayers: Int](gkmatchrequest/maxplayers.md)
  The maximum number of players that can join the match.
- [var defaultNumberOfPlayers: Int](gkmatchrequest/defaultnumberofplayers.md)
  The default number of players for the match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchtype)*