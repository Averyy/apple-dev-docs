# init(frequency:displacement:distanceEnabled:seed:)

**Framework**: GameplayKit  
**Kind**: init  
**Role**: Initializer

Initializes a Voronoi noise source with the specified parameters.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(frequency: Double, displacement: Double, distanceEnabled: Bool, seed: Int32)
```

```objc
- (instancetype) initWithFrequency:(double) frequency displacement:(double) displacement distanceEnabled:(BOOL) distanceEnabled seed:(int32_t) seed;
```

#### Return Value

A new noise source.

#### Discussion

To make use of this noise source, create a [`GKNoise`](../gknoise.md) object from it (and optionally apply operations to that noise object or combine it with other noise objects). Then create a [`GKNoiseMap`](../gknoisemap.md) object from your noise object, generating a concrete field of values that you can sample from directly or visualize using the [`SKTexture`](../../SpriteKit/sktexture.md) or `SKTileMap` class.

## Parameters

- `frequency`: The initial value for the [`frequency`](./frequency.md) property, which determines the number and spacing of cells in generated noise.
- `displacement`: The initial value for the [`displacement`](./displacement.md) property, which determines the variety of noise values between cells in generated noise.
- `distanceEnabled`: The initial value for the [`isDistanceEnabled`](./isdistanceenabled.md) property, which determines whether to add distance values to generated noise.
- `seed`: The initial value for the [`seed`](./seed.md) property, which determines the overall structure of generated noise.

## See Also

### Creating a Noise Source
- [class func voronoiNoise(withFrequency: Double, displacement: Double, distanceEnabled: Bool, seed: Int32) -> Self](./voronoinoise%28withfrequency,displacement,distanceenabled,seed%29.md)
  Creates a Voronoi noise source with the specified parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkvoronoinoisesource/init(frequency:displacement:distanceenabled:seed:))*