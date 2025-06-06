# init(frequency:)

**Framework**: GameplayKit  
**Kind**: init

Initializes a sphere noise source with the specified frequency.

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

#### Return Value

A new noise source.

#### Discussion

To make use of this noise source, create a [`GKNoise`](gknoise.md) object from it (and optionally apply operations to that noise object or combine it with other noise objects). Then create a [`GKNoiseMap`](gknoisemap.md) object from your noise object, generating a concrete field of values that you can sample from directly or visualize using the [`SKTexture`](https://developer.apple.com/documentation/SpriteKit/SKTexture) or `SKTileMap` class.

## Parameters

- `frequency`: The initial value for the   property, which determines the size and spacing of concentric spheres.

## See Also

- [class func spheresNoise(withFrequency: Double) -> Self](gkspheresnoisesource/spheresnoise(withfrequency:).md)
  Creates a sphere noise source with the specified frequency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkspheresnoisesource/init(frequency:))*