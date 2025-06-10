# shader

**Framework**: SpriteKit  
**Kind**: property

A custom shader that is called when the effect node is blended into the parent’s framebuffer.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var shader: SKShader? { get set }
```

#### Discussion

The default value is `nil`, meaning that default blending behavior executes. If a shader is specified, it is called when the rasterized image is blended into the parent’s framebuffer.

## See Also

- [var attributeValues: [String : SKAttributeValue]](skeffectnode/attributevalues.md)
  The values of each attribute associated with the node’s attached shader.
- [func setValue(SKAttributeValue, forAttribute: String)](skeffectnode/setvalue(_:forattribute:).md)
  Sets an attribute value for an attached shader.
- [func value(forAttributeNamed: String) -> SKAttributeValue?](skeffectnode/value(forattributenamed:).md)
  Gets the value of a shader attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skeffectnode/shader)*