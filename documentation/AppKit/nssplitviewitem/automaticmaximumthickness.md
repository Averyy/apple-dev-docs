# automaticMaximumThickness

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The maximum thickness of the split view item when it resizes due to automatic sizing.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var automaticMaximumThickness: CGFloat { get set }
```

```objc
@property CGFloat automaticMaximumThickness;
```

## Discussion

Automatic sizing may happen when the split view item has a set [`preferredThicknessFraction`](./preferredthicknessfraction.md) and the app enters full-screen mode, or when other split view items cause the item to change size. The user can still resize the item up to its absolute maximum size in [`maximumThickness`](./maximumthickness.md) by dragging the divider.

The default value of this property is [`unspecifiedDimension`](./unspecifieddimension.md), which means the split view item doesn’t enforce an automatic maximum size.

## See Also

### Managing the item thickness
- [var preferredThicknessFraction: CGFloat](./preferredthicknessfraction.md)
  The preferred thickness of the split view item relative to the split view.
- [var minimumThickness: CGFloat](./minimumthickness.md)
  The minimum thickness of the split view item.
- [var maximumThickness: CGFloat](./maximumthickness.md)
  The maximum thickness of the split view item.
- [class let unspecifiedDimension: CGFloat](./unspecifieddimension.md)
  A constant that resets a dimension’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewitem/automaticmaximumthickness)*