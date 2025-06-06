# init(componentNoises:selectionNoise:componentBoundaries:boundaryBlendDistances:)

**Framework**: GameplayKit  
**Kind**: init

Creates a noise object by combining the specified noise objects, using another noise object and the specified boundaries to select which regions of the output correspond to which input noise.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(componentNoises noises: [GKNoise], selectionNoise: GKNoise, componentBoundaries: [NSNumber], boundaryBlendDistances blendDistances: [NSNumber])
```

#### Return Value

A new noise object.

#### Discussion

Use this method to create a composite noise map where different regions contain different kinds of noise. For example, you can generate realistic terrain textures by creating several noise objects to represent different biomes (such as ocean, grasslands, forests, and mountains), then combining them with this method. This method preserves the [`gradientColors`](gknoise/gradientcolors.md) property of each component noise object, so generating a colorized texture from the result with the [`SKTexture`](https://developer.apple.com/documentation/SpriteKit/SKTexture) [`init(noiseMap:)`](https://developer.apple.com/documentation/SpriteKit/SKTexture/init(noiseMap:)) method uses the color scheme for each component noise object in the regions where its content appears in the composite noise.

Noise values in the `selectionNoise` object determine which component noise objects “show through” in which areas of the output, and the `componentBoundaries` and `blendDistances` parameters determine which values in the selection noise correspond to which objects in the `noises` array. The `componentBoundaries` array defines boundaries between component noise fields, so the number of boundaries must be one less than the count of the `noises` array. (For example, if there are four component noise fields, there are three boundaries between them.) The `blendDistances` array defines the abruptness or smoothness of each boundary, so its count must match that of the `componentBoundaries` array.

For example, if you pass four noise objects for the `noises` parameter, the array `[-0.5, 0.0, 0.75]` for the `componentBoundaries` parameter, and an array of three zeroes for the `blendDistances` parameter, the composite noise uses values from the first noise field in regions where the `selectionNoise` field has values between `-1.0` and `-0.5`, values from the second noise field in regions where the selection noise value is between `-0.5` and `0.0`, and so on. This effect results in hard transitions between the areas corresponding to each component noise field. To soften these transitions, pass values in the `blendDistances` to set the width (in noise values) of each transition.

In this example, if the first value in the `blendDistances` array is `0.1`, the output noise uses values from the first noise field in areas where the selection noise value is between `-1.0` and `-0.55`, then in areas where the selection noise value is between `-0.55` and `-0.45` the output noise smoothly transitions between values from the first and second noise fields.

![None](https://docs-assets.developer.apple.com/published/e17af09b72dc79daddb55ae834daf642/media-2556367%402x.png)

## Parameters

- `noises`: The array of noise objects to combine.
- `selectionNoise`: A noise object whose values determine which object from the   array contributes to which region of the generated output.
- `componentBoundaries`: The count of this array must be one less than the count of the   array.
- `blendDistances`: The count of this array must be one less than the count of the   array (matching the count of the   array).

## See Also

- [convenience init(componentNoises: [GKNoise], selectionNoise: GKNoise)](gknoise/init(componentnoises:selectionnoise:).md)
  Creates a noise object by combining the specified noise objects, using another noise object to select which regions of the output correspond to which input noise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknoise/init(componentnoises:selectionnoise:componentboundaries:boundaryblenddistances:))*