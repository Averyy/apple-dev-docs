# NSLayoutConstraint.FormatOptions

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

A bit mask that specifies both a part of an interface element to align and a direction for the alignment between two interface elements.

**Availability**:
- macOS

## Declaration

```swift
struct FormatOptions
```

```c
enum NSLayoutFormatOptions : NSUInteger;
```

## Topics

### Constants
- [static var alignAllLeft: NSLayoutConstraint.FormatOptions](./formatoptions/alignallleft.md)
  Align all specified interface elements using [`NSLayoutConstraint.Attribute.left`](./attribute/left.md) on each.
- [static var alignAllRight: NSLayoutConstraint.FormatOptions](./formatoptions/alignallright.md)
  Align all specified interface elements using [`NSLayoutConstraint.Attribute.right`](./attribute/right.md) on each.
- [static var alignAllTop: NSLayoutConstraint.FormatOptions](./formatoptions/alignalltop.md)
  Align all specified interface elements using [`NSLayoutConstraint.Attribute.top`](./attribute/top.md) on each.
- [static var alignAllBottom: NSLayoutConstraint.FormatOptions](./formatoptions/alignallbottom.md)
  Align all specified interface elements using [`NSLayoutConstraint.Attribute.bottom`](./attribute/bottom.md) on each.
- [static var alignAllLeading: NSLayoutConstraint.FormatOptions](./formatoptions/alignallleading.md)
  Align all specified interface elements using [`NSLayoutConstraint.Attribute.leading`](./attribute/leading.md) on each.
- [static var alignAllTrailing: NSLayoutConstraint.FormatOptions](./formatoptions/alignalltrailing.md)
  Align all specified interface elements using [`NSLayoutConstraint.Attribute.trailing`](./attribute/trailing.md) on each.
- [static var alignAllCenterX: NSLayoutConstraint.FormatOptions](./formatoptions/alignallcenterx.md)
  Align all specified interface elements using [`NSLayoutConstraint.Attribute.centerX`](./attribute/centerx.md) on each.
- [static var alignAllCenterY: NSLayoutConstraint.FormatOptions](./formatoptions/alignallcentery.md)
  Align all specified interface elements using [`NSLayoutConstraint.Attribute.centerY`](./attribute/centery.md) on each.
- [static var alignAllLastBaseline: NSLayoutConstraint.FormatOptions](./formatoptions/alignalllastbaseline.md)
  Align all specified interface elements using the last baseline of each one.
- [static var alignAllFirstBaseline: NSLayoutConstraint.FormatOptions](./formatoptions/alignallfirstbaseline.md)
  Align all specified interface elements using the first baseline of each one.
- [static var alignmentMask: NSLayoutConstraint.FormatOptions](./formatoptions/alignmentmask.md)
  Bit mask that can be combined with an [`NSLayoutConstraint.FormatOptions`](./formatoptions.md) variable to yield only the alignment portion of the format options.
- [static var directionLeadingToTrailing: NSLayoutConstraint.FormatOptions](./formatoptions/directionleadingtotrailing.md)
  Arrange objects in order based on the normal text flow for the current user interface language. In left-to-right languages (like English), this arrangement results in the first object being placed farthest to the left, the next one to its right, and so on. In right-to-left languages (like Arabic or Hebrew), the ordering is reversed.
- [static var directionLeftToRight: NSLayoutConstraint.FormatOptions](./formatoptions/directionlefttoright.md)
  Arrange objects in order from left to right.
- [static var directionRightToLeft: NSLayoutConstraint.FormatOptions](./formatoptions/directionrighttoleft.md)
  Arrange objects in order from right to left.
- [static var directionMask: NSLayoutConstraint.FormatOptions](./formatoptions/directionmask.md)
  A bit mask that can be combined with an [`NSLayoutConstraint.FormatOptions`](./formatoptions.md) variable to yield only the direction portion of the format options.
### Initializers
- [init(rawValue: UInt)](./formatoptions/init%28rawvalue%29.md)
  Creates a formatting-options structure with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Constants
- [NSLayoutConstraint.Relation](./relation-swift.enum.md)
  The relation between the first attribute and the modified second attribute in a constraint.
- [NSLayoutConstraint.Attribute](./attribute.md)
  The part of the object’s visual representation that should be used to get the value for the constraint.
- [NSLayoutConstraint.Orientation](./orientation.md)
  The layout constraint orientation, either horizontal or vertical, that the constraint uses to enforce layout between objects.
- [struct NSEdgeInsets](../../Foundation/nsedgeinsets.md)
  A description of the distance between the edges of two rectangles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutconstraint/formatoptions)*