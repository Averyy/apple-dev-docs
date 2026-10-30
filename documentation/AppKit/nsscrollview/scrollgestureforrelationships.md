# scrollGestureForRelationships

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A gesture recognizer for setting up failure or exclusion relationships against scrolling gestures

**Availability**:
- macOS 27.0+

## Declaration

```swift
var scrollGestureForRelationships: NSGestureRecognizer { get }
```

```objc
@property (strong, readonly) NSGestureRecognizer * scrollGestureForRelationships;
```

## Mentions

- [Adopting gesture recognizers in your app](../adopting-gesture-recognizers-in-your-app.md)

## See Also

### Configuring touch scrolling
- [var isTouchScrollingEnabled: Bool](./istouchscrollingenabled.md)
  Enable touch scrolling
- [var minimumNumberOfTouchesForScrolling: Int](./minimumnumberoftouchesforscrolling.md)
  The minimum number of touches needed for scrolling
- [var maximumNumberOfTouchesForScrolling: Int](./maximumnumberoftouchesforscrolling.md)
  The maximum number of touches needed for scrolling
- [var refreshController: NSRefreshController?](./refreshcontroller.md)
  The refresh controller associated with this scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/scrollgestureforrelationships)*