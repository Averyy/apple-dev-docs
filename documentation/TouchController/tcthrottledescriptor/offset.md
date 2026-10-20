# offset

**Framework**: Touch Controller  
**Kind**: property  
**Role**: Instance Property

The control’s offset from the anchor, which determines its position.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var offset: CGPoint { get set }
```

```objc
@property (nonatomic, assign) CGPoint offset;
```

## See Also

### Inspecting the descriptor
- [var backgroundContents: TCControlContents?](./backgroundcontents.md)
  The contents for the background of the throttle.
- [var baseValue: CGFloat](./basevalue.md)
  The initial value of this control.
- [var highlightDuration: TimeInterval](./highlightduration.md)
  The time it takes for a highlight to fade away, in seconds.
- [var indicatorContents: TCControlContents?](./indicatorcontents.md)
  The contents for the indicator of the throttle.
- [var indicatorSize: CGSize](./indicatorsize.md)
  The size (width, height) of the indicator itself in points.
- [var label: TCControlLabel](./label.md)
  The label associated with the throttle.
- [var orientation: TCThrottle.Orientation](./orientation.md)
  The orientation of the throttle.
- [var size: CGSize](./size.md)
  The size (width, height) of the throttle in points.
- [var snapsToBaseValue: Bool](./snapstobasevalue.md)
  A Boolean value that indicates whether the control reverts to it’s base value.
- [var throttleSize: CGSize](./throttlesize.md)
  The size (width, height) of the throttle itself, providing boundaries for the indicator, in points.
- [var zIndex: Int](./zindex.md)
  The z-index of the throttle. A lower z-index is drawn first.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tcthrottledescriptor/offset)*