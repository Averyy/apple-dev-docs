# init(_:)

**Framework**: GameplayKit  
**Kind**: init  
**Role**: Initializer

Initializes a noise map by sampling from the specified noise object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(_ noise: GKNoise)
```

```objc
- (instancetype) initWithNoise:(GKNoise *) noise;
```

## Return Value

A new noise map object.

## Discussion

This initializer is equivalent to calling the [`init(_:size:origin:sampleCount:seamless:)`](./init%28_,size,origin,samplecount,seamless%29.md) initializer with a size of `1.0 x 1.0`, an origin of `[0, 0]`, a sample grid size of `100 x 100`, and a `seamless` parameter of [`false`](../../Swift/false.md).

[`GKNoiseSource`](../gknoisesource.md) and [`GKNoise`](../gknoise.md) objects are lightweight descriptions of noise generation and processing parameters. When you create a noise map from a noise object, GameplayKit performs the computation described by those objects to create an grid of noise sample values. You can then read those values (or interpolated values at non-integral positions on that grid) with the methods listed in Accessing Noise Values in [`GKNoiseMap`](../gknoisemap.md), or use the [`SKTexture`](../../SpriteKit/sktexture.md) or `SKTileMap` classes to generate texture images or tile maps from the generated noise.

For more information, see [GameplayKit Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Parameters

- `noise`: The noise object from which to create a noise map.

## See Also

### Creating a Noise Map
- [init(GKNoise, size: vector_double2, origin: vector_double2, sampleCount: vector_int2, seamless: Bool)](./init%28_,size,origin,samplecount,seamless%29.md)
  Creates a noise map by sampling from the specified noise object.
- [convenience init()](./init%28%29.md)
  Initializes a noise map with a constant noise value of zero throughout.
- [+ noiseMapWithNoise:](./noisemapwithnoise_.md)
  Creates a noise map by sampling from the specified noise object.
- [+ noiseMapWithNoise:size:origin:sampleCount:seamless:](./noisemapwithnoise_size_origin_samplecount_seamless_.md)
  Creates a noise map by sampling from the specified noise object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknoisemap/init(_:))*