# isPresentingGameCenter

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the game is presenting the Game Center dashboard.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var isPresentingGameCenter: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL isPresentingGameCenter;
```

## Mentions

- [Adding an access point to your game](../adding-an-access-point-to-your-game.md)

#### Discussion

This property is [`true`](../../Swift/true.md) when the player taps the access point control and [`false`](../../Swift/false.md) when the player dismisses the Game Center dashboard. This is an observable property.

## See Also

### Displaying the access point
- [var isActive: Bool](./isactive.md)
  A Boolean value that determines whether to display the access point.
- [var isVisible: Bool](./isvisible.md)
  A Boolean value that indicates whether the access point is visible.
- [var showHighlights: Bool](./showhighlights.md)
  A Boolean value that indicates whether to display highlights for achievements and current ranks for leaderboards.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkaccesspoint/ispresentinggamecenter)*