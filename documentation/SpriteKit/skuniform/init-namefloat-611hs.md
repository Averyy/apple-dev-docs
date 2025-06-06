# init(name:float:)

**Framework**: SpriteKit  
**Kind**: init

Initializes a new uniform object that holds a `3 x 3` matrix of floating-point numbers.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- macOS 10.8+
- tvOS ?+

## Declaration

```swift
init(name: String, float value: GLKMatrix3)
```

#### Return Value

An initialized uniform object whose type is set to [`SKUniformType.floatMatrix3`](skuniformtype/floatmatrix3.md).

## Parameters

- `name`: The name used to identify the uniform variable; you use this name inside your shader to read the uniform variable’s value.
- `value`: The initial matrix for the uniform variable.

## See Also

- [init(name: String)](skuniform/init(name:).md)
  Initializes a new uniform object.
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
- [init(name: String, float: GLKMatrix4)](skuniform/init(name:float:)-60zbm.md)
  Initializes a new uniform object that holds a `4 x 4` matrix of floating-point numbers.
- [init(name: String, texture: SKTexture?)](skuniform/init(name:texture:).md)
  Initializes a new uniform object that holds a reference to a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skuniform/init(name:float:)-611hs)*