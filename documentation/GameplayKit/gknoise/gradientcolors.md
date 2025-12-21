# gradientColors

**Framework**: GameplayKit  
**Kind**: property

A dictionary mapping noise values to colors for use in colorizing generated noise.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var gradientColors: [NSNumber : NSColor] { get set }
```

#### Discussion

The noise object does not store noise values or color bitmap data; instead, this property specifies a color ramp as metadata to accompany the noise object. When you later create a [`GKNoiseMap`](gknoisemap.md) object from this noise object and use the [`init(noiseMap:)`](https://developer.apple.com/documentation/SpriteKit/SKTexture/init(noiseMap:)) method to generate a texture image from the noise map, the [`SKTexture`](https://developer.apple.com/documentation/SpriteKit/SKTexture) class automatically uses the gradient colors from the noise map’s underlying noise objects. If you combine noise objects using the [`init(componentNoises:selectionNoise:)`](gknoise/init(componentnoises:selectionnoise:).md) method before generating a noise map, texture generation automatically uses the color gradient corresponding to each component noise for the regions of the noise map where that noise appears.

Each key in this dictionary specifies a value in the generated noise field, and the corresponding value for that key is the color to associate with that noise value when generating textures or images from the noise field. When the [`SKTexture`](https://developer.apple.com/documentation/SpriteKit/SKTexture) class generates a texture image, it creates a gradient by interpolating colors for noise values in between those you specify.

![None](https://docs-assets.developer.apple.com/published/6fc08fd488d4fee54194e0ac565d63f3/media-2556371%402x.png)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknoise/gradientcolors)*