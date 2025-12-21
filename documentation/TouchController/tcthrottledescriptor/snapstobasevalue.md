# snapsToBaseValue

**Framework**: Touch Controller  
**Kind**: property

A Boolean value that indicates whether the control reverts to it’s base value.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var snapsToBaseValue: Bool { get set }
```

#### Discussion

If `YES`, the control’s value will revert to its base value when no longer pressed.

## See Also

- [var backgroundContents: TCControlContents?](tcthrottledescriptor/backgroundcontents.md)
  The contents for the background of the throttle.
- [var baseValue: CGFloat](tcthrottledescriptor/basevalue.md)
  The initial value of this control.
- [var highlightDuration: TimeInterval](tcthrottledescriptor/highlightduration.md)
  The time it takes for a highlight to fade away, in seconds.
- [var indicatorContents: TCControlContents?](tcthrottledescriptor/indicatorcontents.md)
  The contents for the indicator of the throttle.
- [var indicatorSize: CGSize](tcthrottledescriptor/indicatorsize.md)
  The size (width, height) of the indicator itself in points.
- [var label: TCControlLabel](tcthrottledescriptor/label.md)
  The label associated with the throttle.
- [var offset: CGPoint](tcthrottledescriptor/offset.md)
  The control’s offset from the anchor, which determines its position.
- [var orientation: TCThrottle.Orientation](tcthrottledescriptor/orientation.md)
  The orientation of the throttle.
- [var size: CGSize](tcthrottledescriptor/size.md)
  The size (width, height) of the throttle in points.
- [var throttleSize: CGSize](tcthrottledescriptor/throttlesize.md)
  The size (width, height) of the throttle itself, providing boundaries for the indicator, in points.
- [var zIndex: Int](tcthrottledescriptor/zindex.md)
  The z-index of the throttle. A lower z-index is drawn first.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tcthrottledescriptor/snapstobasevalue)*