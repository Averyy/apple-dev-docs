# ImmersiveDynamicMask.ControlPointInterpolation

**Framework**: Immersive Media Support  
**Kind**: enum

The interpolation methods used while processing control points.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum ControlPointInterpolation
```

## Topics

### Enumeration Cases
- [ImmersiveDynamicMask.ControlPointInterpolation.cubicHermite](immersivedynamicmask/controlpointinterpolation-swift.enum/cubichermite.md)
- [ImmersiveDynamicMask.ControlPointInterpolation.linear](immersivedynamicmask/controlpointinterpolation-swift.enum/linear.md)
### Initializers
- [init(from: any Decoder) throws](immersivedynamicmask/controlpointinterpolation-swift.enum/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [init?(rawValue: Int)](immersivedynamicmask/controlpointinterpolation-swift.enum/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [var rawValue: Int](immersivedynamicmask/controlpointinterpolation-swift.enum/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Instance Methods
- [func encode(to: any Encoder) throws](immersivedynamicmask/controlpointinterpolation-swift.enum/encode(to:).md)
  Encodes this value into the given encoder.
### Type Aliases
- [ImmersiveDynamicMask.ControlPointInterpolation.RawValue](immersivedynamicmask/controlpointinterpolation-swift.enum/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](immersivedynamicmask/controlpointinterpolation-swift.enum/equatable-implementations.md)
- [RawRepresentable Implementations](immersivedynamicmask/controlpointinterpolation-swift.enum/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [ImmersiveDynamicMask.MaskEdgeTreatment](immersivedynamicmask/maskedgetreatment.md)
  Represents edge treatment types for the immersive media mask.
- [ImmersiveDynamicMask.MaskStereoRelation](immersivedynamicmask/maskstereorelation-swift.enum.md)
  An enumeration of the stereo relation of a mask. It determines how left mask relates to the right or vice versa.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivedynamicmask/controlpointinterpolation-swift.enum)*