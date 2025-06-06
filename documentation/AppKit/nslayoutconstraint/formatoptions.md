# NSLayoutConstraint.FormatOptions

**Framework**: AppKit  
**Kind**: struct

A bit mask that specifies both a part of an interface element to align and a direction for the alignment between two interface elements.

**Availability**:
- macOS ?+

## Declaration

```swift
struct FormatOptions
```

## Topics

### Constants
- [static var alignAllLeft: NSLayoutConstraint.FormatOptions](nslayoutconstraint/formatoptions/alignallleft.md)
  Align all specified interface elements using [`NSLayoutConstraint.Attribute.left`](nslayoutconstraint/attribute/left.md) on each.
- [static var alignAllRight: NSLayoutConstraint.FormatOptions](nslayoutconstraint/formatoptions/alignallright.md)
  Align all specified interface elements using [`NSLayoutConstraint.Attribute.right`](nslayoutconstraint/attribute/right.md) on each.
- [static var alignAllTop: NSLayoutConstraint.FormatOptions](nslayoutconstraint/formatoptions/alignalltop.md)
  Align all specified interface elements using [`NSLayoutConstraint.Attribute.top`](nslayoutconstraint/attribute/top.md) on each.
- [static var alignAllBottom: NSLayoutConstraint.FormatOptions](nslayoutconstraint/formatoptions/alignallbottom.md)
  Align all specified interface elements using [`NSLayoutConstraint.Attribute.bottom`](nslayoutconstraint/attribute/bottom.md) on each.
- [static var alignAllLeading: NSLayoutConstraint.FormatOptions](nslayoutconstraint/formatoptions/alignallleading.md)
  Align all specified interface elements using [`NSLayoutConstraint.Attribute.leading`](nslayoutconstraint/attribute/leading.md) on each.
- [static var alignAllTrailing: NSLayoutConstraint.FormatOptions](nslayoutconstraint/formatoptions/alignalltrailing.md)
  Align all specified interface elements using [`NSLayoutConstraint.Attribute.trailing`](nslayoutconstraint/attribute/trailing.md) on each.
- [static var alignAllCenterX: NSLayoutConstraint.FormatOptions](nslayoutconstraint/formatoptions/alignallcenterx.md)
  Align all specified interface elements using [`NSLayoutConstraint.Attribute.centerX`](nslayoutconstraint/attribute/centerx.md) on each.
- [static var alignAllCenterY: NSLayoutConstraint.FormatOptions](nslayoutconstraint/formatoptions/alignallcentery.md)
  Align all specified interface elements using [`NSLayoutConstraint.Attribute.centerY`](nslayoutconstraint/attribute/centery.md) on each.
- [static var alignAllLastBaseline: NSLayoutConstraint.FormatOptions](nslayoutconstraint/formatoptions/alignalllastbaseline.md)
  Align all specified interface elements using the last baseline of each one.
- [static var alignAllFirstBaseline: NSLayoutConstraint.FormatOptions](nslayoutconstraint/formatoptions/alignallfirstbaseline.md)
  Align all specified interface elements using the first baseline of each one.
- [static var alignmentMask: NSLayoutConstraint.FormatOptions](nslayoutconstraint/formatoptions/alignmentmask.md)
  Bit mask that can be combined with an [`NSLayoutConstraint.FormatOptions`](nslayoutconstraint/formatoptions.md) variable to yield only the alignment portion of the format options.
- [static var directionLeadingToTrailing: NSLayoutConstraint.FormatOptions](nslayoutconstraint/formatoptions/directionleadingtotrailing.md)
  Arrange objects in order based on the normal text flow for the current user interface language. In left-to-right languages (like English), this arrangement results in the first object being placed farthest to the left, the next one to its right, and so on. In right-to-left languages (like Arabic or Hebrew), the ordering is reversed.
- [static var directionLeftToRight: NSLayoutConstraint.FormatOptions](nslayoutconstraint/formatoptions/directionlefttoright.md)
  Arrange objects in order from left to right.
- [static var directionRightToLeft: NSLayoutConstraint.FormatOptions](nslayoutconstraint/formatoptions/directionrighttoleft.md)
  Arrange objects in order from right to left.
- [static var directionMask: NSLayoutConstraint.FormatOptions](nslayoutconstraint/formatoptions/directionmask.md)
  A bit mask that can be combined with an [`NSLayoutConstraint.FormatOptions`](nslayoutconstraint/formatoptions.md) variable to yield only the direction portion of the format options.
### Initializers
- [init(rawValue: UInt)](nslayoutconstraint/formatoptions/init(rawvalue:).md)
  Creates a formatting-options structure with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [NSLayoutConstraint.Relation](nslayoutconstraint/relation-swift.enum.md)
  The relation between the first attribute and the modified second attribute in a constraint.
- [NSLayoutConstraint.Attribute](nslayoutconstraint/attribute.md)
  The part of the object’s visual representation that should be used to get the value for the constraint.
- [NSLayoutConstraint.Orientation](nslayoutconstraint/orientation.md)
  The layout constraint orientation, either horizontal or vertical, that the constraint uses to enforce layout between objects.
- [struct NSEdgeInsets](../Foundation/NSEdgeInsets.md)
  A description of the distance between the edges of two rectangles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutconstraint/formatoptions)*