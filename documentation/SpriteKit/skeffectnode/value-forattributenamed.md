# value(forAttributeNamed:)

**Framework**: SpriteKit  
**Kind**: method

Gets the value of a shader attribute.

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
func value(forAttributeNamed key: String) -> SKAttributeValue?
```

#### Return Value

An attribute value object containing the scalar or vector value or `nil` if no such attribute exists.

## Parameters

- `key`: The attribute name.

## See Also

- [var shader: SKShader?](skeffectnode/shader.md)
  A custom shader that is called when the effect node is blended into the parent’s framebuffer.
- [var attributeValues: [String : SKAttributeValue]](skeffectnode/attributevalues.md)
  The values of each attribute associated with the node’s attached shader.
- [func setValue(SKAttributeValue, forAttribute: String)](skeffectnode/setvalue(_:forattribute:).md)
  Sets an attribute value for an attached shader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skeffectnode/value(forattributenamed:))*