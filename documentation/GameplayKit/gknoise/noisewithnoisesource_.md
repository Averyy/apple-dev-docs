# noiseWithNoiseSource:

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Type Method

Creates a noise object with the specified noise source.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) noiseWithNoiseSource:(GKNoiseSource *) noiseSource;
```

## Return Value

A new noise object.

## Discussion

To sample from the newly created object’s noise field or generate texture images, create a [`GKNoiseMap`](../gknoisemap.md) object from this noise object. Optionally, before doing so you can apply operations to process or transform the noise field, or combine it with other noise objects, to create a more complex or natural noise pattern. For details, see Applying Operations to Noise Values, Applying Operations that Combine Noise, Applying Operations that Distort Noise, Applying Geometric Transformations, and Creating Noise by Combining Noise in [`GKNoise`](../gknoise.md).

## Parameters

- `noiseSource`: The noise source defining the style and configuration of noise to generate.

## See Also

### Creating Noise
- [convenience init(GKNoiseSource)](./init%28_%29.md)
  Initializes a noise object with the specified noise source.
- [init(GKNoiseSource, gradientColors: [NSNumber : UIColor])](./init%28_,gradientcolors%29.md)
  Initializes a noise object with the specified noise source, with colors for later use in generating noise textures.
- [+ noiseWithNoiseSource:gradientColors:](./noisewithnoisesource_gradientcolors_.md)
  Creates a noise object with the specified noise source, with colors for later use in generating noise textures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknoise/noisewithnoisesource:)*