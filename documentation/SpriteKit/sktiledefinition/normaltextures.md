# normalTextures

**Framework**: SpriteKit  
**Kind**: property

An array of [`SKTexture`](sktexture.md) objects used to generate the normals for the tile to simulate 3D lighting.

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
var normalTextures: [SKTexture] { get set }
```

#### Discussion

If the tile is non-animated, this will be an array containing one texture.

## See Also

- [var textures: [SKTexture]](sktiledefinition/textures.md)
  An array of [`SKTexture`](sktexture.md) objects that defines the tile definition object’s content.
- [var timePerFrame: CGFloat](sktiledefinition/timeperframe.md)
  The duration, in seconds, that each texture in the textures array is displayed before switching to the next texture in the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktiledefinition/normaltextures)*