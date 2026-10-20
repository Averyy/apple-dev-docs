# isVisible

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the access point is visible.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var isVisible: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isVisible) BOOL visible;
```

#### Discussion

On Apple TV, you can set this property to [`true`](../../Swift/true.md) to move the focus to the access point. This is an observable property.

## See Also

### Displaying the access point
- [var isActive: Bool](./isactive.md)
  A Boolean value that determines whether to display the access point.
- [var isPresentingGameCenter: Bool](./ispresentinggamecenter.md)
  A Boolean value that indicates whether the game is presenting the Game Center dashboard.
- [var showHighlights: Bool](./showhighlights.md)
  A Boolean value that indicates whether to display highlights for achievements and current ranks for leaderboards.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkaccesspoint/isvisible)*