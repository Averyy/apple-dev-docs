# minimumNumberOfTouchesForScrolling

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The minimum number of touches needed for scrolling

**Availability**:
- macOS 27.0+

## Declaration

```swift
var minimumNumberOfTouchesForScrolling: Int { get set }
```

```objc
@property NSInteger minimumNumberOfTouchesForScrolling;
```

## Discussion

Defaults to 1.

## See Also

### Configuring touch scrolling
- [var isTouchScrollingEnabled: Bool](./istouchscrollingenabled.md)
  Enable touch scrolling
- [var maximumNumberOfTouchesForScrolling: Int](./maximumnumberoftouchesforscrolling.md)
  The maximum number of touches needed for scrolling
- [var scrollGestureForRelationships: NSGestureRecognizer](./scrollgestureforrelationships.md)
  A gesture recognizer for setting up failure or exclusion relationships against scrolling gestures
- [var refreshController: NSRefreshController?](./refreshcontroller.md)
  The refresh controller associated with this scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/minimumnumberoftouchesforscrolling)*