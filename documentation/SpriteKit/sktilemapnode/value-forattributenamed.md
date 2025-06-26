# value(forAttributeNamed:)

**Framework**: SpriteKit  
**Kind**: method

The value of a shader attribute.

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

#### Return Value

An attribute value object containing the scalar or vector value or `nil` if no such attribute exists.

## Parameters

- `key`: The attribute name.

## See Also

- [var shader: SKShader?](sktilemapnode/shader.md)
  Defines a shader which is applied to each tile of the tile map.
- [var attributeValues: [String : SKAttributeValue]](sktilemapnode/attributevalues.md)
  The values of each attribute associated with the node’s attached shader.
- [func setValue(SKAttributeValue, forAttribute: String)](sktilemapnode/setvalue(_:forattribute:).md)
  Sets an attribute value for an attached shader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktilemapnode/value(forattributenamed:))*