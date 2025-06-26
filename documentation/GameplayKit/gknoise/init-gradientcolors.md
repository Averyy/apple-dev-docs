# init(_:gradientColors:)

**Framework**: GameplayKit  
**Kind**: init

Initializes a noise object with the specified noise source, with colors for later use in generating noise textures.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(_ noiseSource: GKNoiseSource, gradientColors: [NSNumber : UIColor])
```

#### Return Value

A new noise object.

#### Discussion

To sample from the newly created object’s noise field or generate texture images, create a [`GKNoiseMap`](gknoisemap.md) object from this noise object. Optionally, before doing so you can apply operations to process or transform the noise field, or combine it with other noise objects, to create a more complex or natural noise pattern. For details, see Applying Operations to Noise Values, Applying Operations that Combine Noise, Applying Operations that Distort Noise, Applying Geometric Transformations, and Creating Noise by Combining Noise in [`GKNoise`](gknoise.md).

The `gradientColors` parameter specifies a color ramp as metadata to accompany the noise object. When you later create a [`GKNoiseMap`](gknoisemap.md) object from this noise object and use the [`init(noiseMap:)`](https://developer.apple.com/documentation/SpriteKit/SKTexture/init(noiseMap:)) method to generate a texture image from the noise map, the [`SKTexture`](https://developer.apple.com/documentation/SpriteKit/SKTexture) class automatically uses the gradient colors from the noise map’s underlying noise objects. If you combine noise objects using the [`init(componentNoises:selectionNoise:)`](gknoise/init(componentnoises:selectionnoise:).md) method before generating a noise map, texture generation automatically uses the color gradient corresponding to each component noise for the regions of the noise map where that noise appears.

![None](https://docs-assets.developer.apple.com/published/6fc08fd488d4fee54194e0ac565d63f3/media-2556356%402x.png)

## Parameters

- `noiseSource`: The noise source defining the style and configuration of noise to generate.
- `gradientColors`: A dictionary that specifies a gradient ramp for colorizing generated noise. Each key in this dictionary specifies a value in the generated noise field, and the corresponding value for that key is the color to associate with that noise value when generating textures or images from the noise field. For more details, see the   property.

## See Also

- [convenience init(GKNoiseSource)](gknoise/init(_:).md)
  Initializes a noise object with the specified noise source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknoise/init(_:gradientcolors:))*