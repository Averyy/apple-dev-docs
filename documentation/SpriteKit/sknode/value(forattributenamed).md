# value(forAttributeNamed:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

The value of a shader attribute.

**Availability**:
- iOS 10.0+ - Deprecated in 10.0
- iPadOS 10.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.12+ - Deprecated in 10.12
- tvOS 10.0+ - Deprecated in 10.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

> **Deprecated**: Attributes are only available to node classes supporting [`SKShader`](../skshader.md), such as [`SKSpriteNode`](../skspritenode.md), [`SKEffectNode`](../skeffectnode.md) and [`SKShapeNode`](../skshapenode.md).

## Declaration

```swift
func value(forAttributeNamed key: String) -> SKAttributeValue?
```

```objc
- (SKAttributeValue *) valueForAttributeNamed:(NSString *) key;
```

## Return Value

An attribute value object containing the scalar or vector value or `nil` if no such attribute exists.

## Parameters

- `key`: The attribute name.

## See Also

### Setting a Node’s Unique Attributes for a Shader
- [var attributeValues: [String : SKAttributeValue]](./attributevalues.md)
  The values of each attribute associated with the node’s attached shader.
- [func setValue(SKAttributeValue, forAttribute: String)](./setvalue%28_,forattribute%29.md)
  Sets an attribute value for an attached shader


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/value(forattributenamed:))*