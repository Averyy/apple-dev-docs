# isActive

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether to display the access point.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var isActive: Bool { get set }
```

```objc
@property (nonatomic, assign, getter=isActive) BOOL active;
```

## Mentions

- [Adding an access point to your game](../adding-an-access-point-to-your-game.md)

## Discussion

If this property is [`true`](../../Swift/true.md), the access point appears after you initialize the local player or appears immediately if you’ve already initialized the player.

## See Also

### Displaying the access point
- [var isPresentingGameCenter: Bool](./ispresentinggamecenter.md)
  A Boolean value that indicates whether the game is presenting the Game Center dashboard.
- [var isVisible: Bool](./isvisible.md)
  A Boolean value that indicates whether the access point is visible.
- [var showHighlights: Bool](./showhighlights.md)
  A Boolean value that indicates whether to display highlights for achievements and current ranks for leaderboards.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkaccesspoint/isactive)*