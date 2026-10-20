# shadowColor

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The color of any shadow cast by a sprite.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```swift
var shadowColor: UIColor { get set }
```

*macOS*

```swift
var shadowColor: NSColor { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic) UIColor * shadowColor;
```

*macOS*

```objc
@property (nonatomic) NSColor * shadowColor;
```

#### Discussion

The default color is black with an opacity (alpha) of `0.5`.

When lighting is calculated, shadows are created as if a ray was cast out from the light node’s position. If a sprite casts a shadow, the rays are blocked when they intersect with the sprite’s physics body. Otherwise, the sprite’s texture is used to generate a mask, and any pixel in the sprite node’s texture that has an alpha value that is nonzero blocks the light.

Shadows may be cast on content that is rendered prior to the sprite, even if that content does not otherwise interact with the light.

## See Also

### Configuring the Lighting Properties
- [var ambientColor: UIColor](./ambientcolor.md)
  The ambient color of the light.
- [var lightColor: UIColor](./lightcolor.md)
  The diffuse and specular color of the light source.
- [var falloff: CGFloat](./falloff.md)
  The exponent for the rate of decay of the light source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sklightnode/shadowcolor)*