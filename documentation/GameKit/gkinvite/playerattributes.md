# playerAttributes

**Framework**: GameKit  
**Kind**: property

The player attributes for the match.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var playerAttributes: UInt32 { get }
```

#### Discussion

The value of this property matches the [`playerAttributes`](gkmatchrequest/playerattributes.md) property of the match request that the other player uses to create the match.

## See Also

- [var sender: GKPlayer](gkinvite/sender.md)
  The player who sends the invitation.
- [var playerGroup: Int](gkinvite/playergroup.md)
  The player group for the match.
- [var isHosted: Bool](gkinvite/ishosted.md)
  A Boolean value that indicates whether you host the game on your own servers.
- [var inviter: String](gkinvite/inviter.md)
  The identifier for the player who sends the invitation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkinvite/playerattributes)*