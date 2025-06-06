# init(texture:normalTexture:size:)

**Framework**: SpriteKit  
**Kind**: init

Initializes a new tile definition with a single texture and separate normal texture for simulating 3D lighting.

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
init(texture: SKTexture, normalTexture: SKTexture, size: CGSize)
```

#### Return Value

A new tile definition.

## Parameters

- `texture`: The texture to reference for the definition’s content.
- `normalTexture`: The texture to reference for generating normals to simulate 3D lighting.
- `size`: The size of the tile in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktiledefinition/init(texture:normaltexture:size:))*