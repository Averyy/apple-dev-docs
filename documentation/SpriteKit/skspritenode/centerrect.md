# centerRect

**Framework**: SpriteKit  
**Kind**: property

Enable nine-part stretching of the sprite’s texture.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var centerRect: CGRect { get set }
```

## Mentions

- [Resizing a Sprite in Nine Parts](resizing-a-sprite-in-nine-parts.md)
- [Animating a Sprite by Changing its Texture](animating-a-sprite-by-changing-its-texture.md)

#### Discussion

Controls how the texture is stretched to fill the SKSpriteNode.

The argument rectangle is in the unit coordinate space with a default value of `(0,0)-(1.0,1.0)`, which indicates that the entire texture is stretched to fill the sprite.

If instead you define a different rectangle, its coordinates are used to break the texture into a 3 x 3 grid that is scaled like the following:

- The four corners of this grid are applied without performing any scaling.
- The upper and lower-middle parts are scaled horizontally
- The left and right-middle parts are scaled vertically
- The center is scaled in all directions.

This is what’s referred to as a 9-part scaling algorithm.

## See Also

- [Resizing a Sprite in Nine Parts](resizing-a-sprite-in-nine-parts.md)
  Scale a sprite using nine-part algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skspritenode/centerrect)*