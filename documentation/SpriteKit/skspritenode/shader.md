# shader

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

A text file that defines code that does custom per-pixel drawing or colorization.

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
var shader: SKShader? { get set }
```

```objc
@property (nonatomic, retain, nullable) SKShader * shader;
```

## Mentions

- [Applying Shaders to a Sprite](../applying-shaders-to-a-sprite.md)

## Discussion

The default value is `nil`, which means the default behavior for sprite rendering is performed. SpriteKit implements many sprite features using a default shader, such as:

- Animations on [`alpha`](../sknode/alpha.md).
- `SKTexture` [`filteringMode`](../sktexture/filteringmode.md).
- Light from [`SKLightNode`](../sklightnode.md).

If you supply a custom value for `shader`, your custom shader overrides the default shader which neutralizes the default features. It is the responsibility of your custom shader to implement any of the features your sprites require.

## See Also

### Adding a Custom Shader to a Sprite
- [Applying Shaders to a Sprite](../applying-shaders-to-a-sprite.md)
  Write custom GLSL code that modifies the look of your sprite.
- [var attributeValues: [String : SKAttributeValue]](./attributevalues.md)
  The values of each attribute associated with the node’s attached shader.
- [func setValue(SKAttributeValue, forAttribute: String)](./setvalue%28_,forattribute%29.md)
  Sets an attribute value for an attached shader.
- [func value(forAttributeNamed: String) -> SKAttributeValue?](./value%28forattributenamed%29.md)
  Sets the value of a shader attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skspritenode/shader)*