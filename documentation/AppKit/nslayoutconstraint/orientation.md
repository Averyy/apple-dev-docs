# NSLayoutConstraint.Orientation

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

The layout constraint orientation, either horizontal or vertical, that the constraint uses to enforce layout between objects.

**Availability**:
- macOS

## Declaration

```swift
enum Orientation
```

```c
enum NSLayoutConstraintOrientation : NSInteger;
```

## Topics

### Constants
- [NSLayoutConstraint.Orientation.horizontal](./orientation/horizontal.md)
  The constraint orientation applied to laying out the horizontal relationship between objects.
- [NSLayoutConstraint.Orientation.vertical](./orientation/vertical.md)
  The constraint orientation applied to laying out the vertical relationship between objects.
### Initializers
- [init?(rawValue: Int)](./orientation/init%28rawvalue%29.md)

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
- [struct NSEdgeInsets](../../Foundation/nsedgeinsets.md)
  A description of the distance between the edges of two rectangles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutconstraint/orientation)*