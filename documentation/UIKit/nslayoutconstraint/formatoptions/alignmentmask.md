# alignmentMask

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

Bit mask that can be combined with a [`NSLayoutConstraint.FormatOptions`](../formatoptions.md) variable to yield only the alignment portion of the format options.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
static var alignmentMask: NSLayoutConstraint.FormatOptions { get }
```

```c
NSLayoutFormatAlignmentMask
```

## See Also

### Constants
- [static var alignAllLeft: NSLayoutConstraint.FormatOptions](./alignallleft.md)
  Align all specified interface elements using [`NSLayoutConstraint.Attribute.left`](../attribute/left.md) on each.
- [static var alignAllRight: NSLayoutConstraint.FormatOptions](./alignallright.md)
  Align all specified interface elements using [`NSLayoutConstraint.Attribute.right`](../attribute/right.md) on each.
- [static var alignAllTop: NSLayoutConstraint.FormatOptions](./alignalltop.md)
  Align all specified interface elements using [`NSLayoutConstraint.Attribute.top`](../attribute/top.md) on each.
- [static var alignAllBottom: NSLayoutConstraint.FormatOptions](./alignallbottom.md)
  Align all specified interface elements using [`NSLayoutConstraint.Attribute.bottom`](../attribute/bottom.md) on each.
- [static var alignAllLeading: NSLayoutConstraint.FormatOptions](./alignallleading.md)
  Align all specified interface elements using [`NSLayoutConstraint.Attribute.leading`](../attribute/leading.md) on each.
- [static var alignAllTrailing: NSLayoutConstraint.FormatOptions](./alignalltrailing.md)
  Align all specified interface elements using [`NSLayoutConstraint.Attribute.trailing`](../attribute/trailing.md) on each.
- [static var alignAllCenterX: NSLayoutConstraint.FormatOptions](./alignallcenterx.md)
  Align all specified interface elements using [`NSLayoutConstraint.Attribute.centerX`](../attribute/centerx.md) on each.
- [static var alignAllCenterY: NSLayoutConstraint.FormatOptions](./alignallcentery.md)
  Align all specified interface elements using [`NSLayoutConstraint.Attribute.centerY`](../attribute/centery.md) on each.
- [static var alignAllLastBaseline: NSLayoutConstraint.FormatOptions](./alignalllastbaseline.md)
  Align all specified interface elements using the last baseline of each one.
- [static var alignAllFirstBaseline: NSLayoutConstraint.FormatOptions](./alignallfirstbaseline.md)
  Align all specified interface elements using the first baseline of each one.
- [static var directionLeadingToTrailing: NSLayoutConstraint.FormatOptions](./directionleadingtotrailing.md)
  Arrange objects in order based on the normal text flow for the current user interface language. In left-to-right languages (like English), this arrangement results in the first object being placed farthest to the left, the next one to its right, and so on. In right-to-left languages (like Arabic or Hebrew), the ordering is reversed.
- [static var directionLeftToRight: NSLayoutConstraint.FormatOptions](./directionlefttoright.md)
  Arrange objects in order from left to right.
- [static var directionRightToLeft: NSLayoutConstraint.FormatOptions](./directionrighttoleft.md)
  Arrange objects in order from right to left.
- [static var directionMask: NSLayoutConstraint.FormatOptions](./directionmask.md)
  A bit mask that can be combined with an [`NSLayoutConstraint.FormatOptions`](../formatoptions.md) variable to yield only the direction portion of the format options.
- [static var spacingBaselineToBaseline: NSLayoutConstraint.FormatOptions](./spacingbaselinetobaseline.md)
  Align elements vertically according to their baseline positions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutconstraint/formatoptions/alignmentmask)*