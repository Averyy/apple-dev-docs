# automaticMaximumThickness

**Framework**: AppKit  
**Kind**: property

The maximum thickness of the split view item when it resizes due to automatic sizing.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var automaticMaximumThickness: CGFloat { get set }
```

#### Discussion

Automatic sizing may happen when the split view item has a set [`preferredThicknessFraction`](nssplitviewitem/preferredthicknessfraction.md) and the app enters full-screen mode, or when other split view items cause the item to change size. The user can still resize the item up to its absolute maximum size in [`maximumThickness`](nssplitviewitem/maximumthickness.md) by dragging the divider.

The default value of this property is [`unspecifiedDimension`](nssplitviewitem/unspecifieddimension.md), which means the split view item doesn’t enforce an automatic maximum size.

## See Also

- [var preferredThicknessFraction: CGFloat](nssplitviewitem/preferredthicknessfraction.md)
  The preferred thickness of the split view item relative to the split view.
- [var minimumThickness: CGFloat](nssplitviewitem/minimumthickness.md)
  The minimum thickness of the split view item.
- [var maximumThickness: CGFloat](nssplitviewitem/maximumthickness.md)
  The maximum thickness of the split view item.
- [class let unspecifiedDimension: CGFloat](nssplitviewitem/unspecifieddimension.md)
  A constant that resets a dimension’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewitem/automaticmaximumthickness)*