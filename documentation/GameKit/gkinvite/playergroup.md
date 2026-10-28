# playerGroup

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The player group for the match.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var playerGroup: Int { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) NSUInteger playerGroup;
```

*macOS*

```objc
@property (atomic, readonly) NSUInteger playerGroup;
```

## Discussion

The value of this property matches the [`playerGroup`](../gkmatchrequest/playergroup.md) property of the match request that the other player uses to create the match.

## See Also

### Getting Properties
- [var sender: GKPlayer](./sender.md)
  The player who sends the invitation.
- [var playerAttributes: UInt32](./playerattributes.md)
  The player attributes for the match.
- [var isHosted: Bool](./ishosted.md)
  A Boolean value that indicates whether you host the game on your own servers.
- [var inviter: String](./inviter.md)
  The identifier for the player who sends the invitation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkinvite/playergroup)*