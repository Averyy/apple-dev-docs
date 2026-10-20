# value(forAttributeNamed:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

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
func value(forAttributeNamed key: String) -> SKAttributeValue?
```

```objc
- (SKAttributeValue *) valueForAttributeNamed:(NSString *) key;
```

#### Return Value

An attribute value object containing the scalar or vector value or `nil` if no such attribute exists.

## Parameters

- `key`: The attribute name.

## See Also

### Taking Full Control of Particle Drawing with a Shader
- [Getting Started with Particle Shaders](../getting-started-with-particle-shaders.md)
  Provide custom shader code to alter a particle’s look.
- [var shader: SKShader?](./shader.md)
  A custom shader used to determine how particles are rendered.
- [var attributeValues: [String : SKAttributeValue]](./attributevalues.md)
  The values of each attribute associated with the node’s attached shader.
- [func setValue(SKAttributeValue, forAttribute: String)](./setvalue%28_,forattribute%29.md)
  Sets an attribute value for an attached shader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/value(forattributenamed:))*