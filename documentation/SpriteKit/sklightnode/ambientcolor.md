# ambientColor

**Framework**: SpriteKit  
**Kind**: property

The ambient color of the light.

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
@MainActor
var ambientColor: NSColor { get set }
```

#### Discussion

The alpha value of the color is ignored. The default color is black, meaning that the light does not have an ambient component. The ambient component of the light is not affected by the light’s [`falloff`](sklightnode/falloff.md) property, nor is it affected by any normal map ([`normalTexture`](skspritenode/normaltexture.md)) on the sprite node.

## See Also

- [var lightColor: UIColor](sklightnode/lightcolor.md)
  The diffuse and specular color of the light source.
- [var shadowColor: UIColor](sklightnode/shadowcolor.md)
  The color of any shadow cast by a sprite.
- [var falloff: CGFloat](sklightnode/falloff.md)
  The exponent for the rate of decay of the light source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sklightnode/ambientcolor)*