# TCSpriteRenderer

**Framework**: Touch Controller  
**Kind**: class

A renderer for drawing sprites using Metal.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class TCSpriteRenderer
```

## Topics

### Creating a sprite renderer
- [convenience init(texture: any MTLTexture, size: CGSize)](tcspriterenderer/init(texture:size:).md)
  Creates a new sprite renderer with the specified texture and size.
- [init(texture: any MTLTexture, size: CGSize, highlight: (any MTLTexture)?, offset: CGPoint, colorTint: CGColor)](tcspriterenderer/init(texture:size:highlight:offset:colortint:).md)
  Creates a new sprite renderer with the specified texture, size, highlight texture, offset, and color tint.
### Inspecting a sprite renderer
- [var colorTint: CGColor](tcspriterenderer/colortint.md)
  The color tint to apply to the texture. The color ref is retained.
- [var highlightTexture: (any MTLTexture)?](tcspriterenderer/highlighttexture.md)
  The Metal texture to use for the sprite when highlighted. May be `nil`.
- [var offset: CGPoint](tcspriterenderer/offset.md)
  The offset from the center of the parent control in points.
- [var size: CGSize](tcspriterenderer/size.md)
  The size of the sprite in points.
- [var texture: any MTLTexture](tcspriterenderer/texture.md)
  The Metal texture to use for the sprite.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class TCControlVisuals](tccontrolvisuals.md)
  Represents the visual elements of a touch control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tcspriterenderer)*