# init(frequency:)

**Framework**: GameplayKit  
**Kind**: init  
**Role**: Initializer

Initializes a cylinder noise source with the specified frequency.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(frequency: Double)
```

```objc
- (instancetype) initWithFrequency:(double) frequency;
```

## Return Value

A new noise source.

## Discussion

To make use of this noise source, create a [`GKNoise`](../gknoise.md) object from it (and optionally apply operations to that noise object or combine it with other noise objects). Then create a [`GKNoiseMap`](../gknoisemap.md) object from your noise object, generating a concrete field of values that you can sample from directly or visualize using the [`SKTexture`](../../SpriteKit/sktexture.md) or `SKTileMap` class.

## Parameters

- `frequency`: The initial value for the `frequency` property, which determines the size and spacing of concentric cylinders.

## See Also

### Creating a Noise Source
- [class func cylindersNoise(withFrequency: Double) -> Self](./cylindersnoise%28withfrequency%29.md)
  Creates a cylinder noise source with the specified frequency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkcylindersnoisesource/init(frequency:))*