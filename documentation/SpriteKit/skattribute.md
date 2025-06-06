# SKAttribute

**Framework**: SpriteKit  
**Kind**: class

A specification for dynamic per-node data used with a custom shader.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class SKAttribute
```

## Mentions

- [Creating a Custom Fragment Shader](creating-a-custom-fragment-shader.md)

#### Overview

To define an attribute for your shader, you create an [`SKAttribute`](skattribute.md) object with a unique name and data type, which is a [`SKAttributeType`](skattributetype.md) enum. After creating an [`SKShader`](skshader.md) object, custom attributes are added to its [`attributes`](skshader/attributes.md) array. Attribute values are set on the parent node with [`setValue(_:forAttribute:)`](sknode/setvalue(_:forattribute:).md) and can change for each execution of a shader without the need for recompilation.

The following listing shows how you can use an attribute to pass the size of a sprite into a shader using an attribute. In this example, `a_sprite_size` is available as a global `vec2` within the GLSL code.

Listing 1. Passing an attribute to a shader.

```objc
let attributeBasedShader = SKShader(fileNamed: "UsingAttributes.fsh")
attributeBasedShader.attributes = [
    SKAttribute(name: "a_sprite_size", type: .vectorFloat2)]

let sprite = SKSpriteNode()
sprite.shader = attributeBasedShader
sprite.size = CGSize(width: 10, height: 10)
let spriteSize = vector_float2(Float(sprite.frame.size.width), 
                               Float(sprite.frame.size.height))
sprite.setValue(SKAttributeValue(vectorFloat2: spriteSize), 
                forAttribute: "a_sprite_size")
```

## Topics

### Constants
- [enum SKAttributeType](skattributetype.md)
  Options that specify an attribute’s data type.
### Initializers
- [init(name: String, type: SKAttributeType)](skattribute/init(name:type:).md)
  Creates and initializes a new attribute object of a specified type with a name that can be referenced within the shader.
### Instance Properties
- [var name: String](skattribute/name.md)
  The receiver’s name
- [var type: SKAttributeType](skattribute/type.md)
  The data type of the attribute’s value.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class SKShader](skshader.md)
  An object that allows you to apply a custom fragment shader.
- [class SKAttributeValue](skattributevalue.md)
  A container for dynamic shader data associated with a node.
- [class SKUniform](skuniform.md)
  A container for uniform shader data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skattribute)*