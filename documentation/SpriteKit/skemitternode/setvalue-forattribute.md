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

- [Getting Started with Particle Shaders](getting-started-with-particle-shaders.md)
  Provide custom shader code to alter a particle’s look.
- [var shader: SKShader?](skemitternode/shader.md)
  A custom shader used to determine how particles are rendered.
- [var attributeValues: [String : SKAttributeValue]](skemitternode/attributevalues.md)
  The values of each attribute associated with the node’s attached shader.
- [func value(forAttributeNamed: String) -> SKAttributeValue?](skemitternode/value(forattributenamed:).md)
  Gets the value of a shader attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/setvalue(_:forattribute:))*