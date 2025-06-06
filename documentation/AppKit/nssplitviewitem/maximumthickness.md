# maximumThickness

**Framework**: AppKit  
**Kind**: property

The maximum thickness of the split view item.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var maximumThickness: CGFloat { get set }
```

#### Discussion

This value affects the split view item’s width (for a vertical split view) or height (for a horizontal split view).

The default value of this property is [`unspecifiedDimension`](nssplitviewitem/unspecifieddimension.md), which means the split view item doesn’t enforce a maximum size. However, layout constraints in the contained view hierarchy might specify a maximum size regardless.

## See Also

- [var automaticMaximumThickness: CGFloat](nssplitviewitem/automaticmaximumthickness.md)
  The maximum thickness of the split view item when it resizes due to automatic sizing.
- [var preferredThicknessFraction: CGFloat](nssplitviewitem/preferredthicknessfraction.md)
  The preferred thickness of the split view item relative to the split view.
- [var minimumThickness: CGFloat](nssplitviewitem/minimumthickness.md)
  The minimum thickness of the split view item.
- [class let unspecifiedDimension: CGFloat](nssplitviewitem/unspecifieddimension.md)
  A constant that resets a dimension’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewitem/maximumthickness)*