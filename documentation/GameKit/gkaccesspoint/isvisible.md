# isVisible

**Framework**: GameKit  
**Kind**: property

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

#### Discussion

On Apple TV, you can set this property to [`true`](https://developer.apple.com/documentation/swift/true) to move the focus to the access point. This is an observable property.

## See Also

- [var isActive: Bool](gkaccesspoint/isactive.md)
  A Boolean value that determines whether to display the access point.
- [var isPresentingGameCenter: Bool](gkaccesspoint/ispresentinggamecenter.md)
  A Boolean value that indicates whether the game is presenting the Game Center dashboard.
- [var showHighlights: Bool](gkaccesspoint/showhighlights.md)
  A Boolean value that indicates whether to display highlights for achievements and current ranks for leaderboards.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkaccesspoint/isvisible)*