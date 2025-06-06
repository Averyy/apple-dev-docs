# sampleCount

**Framework**: GameplayKit  
**Kind**: property

The width and height of integer grid for which the noise map contains sampled noise values.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var sampleCount: vector_int2 { get }
```

#### Discussion

This property is read-only; you define the origin of a noise map when creating it with the [`interpolatedValue(at:)`](gknoisemap/interpolatedvalue(at:).md) initializer.

## See Also

- [var size: vector_double2](gknoisemap/size.md)
  The size of the “slice” of noise samples contained in the noise map relative to the unit coordinate space of the noise object it was created from.
- [var origin: vector_double2](gknoisemap/origin.md)
  The position of the “slice” of noise samples contained in the noise map relative to the unit coordinate space of the noise object it was created from.
- [var isSeamless: Bool](gknoisemap/isseamless.md)
  A Boolean value indicating whether the noise map’s output can repeat seamlessly in all directions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknoisemap/samplecount)*