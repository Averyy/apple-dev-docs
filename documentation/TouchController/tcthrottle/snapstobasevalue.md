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

- [var backgroundContents: TCControlContents?](tcthrottle/backgroundcontents.md)
  The contents for the background of the throttle.
- [var baseValue: CGFloat](tcthrottle/basevalue.md)
  The initial value of this control.
- [var highlightDuration: TimeInterval](tcthrottle/highlightduration.md)
  The time it takes for a highlight to fade away, in seconds.
- [var indicatorContents: TCControlContents?](tcthrottle/indicatorcontents.md)
  The contents for the indicator of the throttle.
- [var indicatorSize: CGSize](tcthrottle/indicatorsize.md)
  The size (width, height) of the indicator itself in points.
- [var throttleSize: CGSize](tcthrottle/throttlesize.md)
  The size (width, height) of the throttle itself, providing boundaries for the indicator, in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tcthrottle/snapstobasevalue)*