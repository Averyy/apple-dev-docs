# maximumNumberOfTouchesForScrolling

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The maximum number of touches needed for scrolling

**Availability**:
- macOS 27.0+

## Declaration

```swift
var maximumNumberOfTouchesForScrolling: Int { get set }
```

```objc
@property NSInteger maximumNumberOfTouchesForScrolling;
```

## Discussion

Set this property to 0 to require exactly `minimumNumberOfTouchesForScrolling` touches to recognize the gesture. Defaults to `NSIntegerMax`.

## See Also

### Configuring touch scrolling
- [var isTouchScrollingEnabled: Bool](./istouchscrollingenabled.md)
  Enable touch scrolling
- [var minimumNumberOfTouchesForScrolling: Int](./minimumnumberoftouchesforscrolling.md)
  The minimum number of touches needed for scrolling
- [var scrollGestureForRelationships: NSGestureRecognizer](./scrollgestureforrelationships.md)
  A gesture recognizer for setting up failure or exclusion relationships against scrolling gestures
- [var refreshController: NSRefreshController?](./refreshcontroller.md)
  The refresh controller associated with this scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/maximumnumberoftouchesforscrolling)*