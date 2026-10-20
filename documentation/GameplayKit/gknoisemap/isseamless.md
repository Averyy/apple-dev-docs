# isSeamless

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the noise map’s output can repeat seamlessly in all directions.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var isSeamless: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isSeamless) BOOL seamless;
```

#### Discussion

This property is read-only; you choose whether a noise map tiles seamlessly when creating it with the [`interpolatedValue(at:)`](./interpolatedvalue%28at%29.md) initializer.

## See Also

### Inspecting a Noise Map
- [var size: vector_double2](./size.md)
  The size of the “slice” of noise samples contained in the noise map relative to the unit coordinate space of the noise object it was created from.
- [var origin: vector_double2](./origin.md)
  The position of the “slice” of noise samples contained in the noise map relative to the unit coordinate space of the noise object it was created from.
- [var sampleCount: vector_int2](./samplecount.md)
  The width and height of integer grid for which the noise map contains sampled noise values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknoisemap/isseamless)*