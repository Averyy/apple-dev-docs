# isHosted

**Framework**: GameKit  
**Kind**: property

A Boolean value that indicates whether you host the game on your own servers.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var isHosted: Bool { get }
```

## Mentions

- [Finding players for custom server-based games](finding-players-for-custom-server-based-games.md)

#### Discussion

If the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), you host the game on your own servers. If the value is [`false`](https://developer.apple.com/documentation/Swift/false), Game Center hosts the peer-to-peer match on its servers. The default value is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var sender: GKPlayer](gkinvite/sender.md)
  The player who sends the invitation.
- [var playerAttributes: UInt32](gkinvite/playerattributes.md)
  The player attributes for the match.
- [var playerGroup: Int](gkinvite/playergroup.md)
  The player group for the match.
- [var inviter: String](gkinvite/inviter.md)
  The identifier for the player who sends the invitation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkinvite/ishosted)*