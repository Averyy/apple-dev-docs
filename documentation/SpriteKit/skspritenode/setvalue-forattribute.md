# setValue(_:forAttribute:)

**Framework**: SpriteKit  
**Kind**: method

Sets an attribute value for an attached shader.

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
@MainActor
func setValue(_ value: SKAttributeValue, forAttribute key: String)
```

## Parameters

- `value`: An attribute value object containing the scalar or vector value to set in the attached shader.
- `key`: The attribute name.

## See Also

- [Applying Shaders to a Sprite](applying-shaders-to-a-sprite.md)
  Write custom GLSL code that modifies the look of your sprite.
- [var shader: SKShader?](skspritenode/shader.md)
  A text file that defines code that does custom per-pixel drawing or colorization.
- [var attributeValues: [String : SKAttributeValue]](skspritenode/attributevalues.md)
  The values of each attribute associated with the node’s attached shader.
- [func value(forAttributeNamed: String) -> SKAttributeValue?](skspritenode/value(forattributenamed:).md)
  Sets the value of a shader attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skspritenode/setvalue(_:forattribute:))*