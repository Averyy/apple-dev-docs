# shader

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

A custom shader used to determine how particles are rendered.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var shader: SKShader? { get set }
```

```objc
@property (nonatomic, retain, nullable) SKShader * shader;
```

## Discussion

The default value is `nil`. If a shader is specified, then the shader is used to determine the output colors for any of the emitter’s particles.

## See Also

### Taking Full Control of Particle Drawing with a Shader
- [Getting Started with Particle Shaders](../getting-started-with-particle-shaders.md)
  Provide custom shader code to alter a particle’s look.
- [var attributeValues: [String : SKAttributeValue]](./attributevalues.md)
  The values of each attribute associated with the node’s attached shader.
- [func setValue(SKAttributeValue, forAttribute: String)](./setvalue%28_,forattribute%29.md)
  Sets an attribute value for an attached shader.
- [func value(forAttributeNamed: String) -> SKAttributeValue?](./value%28forattributenamed%29.md)
  Gets the value of a shader attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/shader)*