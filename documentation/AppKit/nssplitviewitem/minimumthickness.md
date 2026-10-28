# minimumThickness

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The minimum thickness of the split view item.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var minimumThickness: CGFloat { get set }
```

```objc
@property CGFloat minimumThickness;
```

## Discussion

This value affects the split view item’s width (for a vertical split view) or height (for a horizontal split view).

The default value of this property is [`unspecifiedDimension`](./unspecifieddimension.md), which means the split view item doesn’t enforce a minimum size. However, layout constraints in the contained view hierarchy might specify a minimum size regardless.

## See Also

### Managing the item thickness
- [var automaticMaximumThickness: CGFloat](./automaticmaximumthickness.md)
  The maximum thickness of the split view item when it resizes due to automatic sizing.
- [var preferredThicknessFraction: CGFloat](./preferredthicknessfraction.md)
  The preferred thickness of the split view item relative to the split view.
- [var maximumThickness: CGFloat](./maximumthickness.md)
  The maximum thickness of the split view item.
- [class let unspecifiedDimension: CGFloat](./unspecifieddimension.md)
  A constant that resets a dimension’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewitem/minimumthickness)*