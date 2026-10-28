# unspecifiedDimension

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A constant that resets a dimension’s value.

**Availability**:
- macOS 10.11+

## Declaration

```swift
class let unspecifiedDimension: CGFloat
```

```c
extern const CGFloat NSSplitViewItemUnspecifiedDimension;
```

## Discussion

Use this constant with any sizing-related [`NSSplitViewItem`](../nssplitviewitem.md) property to reset its value to the standard system default.

## See Also

### Managing the item thickness
- [var automaticMaximumThickness: CGFloat](./automaticmaximumthickness.md)
  The maximum thickness of the split view item when it resizes due to automatic sizing.
- [var preferredThicknessFraction: CGFloat](./preferredthicknessfraction.md)
  The preferred thickness of the split view item relative to the split view.
- [var minimumThickness: CGFloat](./minimumthickness.md)
  The minimum thickness of the split view item.
- [var maximumThickness: CGFloat](./maximumthickness.md)
  The maximum thickness of the split view item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewitem/unspecifieddimension)*