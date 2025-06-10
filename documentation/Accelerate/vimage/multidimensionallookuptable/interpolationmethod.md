# vImage.MultidimensionalLookupTable.InterpolationMethod

**Framework**: Accelerate  
**Kind**: enum

Describes the method a multidimensional lookup table uses the generate interpolated values between lookup table values.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
enum InterpolationMethod
```

## Topics

### Enumeration Cases
- [vImage.MultidimensionalLookupTable.InterpolationMethod.full](vimage/multidimensionallookuptable/interpolationmethod/full.md)
  Full linear interpolation.
- [vImage.MultidimensionalLookupTable.InterpolationMethod.half](vimage/multidimensionallookuptable/interpolationmethod/half.md)
  Partial linear interpolation between vertices on gray axis and `N-1` nearest vertices.
- [vImage.MultidimensionalLookupTable.InterpolationMethod.none](vimage/multidimensionallookuptable/interpolationmethod/none.md)
  Nearest neighbor.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/multidimensionallookuptable/interpolationmethod)*