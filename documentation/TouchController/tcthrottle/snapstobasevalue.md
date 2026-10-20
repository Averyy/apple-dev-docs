# snapsToBaseValue

**Framework**: Touch Controller  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the control reverts to it’s base value.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var snapsToBaseValue: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL snapsToBaseValue;
```

#### Discussion

If `YES`, the control’s value will revert to its base value when no longer pressed.

## See Also

### Inspecting the throttle
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
- [var throttleSize: CGSize](./throttlesize.md)
  The size (width, height) of the throttle itself, providing boundaries for the indicator, in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tcthrottle/snapstobasevalue)*