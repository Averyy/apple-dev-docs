# constantNoise(withValue:)

**Framework**: GameplayKit  
**Kind**: method

Creates a noise source with the specified constant value.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func constantNoise(withValue value: Double) -> Self
```

#### Return Value

A new noise source.

#### Discussion

To make use of this noise source, create a [`GKNoise`](gknoise.md) object from it (and optionally apply operations to that noise object or combine it with other noise objects). Then create a [`GKNoiseMap`](gknoisemap.md) object from your noise object, generating a concrete field of values that you can sample from directly or visualize using the [`SKTexture`](https://developer.apple.com/documentation/SpriteKit/SKTexture) or `SKTileMap` class.

## Parameters

- `value`: The constant value for the generated noise.

## See Also

- [init(value: Double)](gkconstantnoisesource/init(value:).md)
  Initializes a noise source with the specified constant value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkconstantnoisesource/constantnoise(withvalue:))*