# attributeValues

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The values of each attribute associated with the node’s attached shader.

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
var attributeValues: [String : SKAttributeValue] { get set }
```

```objc
@property (nonatomic, copy, nonnull) NSDictionary<NSString *,SKAttributeValue *> * attributeValues;
```

#### Discussion

All nodes have their own copy of an attribute value and therefore the attribute values can be different across the same `SKShader`. If instead you need all nodes to share the same value, use `SKUniform`. Uniforms can change values every frame, but uniforms cannot vary per-node like attributes can.

## See Also

### Setting a Node’s Unique Attributes for a Shader
- [func setValue(SKAttributeValue, forAttribute: String)](./setvalue%28_,forattribute%29.md)
  Sets an attribute value for an attached shader
- [func value(forAttributeNamed: String) -> SKAttributeValue?](./value%28forattributenamed%29.md)
  The value of a shader attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/attributevalues)*