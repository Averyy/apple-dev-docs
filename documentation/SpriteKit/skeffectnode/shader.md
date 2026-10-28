# shader

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

A custom shader that is called when the effect node is blended into the parent’s framebuffer.

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

The default value is `nil`, meaning that default blending behavior executes. If a shader is specified, it is called when the rasterized image is blended into the parent’s framebuffer.

## See Also

### Applying a Shader with an Effect Node
- [var attributeValues: [String : SKAttributeValue]](./attributevalues.md)
  The values of each attribute associated with the node’s attached shader.
- [func setValue(SKAttributeValue, forAttribute: String)](./setvalue%28_,forattribute%29.md)
  Sets an attribute value for an attached shader.
- [func value(forAttributeNamed: String) -> SKAttributeValue?](./value%28forattributenamed%29.md)
  Gets the value of a shader attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skeffectnode/shader)*