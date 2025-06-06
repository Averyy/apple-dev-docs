# init(frequency:octaveCount:persistence:lacunarity:seed:)

**Framework**: GameplayKit  
**Kind**: init

Creates a billow noise source with the specified parameters.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(frequency: Double, octaveCount: Int, persistence: Double, lacunarity: Double, seed: Int32)
```

#### Return Value

A new noise source.

#### Discussion

To make use of this noise source, create a [`GKNoise`](gknoise.md) object from it (and optionally apply operations to that noise object or combine it with other noise objects). Then create a [`GKNoiseMap`](gknoisemap.md) object from your noise object, generating a concrete field of values that you can sample from directly or visualize using the [`SKTexture`](https://developer.apple.com/documentation/SpriteKit/SKTexture) or `SKTileMap` class.

## Parameters

- `frequency`: The initial value for the   property, which determines the number and size of visible features in any given unit area of generated noise.
- `octaveCount`: The initial value for the   property, which determines the complexity of generated noise.
- `persistence`: The initial value for the   property, which determines the decrease in amplitude between octaves and thus the roughness of generated noise.
- `lacunarity`: The initial value for the   property, which determines the increase in frequency between octaves and thus the gradation between coarseness and uniformity in generated noise.
- `seed`: The initial value for the   property, which determines the overall structure of generated noise.

## See Also

- [var persistence: Double](gkbillownoisesource/persistence.md)
  The rate at which successive octaves of the noise function decrease in amplitude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkbillownoisesource/init(frequency:octavecount:persistence:lacunarity:seed:))*