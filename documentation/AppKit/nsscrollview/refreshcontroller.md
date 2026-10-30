# refreshController

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The refresh controller associated with this scroll view.

**Availability**:
- macOS 27.0+

## Declaration

```swift
var refreshController: NSRefreshController? { get set }
```

```objc
@property (strong, nullable) NSRefreshController * refreshController;
```

## Discussion

Setting this property adds the refresh controller to the scroll view, enabling pull-to-refresh functionality. Set to nil to remove it.

## See Also

### Configuring touch scrolling
- [var isTouchScrollingEnabled: Bool](./istouchscrollingenabled.md)
  Enable touch scrolling
- [var minimumNumberOfTouchesForScrolling: Int](./minimumnumberoftouchesforscrolling.md)
  The minimum number of touches needed for scrolling
- [var maximumNumberOfTouchesForScrolling: Int](./maximumnumberoftouchesforscrolling.md)
  The maximum number of touches needed for scrolling
- [var scrollGestureForRelationships: NSGestureRecognizer](./scrollgestureforrelationships.md)
  A gesture recognizer for setting up failure or exclusion relationships against scrolling gestures


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/refreshcontroller)*