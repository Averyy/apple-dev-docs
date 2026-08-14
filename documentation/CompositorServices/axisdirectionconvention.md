# AxisDirectionConvention

**Framework**: Compositor Services  
**Kind**: enum

Constants that indicate the axis and direction to use for a perspective projection matrix.

**Availability**:
- macOS 26.0+
- visionOS 2.0+

## Declaration

```swift
enum AxisDirectionConvention
```

## Topics

### Getting the axis directions
- [AxisDirectionConvention.rightUpBack](axisdirectionconvention/rightupback.md)
  The convention that uses a counterclockwise winding order and positions the leading pixel at the top-left corner of the view.
- [AxisDirectionConvention.rightUpForward](axisdirectionconvention/rightupforward.md)
  The convention that uses a clockwise winding order and positions the leading pixel at the top-left corner of the view.
- [AxisDirectionConvention.rightDownBack](axisdirectionconvention/rightdownback.md)
  The convention that uses a counterclockwise winding order and positions the leading pixel at the bottom-left corner of the view.
- [AxisDirectionConvention.rightDownForward](axisdirectionconvention/rightdownforward.md)
  The convention that uses a clockwise winding order and positions the leading pixel at the bottom-left corner of the view.
### Initializers
- [init?(rawValue: UInt8)](axisdirectionconvention/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/axisdirectionconvention)*