# UIFloatRange

**Framework**: UIKit  
**Kind**: struct

The range of motion for attached objects.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct UIFloatRange
```

## Topics

### Creating a float range
- [init()](uifloatrange/init.md)
- [init(minimum: CGFloat, maximum: CGFloat)](uifloatrange/init(minimum:maximum:)-8dzgq.md)
  Returns a new float range structure from the given components.
- [static let infinite: UIFloatRange](uifloatrange/infinite.md)
  A range whose range is minus infinity to infinity.
- [static let zero: UIFloatRange](uifloatrange/zero.md)
  A range whose minimum and maximum are both `0.0`.
### Getting the range values
- [var maximum: CGFloat](uifloatrange/maximum.md)
  The maximum range of motion for sliding and pin attachments.
- [var minimum: CGFloat](uifloatrange/minimum.md)
  The minimum range of motion for sliding and pin attachments.
### Testing the range values
- [var isInfinite: Bool](uifloatrange/isinfinite.md)
  Returns a Boolean indicating whether the specified float range is infinitely large.
- [func UIFloatRangeIsEqualToRange(UIFloatRange, UIFloatRange) -> Bool](uifloatrangeisequaltorange(_:_:).md)
  Returns a Boolean indicating whether two float ranges are equivalent.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [UIAttachmentBehavior.AttachmentType](uiattachmentbehavior/attachmenttype.md)
  Constants indicating the type of the attachment behavior object.
- [Float range constants](float-range-constants.md)
  Constants for specifying standard ranges.
- [struct UIOffset](uioffset.md)
  A structure that specifies an amount to offset a position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifloatrange)*