# attributeValues

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

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
var attributeValues: [String : SKAttributeValue] { get set }
```

```objc
@property (nonatomic, copy, nonnull) NSDictionary<NSString *,SKAttributeValue *> * attributeValues;
```

## Discussion

All nodes have their own copy of an attribute value and therefore the attribute values can be different per-node across the same [`SKShader`](../skshader.md). If instead you need all nodes to share the same value, use [`SKUniform`](../skuniform.md). Uniforms can change values every frame, but uniforms cannot vary per-node like attributes can.

## See Also

### Taking Full Control of Particle Drawing with a Shader
- [Getting Started with Particle Shaders](../getting-started-with-particle-shaders.md)
  Provide custom shader code to alter a particle’s look.
- [var shader: SKShader?](./shader.md)
  A custom shader used to determine how particles are rendered.
- [func setValue(SKAttributeValue, forAttribute: String)](./setvalue%28_,forattribute%29.md)
  Sets an attribute value for an attached shader.
- [func value(forAttributeNamed: String) -> SKAttributeValue?](./value%28forattributenamed%29.md)
  Gets the value of a shader attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/attributevalues)*