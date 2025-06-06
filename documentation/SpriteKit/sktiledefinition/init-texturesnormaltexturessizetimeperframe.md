# init(textures:normalTextures:size:timePerFrame:)

**Framework**: SpriteKit  
**Kind**: init

Initializes a new tile definition with arrays of textures and normal textures for animation.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
init(textures: [SKTexture], normalTextures: [SKTexture], size: CGSize, timePerFrame: CGFloat)
```

#### Return Value

A new tile definition.

## Parameters

- `textures`: An array of textures to reference for the definition’s content.
- `normalTextures`: An array of textures to reference for generating normals to simulate 3D lighting.
- `size`: The size of the tile in points.
- `timePerFrame`: The duration, in seconds, that each texture is displayed.

## See Also

- [init(textures: [SKTexture], size: CGSize, timePerFrame: CGFloat)](sktiledefinition/init(textures:size:timeperframe:).md)
  Initializes a new tile definition with an array of textures for animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktiledefinition/init(textures:normaltextures:size:timeperframe:))*