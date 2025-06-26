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

All nodes have their own copy of an attribute value and therefore the attribute values can be different across the same [`SKShader`](skshader.md). If instead you need all nodes to share the same value, use [`SKUniform`](skuniform.md). Uniforms can change values every frame, but uniforms cannot vary per-node like attributes can.

## See Also

- [Controlling Shape Drawing with Shaders](controlling-shape-drawing-with-shaders.md)
  Change a shape node’s appearance by supplying custom shader code.
- [var strokeShader: SKShader?](skshapenode/strokeshader.md)
  A custom shader used to determine the color of the stroked portion of the shape node.
- [var fillShader: SKShader?](skshapenode/fillshader.md)
  A custom shader used to determine the color of the filled portion of the shape node.
- [func setValue(SKAttributeValue, forAttribute: String)](skshapenode/setvalue(_:forattribute:).md)
  Sets an attribute value for an attached shader.
- [func value(forAttributeNamed: String) -> SKAttributeValue?](skshapenode/value(forattributenamed:).md)
  The value of a shader attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshapenode/attributevalues)*