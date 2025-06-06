# lightColor

**Framework**: SpriteKit  
**Kind**: property

The diffuse and specular color of the light source.

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
var lightColor: NSColor { get set }
```

#### Discussion

The default value is white.

If you are using custom shaders, you can substitute an [`SKUniform`](skuniform.md) object instead.

## See Also

- [var ambientColor: UIColor](sklightnode/ambientcolor.md)
  The ambient color of the light.
- [var shadowColor: UIColor](sklightnode/shadowcolor.md)
  The color of any shadow cast by a sprite.
- [var falloff: CGFloat](sklightnode/falloff.md)
  The exponent for the rate of decay of the light source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sklightnode/lightcolor)*