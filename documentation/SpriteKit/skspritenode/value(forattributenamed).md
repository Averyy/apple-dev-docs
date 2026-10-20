# value(forAttributeNamed:)

**Framework**: SpriteKit  
**Kind**: method

Sets the value of a shader attribute.

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
func value(forAttributeNamed key: String) -> SKAttributeValue?
```

#### Return Value

An attribute value object containing the scalar or vector value or `nil` if no such attribute exists.

## Parameters

- `key`: The attribute name.

## See Also

- [Applying Shaders to a Sprite](applying-shaders-to-a-sprite.md)
  Write custom GLSL code that modifies the look of your sprite.
- [var shader: SKShader?](skspritenode/shader.md)
  A text file that defines code that does custom per-pixel drawing or colorization.
- [var attributeValues: [String : SKAttributeValue]](skspritenode/attributevalues.md)
  The values of each attribute associated with the node’s attached shader.
- [func setValue(SKAttributeValue, forAttribute: String)](skspritenode/setvalue(_:forattribute:).md)
  Sets an attribute value for an attached shader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skspritenode/value(forattributenamed:))*