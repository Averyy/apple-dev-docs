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
func setValue(_ value: SKAttributeValue, forAttribute key: String)
```

## Parameters

- `value`: An attribute value object containing the scalar or vector value to set in the attached shader.
- `key`: The attribute name.

## See Also

- [var shader: SKShader?](skeffectnode/shader.md)
  A custom shader that is called when the effect node is blended into the parent’s framebuffer.
- [var attributeValues: [String : SKAttributeValue]](skeffectnode/attributevalues.md)
  The values of each attribute associated with the node’s attached shader.
- [func value(forAttributeNamed: String) -> SKAttributeValue?](skeffectnode/value(forattributenamed:).md)
  Gets the value of a shader attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skeffectnode/setvalue(_:forattribute:))*