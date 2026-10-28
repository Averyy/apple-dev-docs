# preferredThicknessFraction

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The preferred thickness of the split view item relative to the split view.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var preferredThicknessFraction: CGFloat { get set }
```

```objc
@property CGFloat preferredThicknessFraction;
```

## Discussion

This value represents the proportion of the split view that you want the split view item to occupy on a scale of `0.0` to `1.0`. The system uses this value to adjust the thickness of the item in relation to other items when a user double-clicks a neighboring divider, and when the app enters full-screen mode.

The default value of this property is [`unspecifiedDimension`](./unspecifieddimension.md), which means the item doesn’t resize when a user double-clicks the divider, and the system preserves the absolute size when the app enters full-screen mode.

## See Also

### Managing the item thickness
- [var automaticMaximumThickness: CGFloat](./automaticmaximumthickness.md)
  The maximum thickness of the split view item when it resizes due to automatic sizing.
- [var minimumThickness: CGFloat](./minimumthickness.md)
  The minimum thickness of the split view item.
- [var maximumThickness: CGFloat](./maximumthickness.md)
  The maximum thickness of the split view item.
- [class let unspecifiedDimension: CGFloat](./unspecifieddimension.md)
  A constant that resets a dimension’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewitem/preferredthicknessfraction)*