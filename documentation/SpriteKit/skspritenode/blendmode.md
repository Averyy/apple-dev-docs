# blendMode

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The blend mode used to draw the sprite into the parent’s framebuffer.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var blendMode: SKBlendMode { get set }
```

```objc
@property (nonatomic) SKBlendMode blendMode;
```

## Mentions

- [Blending a Sprite with Different Interpretations of Alpha](../blending-a-sprite-with-different-interpretations-of-alpha.md)

## Discussion

The default value is [`SKBlendMode.alpha`](../skblendmode/alpha.md).

## See Also

### Configuring Alpha Blendling
- [Blending a Sprite with Different Interpretations of Alpha](../blending-a-sprite-with-different-interpretations-of-alpha.md)
  Reinterpret a sprite’s alpha property to react differently to the objects below it.
- [enum SKBlendMode](../skblendmode.md)
  The modes that describe how the source and destination pixel colors are used to calculate the new destination color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skspritenode/blendmode)*