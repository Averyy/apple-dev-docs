# backgroundContents

**Framework**: Touch Controller  
**Kind**: property  
**Role**: Instance Property

The contents for the background of the throttle.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var backgroundContents: TCControlContents? { get set }
```

```objc
@property (nonatomic, strong, nullable) TCControlContents * backgroundContents;
```

#### Discussion

May be `nil`.

## See Also

### Inspecting the throttle
- [var baseValue: CGFloat](./basevalue.md)
  The initial value of this control.
- [var highlightDuration: TimeInterval](./highlightduration.md)
  The time it takes for a highlight to fade away, in seconds.
- [var indicatorContents: TCControlContents?](./indicatorcontents.md)
  The contents for the indicator of the throttle.
- [var indicatorSize: CGSize](./indicatorsize.md)
  The size (width, height) of the indicator itself in points.
- [var snapsToBaseValue: Bool](./snapstobasevalue.md)
  A Boolean value that indicates whether the control reverts to it’s base value.
- [var throttleSize: CGSize](./throttlesize.md)
  The size (width, height) of the throttle itself, providing boundaries for the indicator, in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tcthrottle/backgroundcontents)*