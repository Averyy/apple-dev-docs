# fillShader

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

A custom shader used to determine the color of the filled portion of the shape node.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var fillShader: SKShader? { get set }
```

```objc
@property (nonatomic, retain, nullable) SKShader * fillShader;
```

## Mentions

- [Controlling Shape Drawing with Shaders](../controlling-shape-drawing-with-shaders.md)

#### Discussion

The default value is `nil`. If a `fillShader` is specified, when the shape node is drawn, the shader is used to determine the output colors for any part of the shape node that’s fillled. SpriteKit implements many fill features using a default shader, such as:

- Fill color.
- Animations on [`alpha`](../sknode/alpha.md).
- Light cast by [`SKLightNode`](../sklightnode.md).

If you supply a custom value for `fillShader`, your custom shader overrides the default shader which neutralizes the default features. It is the responsibility of your custom fillShader to implement any of the features your shape requires.

## See Also

### Customizing Stroking or Fill Drawing
- [Controlling Shape Drawing with Shaders](../controlling-shape-drawing-with-shaders.md)
  Change a shape node’s appearance by supplying custom shader code.
- [var strokeShader: SKShader?](./strokeshader.md)
  A custom shader used to determine the color of the stroked portion of the shape node.
- [var attributeValues: [String : SKAttributeValue]](./attributevalues.md)
  The values of each attribute associated with the node’s attached shader.
- [func setValue(SKAttributeValue, forAttribute: String)](./setvalue%28_,forattribute%29.md)
  Sets an attribute value for an attached shader.
- [func value(forAttributeNamed: String) -> SKAttributeValue?](./value%28forattributenamed%29.md)
  The value of a shader attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshapenode/fillshader)*