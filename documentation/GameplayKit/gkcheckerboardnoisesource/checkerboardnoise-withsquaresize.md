# checkerboardNoise(withSquareSize:)

**Framework**: GameplayKit  
**Kind**: method

Creates a checkerboard noise source with the specified square size.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func checkerboardNoise(withSquareSize squareSize: Double) -> Self
```

#### Return Value

A new noise source.

#### Discussion

To make use of this noise source, create a [`GKNoise`](gknoise.md) object from it (and optionally apply operations to that noise object or combine it with other noise objects). Then create a [`GKNoiseMap`](gknoisemap.md) object from your noise object, generating a concrete field of values that you can sample from directly or visualize using the [`SKTexture`](https://developer.apple.com/documentation/SpriteKit/SKTexture) or `SKTileMap` class.

## Parameters

- `squareSize`: The initial value for the   property, which determines the size of the checkerboard pattern.

## See Also

- [init(squareSize: Double)](gkcheckerboardnoisesource/init(squaresize:).md)
  Initializes a checkerboard noise source with the specified square size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkcheckerboardnoisesource/checkerboardnoise(withsquaresize:))*