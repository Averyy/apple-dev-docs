# init(noiseMap:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Creates a texture from the specified noise map.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(noiseMap: GKNoiseMap)
```

```objc
+ (instancetype) textureWithNoiseMap:(GKNoiseMap *) noiseMap;
```

#### Return Value

A new texture based on the contents of the noise map.

#### Discussion

The [`GKNoiseMap`](../../GameplayKit/gknoisemap.md) class encapsulates the output of procedural noise generation and processing. You use noise sources (the [`GKNoiseSource`](../../GameplayKit/gknoisesource.md) class cluster), noise objects (the [`GKNoise`](../../GameplayKit/gknoise.md) class), and noise maps to generate, process, and combine styles of noise, then use this method to create a graphical representation of the noise for use as a texture image in your game. Noise textures can be useful for imitating natural phenomena such as clouds, stone surfaces, and wood grain. You can also use noise textures as normal maps to make surfaces appear more natural under lighting.

This method colorizes the generated texture using the [`gradientColors`](../../GameplayKit/gknoise/gradientcolors.md) property of the [`GKNoise`](../../GameplayKit/gknoise.md) object from which the noise map was created. By default, that property specifies a simple grayscale ramp, but you can change it to create more colorful textures. When you use the [`init(componentNoises:selectionNoise:)`](../../GameplayKit/gknoise/init%28componentnoises,selectionnoise%29.md) method to combine noise objects, each component noise object keeps its original colors, and the selection noise determines which component noise’s colors appear in which areas of a generated texture.

The following Swift code shows how to create a texture based on Perlin noise:

```swift
let noiseSource = GKPerlinNoiseSource(frequency: 4,
                                      octaveCount: 3,
                                      persistence: 0.2,
                                      lacunarity: 1,
                                      seed: 0)

let noise = GKNoise(noiseSource)

let noiseMap = GKNoiseMap(noise, size: double2(8,8),
                          origin: double2(0,0),
                          sampleCount: int2(640,640),
                          seamless: false)

let noiseTexture = SKTexture(noiseMap: noiseMap)
```

The following image illustrates a sprite node using this texture as both arguments for [`init(texture:normalMap:)`](../skspritenode/init%28texture,normalmap%29.md).

![Sprite node with a GKNoiseMap based texture.](https://developer.apple.com/tutorials/images/com.apple.spritekit/media-2658037@2x.png)

## Parameters

- `noiseMap`: The noise map object from which to generate a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktexture/init(noisemap:))*