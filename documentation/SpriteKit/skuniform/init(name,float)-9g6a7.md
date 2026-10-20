# init(name:float:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Creates and initializes a new uniform object that holds a vector of three floating-point numbers.

**Availability**:
- iOS 7.0+ - Deprecated in 10.0
- iPadOS 7.0+ - Deprecated in 10.0
- macOS 10.8+ - Deprecated in 10.12
- tvOS - Deprecated in 10.0

## Declaration

```swift
init(name: String, float value: GLKVector3)
```

```objc
- (instancetype) initWithName:(NSString *) name floatVector3:(GLKVector3) value;
```

#### Return Value

An initialized uniform object whose type is set to [`SKUniformType.floatVector3`](../skuniformtype/floatvector3.md).

## Parameters

- `name`: The name used to identify the uniform variable; you use this name inside your shader to read the uniform variable’s value.
- `value`: The initial vector for the uniform variable.

## See Also

### Creating and Initializing Uniform Objects
- [init(name: String)](./init%28name%29.md)
  Initializes a new uniform object.
- [init(name: String, float: Float)](./init%28name,float%29-48rln.md)
  Initializes a new uniform object that holds a floating-point number.
- [init(name: String, float: GLKVector2)](./init%28name,float%29-9g5vj.md)
  Initializes a new uniform object that holds a vector of two floating-point numbers.
- [init(name: String, float: GLKVector4)](./init%28name,float%29-9g7j7.md)
  Initializes a new uniform object that holds a vector of four floating-point numbers.
- [init(name: String, float: GLKMatrix2)](./init%28name,float%29-6110m.md)
  Initializes a new uniform object that holds a `2 x 2` matrix of floating-point numbers.
- [init(name: String, float: GLKMatrix3)](./init%28name,float%29-611hs.md)
  Initializes a new uniform object that holds a `3 x 3` matrix of floating-point numbers.
- [init(name: String, float: GLKMatrix4)](./init%28name,float%29-60zbm.md)
  Initializes a new uniform object that holds a `4 x 4` matrix of floating-point numbers.
- [init(name: String, texture: SKTexture?)](./init%28name,texture%29.md)
  Initializes a new uniform object that holds a reference to a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skuniform/init(name:float:)-9g6a7)*