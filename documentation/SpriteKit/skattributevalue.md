# SKAttributeValue

**Framework**: SpriteKit  
**Kind**: class  
**Role**: Class

A container for dynamic shader data associated with a node.

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
class SKAttributeValue
```

```objc
@interface SKAttributeValue : NSObject
```

#### Overview

SpriteKit nodes that are rendered with a custom shader can use [`SKAttributeValue`](./skattributevalue.md) objects to pass dynamic values which can change without requiring that shader to be recompiled. An attribute value is passed to a shader using a node’s [`setValue(_:forAttribute:)`](./sknode/setvalue%28_,forattribute%29.md) method using the relevant attribute’s name. For example, given a shader with a [`SKAttributeType.float`](./skattributetype/float.md) attribute named `a_radius`:

Listing 1. Creating an attribute

```objc
let attribute = SKAttribute(name: "a_radius", 
                            type: SKAttributeType.float)
```

The following code sets the value of this attribute to `10` and passes it to a [`SKSpriteNode`](./skspritenode.md) object’s shader:

Listing 2. Setting an attribute value

```objc
node.setValue(SKAttributeValue(float: 10), 
              forAttribute: "a_radius")
```

The attribute, `a_radius`, is available as a global floating-point variable within the shader code.

Using this technique, a single shader can be shared across many nodes and each nodes can supply its own attributes. This approach is an alternative to using [`SKUniform`](./skuniform.md) objects which would require a recompilation for each distinct set of parameters.

## Topics

### Initializers
- [init()](./skattributevalue/init%28%29.md)
  Creates and initializes a new attribute value object
- [convenience init(float: Float)](./skattributevalue/init%28float%29.md)
  Creates and initializes a new attribute value object that holds a floating point number.
- [convenience init(vectorFloat2: vector_float2)](./skattributevalue/init%28vectorfloat2%29.md)
  Creates and initializes a new attribute value object that holds a vector of two floating point numbers.
- [convenience init(vectorFloat3: vector_float3)](./skattributevalue/init%28vectorfloat3%29.md)
  Creates and initializes a new attribute value object that holds a vector of three floating point numbers.
- [convenience init(vectorFloat4: vector_float4)](./skattributevalue/init%28vectorfloat4%29.md)
  Creates and initializes a new attribute value object that holds a vector of four floating point numbers.
- [init?(coder: NSCoder)](./skattributevalue/init%28coder%29.md)
### Instance Properties
- [var floatValue: Float](./skattributevalue/floatvalue.md)
  The receiver’s floating point value.
- [var vectorFloat2Value: vector_float2](./skattributevalue/vectorfloat2value.md)
  The receiver’s value as a vector of two floating-point numbers.
- [var vectorFloat3Value: vector_float3](./skattributevalue/vectorfloat3value.md)
  The receiver’s value as a vector of three floating point numbers.
- [var vectorFloat4Value: vector_float4](./skattributevalue/vectorfloat4value.md)
  The receiver’s value as a vector of four floating point numbers.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Shaders
- [class SKShader](./skshader.md)
  An object that allows you to apply a custom fragment shader.
- [class SKAttribute](./skattribute.md)
  A specification for dynamic per-node data used with a custom shader.
- [class SKUniform](./skuniform.md)
  A container for uniform shader data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skattributevalue)*