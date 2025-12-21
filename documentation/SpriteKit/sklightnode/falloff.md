# falloff

**Framework**: SpriteKit  
**Kind**: property

The exponent for the rate of decay of the light source.

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
var falloff: CGFloat { get set }
```

#### Discussion

The default value is `1.0`, which means the light decays linearly with distance. The value must be a positive number less than or equal to `1.0`.

## See Also

- [var ambientColor: UIColor](sklightnode/ambientcolor.md)
  The ambient color of the light.
- [var lightColor: UIColor](sklightnode/lightcolor.md)
  The diffuse and specular color of the light source.
- [var shadowColor: UIColor](sklightnode/shadowcolor.md)
  The color of any shadow cast by a sprite.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sklightnode/falloff)*