# vImage.MultidimensionalLookupTable.InterpolationMethod

**Framework**: Accelerate  
**Kind**: enum  
**Role**: Enumeration

Describes the method a multidimensional lookup table uses the generate interpolated values between lookup table values.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
enum InterpolationMethod
```

## Topics

### Enumeration Cases
- [vImage.MultidimensionalLookupTable.InterpolationMethod.full](./interpolationmethod/full.md)
  Full linear interpolation.
- [vImage.MultidimensionalLookupTable.InterpolationMethod.half](./interpolationmethod/half.md)
  Partial linear interpolation between vertices on gray axis and `N-1` nearest vertices.
- [vImage.MultidimensionalLookupTable.InterpolationMethod.none](./interpolationmethod/none.md)
  Nearest neighbor.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/multidimensionallookuptable/interpolationmethod)*