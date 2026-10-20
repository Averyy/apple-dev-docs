# setValue(_:forAttribute:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

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
func setValue(_ value: SKAttributeValue, forAttribute key: String)
```

```objc
- (void) setValue:(SKAttributeValue *) value forAttributeNamed:(NSString *) key;
```

## Parameters

- `value`: An attribute value object containing the scalar or vector value to set in the attached shader.
- `key`: The attribute name.

## See Also

### Taking Full Control of Particle Drawing with a Shader
- [Getting Started with Particle Shaders](../getting-started-with-particle-shaders.md)
  Provide custom shader code to alter a particle’s look.
- [var shader: SKShader?](./shader.md)
  A custom shader used to determine how particles are rendered.
- [var attributeValues: [String : SKAttributeValue]](./attributevalues.md)
  The values of each attribute associated with the node’s attached shader.
- [func value(forAttributeNamed: String) -> SKAttributeValue?](./value%28forattributenamed%29.md)
  Gets the value of a shader attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/setvalue(_:forattribute:))*