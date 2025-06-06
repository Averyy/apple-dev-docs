# value(forAttributeNamed:)

**Framework**: SpriteKit  
**Kind**: method

The value of a shader attribute.

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

- [Controlling Shape Drawing with Shaders](controlling-shape-drawing-with-shaders.md)
  Change a shape node’s appearance by supplying custom shader code.
- [var strokeShader: SKShader?](skshapenode/strokeshader.md)
  A custom shader used to determine the color of the stroked portion of the shape node.
- [var fillShader: SKShader?](skshapenode/fillshader.md)
  A custom shader used to determine the color of the filled portion of the shape node.
- [var attributeValues: [String : SKAttributeValue]](skshapenode/attributevalues.md)
  The values of each attribute associated with the node’s attached shader.
- [func setValue(SKAttributeValue, forAttribute: String)](skshapenode/setvalue(_:forattribute:).md)
  Sets an attribute value for an attached shader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshapenode/value(forattributenamed:))*