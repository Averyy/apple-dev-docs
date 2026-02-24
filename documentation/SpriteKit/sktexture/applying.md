# applying(_:)

**Framework**: SpriteKit  
**Kind**: method

Creates a new texture by applying a Core Image filter to an existing texture.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
func applying(_ filter: CIFilter) -> Self
```

#### Return Value

A new texture object.

#### Discussion

The image data is copied before control is returned to your game.

## Parameters

- `filter`: A Core Image filter that requires a single `inputImage` parameter and produces an `outputImage` parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktexture/applying(_:))*