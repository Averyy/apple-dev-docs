# cylindersNoise(withFrequency:)

**Framework**: GameplayKit  
**Kind**: method

Creates a cylinder noise source with the specified frequency.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func cylindersNoise(withFrequency frequency: Double) -> Self
```

#### Return Value

A new noise source.

#### Discussion

To make use of this noise source, create a [`GKNoise`](gknoise.md) object from it (and optionally apply operations to that noise object or combine it with other noise objects). Then create a [`GKNoiseMap`](gknoisemap.md) object from your noise object, generating a concrete field of values that you can sample from directly or visualize using the [`SKTexture`](https://developer.apple.com/documentation/SpriteKit/SKTexture) or `SKTileMap` class.

## Parameters

- `frequency`: The initial value for the   property, which determines the size and spacing of concentric cylinders.

## See Also

- [init(frequency: Double)](gkcylindersnoisesource/init(frequency:).md)
  Initializes a cylinder noise source with the specified frequency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkcylindersnoisesource/cylindersnoise(withfrequency:))*