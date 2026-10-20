# AxisDirectionConvention

**Framework**: Compositor Services  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the axis and direction to use for a perspective projection matrix.

**Availability**:
- macOS 26.0+
- visionOS 2.0+

## Declaration

```swift
enum AxisDirectionConvention
```

```c
enum cp_axis_direction_convention : uint8_t;
```

## Topics

### Getting the axis directions
- [AxisDirectionConvention.rightUpBack](./axisdirectionconvention/rightupback.md)
  The convention that uses a counterclockwise winding order and positions the leading pixel at the top-left corner of the view.
- [AxisDirectionConvention.rightUpForward](./axisdirectionconvention/rightupforward.md)
  The convention that uses a clockwise winding order and positions the leading pixel at the top-left corner of the view.
- [AxisDirectionConvention.rightDownBack](./axisdirectionconvention/rightdownback.md)
  The convention that uses a counterclockwise winding order and positions the leading pixel at the bottom-left corner of the view.
- [AxisDirectionConvention.rightDownForward](./axisdirectionconvention/rightdownforward.md)
  The convention that uses a clockwise winding order and positions the leading pixel at the bottom-left corner of the view.
### Initializers
- [init?(rawValue: UInt8)](./axisdirectionconvention/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/axisdirectionconvention)*