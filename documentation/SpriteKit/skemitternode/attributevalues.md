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
@MainActor
var attributeValues: [String : SKAttributeValue] { get set }
```

#### Discussion

All nodes have their own copy of an attribute value and therefore the attribute values can be different per-node across the same [`SKShader`](skshader.md). If instead you need all nodes to share the same value, use [`SKUniform`](skuniform.md). Uniforms can change values every frame, but uniforms cannot vary per-node like attributes can.

## See Also

- [Getting Started with Particle Shaders](getting-started-with-particle-shaders.md)
  Provide custom shader code to alter a particle’s look.
- [var shader: SKShader?](skemitternode/shader.md)
  A custom shader used to determine how particles are rendered.
- [func setValue(SKAttributeValue, forAttribute: String)](skemitternode/setvalue(_:forattribute:).md)
  Sets an attribute value for an attached shader.
- [func value(forAttributeNamed: String) -> SKAttributeValue?](skemitternode/value(forattributenamed:).md)
  Gets the value of a shader attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/attributevalues)*