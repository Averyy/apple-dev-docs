# init(name:type:)

**Framework**: SpriteKit  
**Kind**: init

Creates and initializes a new attribute object of a specified type with a name that can be referenced within the shader.

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
init(name: String, type: SKAttributeType)
```

#### Return Value

A new attribute object.

#### Discussion

Attribute names are typically named with a preceding “a” and an underscore. The following code shows how to initialize an attribute named `a_frequency` which is of type [`SKAttributeType.float`](skattributetype/float.md).

```swift
let attribute = SKAttribute(name: "a_frequency", 
                            type: SKAttributeType.float)
```

## Parameters

- `name`: The name of the attribute.
- `type`: The type of the attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skattribute/init(name:type:))*