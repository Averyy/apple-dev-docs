# NSLayoutConstraint.Axis

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Keys that specify a horizontal or vertical layout constraint between objects.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum Axis
```

```c
enum UILayoutConstraintAxis : NSInteger;
```

## Topics

### Constants
- [NSLayoutConstraint.Axis.horizontal](./axis/horizontal.md)
  The constraint applied when laying out the horizontal relationship between objects.
- [NSLayoutConstraint.Axis.vertical](./axis/vertical.md)
  The constraint applied when laying out the vertical relationship between objects.
### Initializers
- [init?(rawValue: Int)](./axis/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [NSLayoutConstraint.Relation](./relation-swift.enum.md)
  The relation between the first attribute and the modified second attribute in a constraint.
- [NSLayoutConstraint.Attribute](./attribute.md)
  The part of the object’s visual representation that should be used to get the value for the constraint.
- [NSLayoutConstraint.FormatOptions](./formatoptions.md)
  A bit mask that specifies both a part of an interface element to align and a direction for the alignment between two interface elements.
- [NSLayoutConstraint.Orientation](../../AppKit/nslayoutconstraint/orientation.md)
  The layout constraint orientation, either horizontal or vertical, that the constraint uses to enforce layout between objects.
- [struct NSEdgeInsets](../../Foundation/nsedgeinsets.md)
  A description of the distance between the edges of two rectangles.
- [var NSLAYOUTCONSTRAINT_H: Int32](../nslayoutconstraint_h.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutconstraint/axis)*