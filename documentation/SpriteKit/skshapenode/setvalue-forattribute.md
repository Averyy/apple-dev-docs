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

- [Controlling Shape Drawing with Shaders](controlling-shape-drawing-with-shaders.md)
  Change a shape node’s appearance by supplying custom shader code.
- [var strokeShader: SKShader?](skshapenode/strokeshader.md)
  A custom shader used to determine the color of the stroked portion of the shape node.
- [var fillShader: SKShader?](skshapenode/fillshader.md)
  A custom shader used to determine the color of the filled portion of the shape node.
- [var attributeValues: [String : SKAttributeValue]](skshapenode/attributevalues.md)
  The values of each attribute associated with the node’s attached shader.
- [func value(forAttributeNamed: String) -> SKAttributeValue?](skshapenode/value(forattributenamed:).md)
  The value of a shader attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshapenode/setvalue(_:forattribute:))*