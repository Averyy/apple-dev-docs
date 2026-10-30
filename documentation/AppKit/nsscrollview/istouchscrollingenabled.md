# isTouchScrollingEnabled

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Enable touch scrolling

**Availability**:
- macOS 27.0+

## Declaration

```swift
var isTouchScrollingEnabled: Bool { get set }
```

```objc
@property (getter=isTouchScrollingEnabled) BOOL touchScrollingEnabled;
```

## Discussion

Defaults to `true`.

## See Also

### Configuring touch scrolling
- [var minimumNumberOfTouchesForScrolling: Int](./minimumnumberoftouchesforscrolling.md)
  The minimum number of touches needed for scrolling
- [var maximumNumberOfTouchesForScrolling: Int](./maximumnumberoftouchesforscrolling.md)
  The maximum number of touches needed for scrolling
- [var scrollGestureForRelationships: NSGestureRecognizer](./scrollgestureforrelationships.md)
  A gesture recognizer for setting up failure or exclusion relationships against scrolling gestures
- [var refreshController: NSRefreshController?](./refreshcontroller.md)
  The refresh controller associated with this scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/istouchscrollingenabled)*