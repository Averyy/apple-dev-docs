# size

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

The size of the “slice” of noise samples contained in the noise map relative to the unit coordinate space of the noise object it was created from.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var size: vector_double2 { get }
```

```objc
@property (nonatomic, readonly) vector_double2 size;
```

## Discussion

If you later generate a texture image from the noise map with the [`SKTexture`](../../SpriteKit/sktexture.md) class, this size is also the pixel dimensions of the texture to generate.

This property is read-only; you define the size of a noise map when creating it with the [`interpolatedValue(at:)`](./interpolatedvalue%28at%29.md) initializer.

## See Also

### Inspecting a Noise Map
- [var origin: vector_double2](./origin.md)
  The position of the “slice” of noise samples contained in the noise map relative to the unit coordinate space of the noise object it was created from.
- [var sampleCount: vector_int2](./samplecount.md)
  The width and height of integer grid for which the noise map contains sampled noise values.
- [var isSeamless: Bool](./isseamless.md)
  A Boolean value indicating whether the noise map’s output can repeat seamlessly in all directions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknoisemap/size)*