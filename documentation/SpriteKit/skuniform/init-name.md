# init(name:)

**Framework**: SpriteKit  
**Kind**: init

Initializes a new uniform object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(name: String)
```

#### Return Value

An initialized uniform object.

#### Discussion

A uniform initialized with this method has no initial type and cannot be used in a shader until it is given an initial value. To set the initial value, use one of the properties defined in [`SKUniform`](skuniform.md). After its value is set, its [`uniformType`](skuniform/uniformtype.md) property is set to match the uniform’s new type. Once set, the type may not be changed.

## Parameters

- `name`: The name used to identify the uniform variable; you use this name inside your shader to read the uniform variable’s value.

## See Also

- [init(name: String, float: Float)](skuniform/init(name:float:)-48rln.md)
  Initializes a new uniform object that holds a floating-point number.
- [init(name: String, float: GLKVector2)](skuniform/init(name:float:)-9g5vj.md)
  Initializes a new uniform object that holds a vector of two floating-point numbers.
- [init(name: String, float: GLKVector3)](skuniform/init(name:float:)-9g6a7.md)
  Creates and initializes a new uniform object that holds a vector of three floating-point numbers.
- [init(name: String, float: GLKVector4)](skuniform/init(name:float:)-9g7j7.md)
  Initializes a new uniform object that holds a vector of four floating-point numbers.
- [init(name: String, float: GLKMatrix2)](skuniform/init(name:float:)-6110m.md)
  Initializes a new uniform object that holds a `2 x 2` matrix of floating-point numbers.
- [init(name: String, float: GLKMatrix3)](skuniform/init(name:float:)-611hs.md)
  Initializes a new uniform object that holds a `3 x 3` matrix of floating-point numbers.
- [init(name: String, float: GLKMatrix4)](skuniform/init(name:float:)-60zbm.md)
  Initializes a new uniform object that holds a `4 x 4` matrix of floating-point numbers.
- [init(name: String, texture: SKTexture?)](skuniform/init(name:texture:).md)
  Initializes a new uniform object that holds a reference to a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skuniform/init(name:))*