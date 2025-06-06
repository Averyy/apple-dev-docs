# attributeValues

**Framework**: SpriteKit  
**Kind**: property

The values of each attribute associated with the node’s attached shader.

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
var attributeValues: [String : SKAttributeValue] { get set }
```

#### Discussion

All nodes have their own copy of an attribute value and therefore the attribute values can be different per-node across the same [`SKShader`](skshader.md). If instead you need all nodes to share the same value, use [`SKUniform`](skuniform.md). Uniforms can change values every frame, but uniforms cannot vary per-node like attributes can.

## See Also

- [Applying Shaders to a Sprite](applying-shaders-to-a-sprite.md)
  Write custom GLSL code that modifies the look of your sprite.
- [var shader: SKShader?](skspritenode/shader.md)
  A text file that defines code that does custom per-pixel drawing or colorization.
- [func setValue(SKAttributeValue, forAttribute: String)](skspritenode/setvalue(_:forattribute:).md)
  Sets an attribute value for an attached shader.
- [func value(forAttributeNamed: String) -> SKAttributeValue?](skspritenode/value(forattributenamed:).md)
  Sets the value of a shader attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skspritenode/attributevalues)*