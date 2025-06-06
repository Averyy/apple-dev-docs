# init(texture:alphaThreshold:size:)

**Framework**: SpriteKit  
**Kind**: init

Creates a physics body from the contents of a texture, capturing only the texels that exceed a specified transparency value.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
init(texture: SKTexture, alphaThreshold: Float, size: CGSize)
```

#### Return Value

A new volume-based physics body.

#### Discussion

Use this method when your sprite has a shape that you want replicated in its physics body. The texture is scaled to the new size and then analyzed. A new physics body is created that includes all of the texels in the texture whose alpha values equal or exceed the `alphaThreshold` parameter. The shape of this body attempts to strike a good balance between performance and accuracy. For example, fine details may be ignored if keeping them would cause a significant performance penalty.

## Parameters

- `texture`: The texture to analyze.
- `alphaThreshold`: The minimum alpha value for texels that should be part of the new physics body.
- `size`: The size of the physics body to return.

## See Also

- [Shaping a Physics Body to Match a Node’s Graphics](shaping-a-physics-body-to-match-a-node-s-graphics.md)
  Shape a physics body to your graphics for the right blend of collision accuracy and performance.
- [init(texture: SKTexture, size: CGSize)](skphysicsbody/init(texture:size:).md)
  Creates a physics body from the contents of a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/init(texture:alphathreshold:size:))*