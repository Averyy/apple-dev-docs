# uniformWithName:float:

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Creates and initializes a new uniform object that holds a floating-point number.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (instancetype) uniformWithName:(NSString *) name float:(float) value;
```

#### Return Value

A newly initialized uniform object whose type is set to [`SKUniformType.float`](../skuniformtype/float.md).

## Parameters

- `name`: The name used to identify the uniform variable; you use this name inside your shader to read the uniform variable’s value.
- `value`: The initial floating-point value for the uniform variable.

## See Also

### Creating and Initializing Uniform Objects
- [+ uniformWithName:](./uniformwithname_.md)
  Creates and initializes a new uniform object.
- [+ uniformWithName:floatVector2:](./uniformwithname_floatvector2_.md)
  Creates and initializes a new uniform object that holds a vector of two floating-point numbers.
- [+ uniformWithName:floatVector3:](./uniformwithname_floatvector3_.md)
  Creates and initializes a new uniform object that holds a vector of three floating-point numbers.
- [+ uniformWithName:floatVector4:](./uniformwithname_floatvector4_.md)
  Creates and initializes a new uniform object that holds a vector of four floating-point numbers.
- [+ uniformWithName:floatMatrix2:](./uniformwithname_floatmatrix2_.md)
  Creates and initializes a new uniform object that holds a `2 x 2` matrix of floating-point numbers.
- [+ uniformWithName:floatMatrix3:](./uniformwithname_floatmatrix3_.md)
  Creates and initializes a new uniform object that holds a `3 x 3` matrix of floating-point numbers.
- [+ uniformWithName:floatMatrix4:](./uniformwithname_floatmatrix4_.md)
  Creates and initializes a new uniform object that holds a `4 x 4` matrix of floating-point numbers.
- [+ uniformWithName:texture:](./uniformwithname_texture_.md)
  Creates and initializes a new uniform object that holds a reference to a texture.
- [init(name: String)](./init%28name%29.md)
  Initializes a new uniform object.
- [init(name: String, float: Float)](./init%28name,float%29-48rln.md)
  Initializes a new uniform object that holds a floating-point number.
- [init(name: String, float: GLKVector2)](./init%28name,float%29-9g5vj.md)
  Initializes a new uniform object that holds a vector of two floating-point numbers.
- [init(name: String, float: GLKVector3)](./init%28name,float%29-9g6a7.md)
  Creates and initializes a new uniform object that holds a vector of three floating-point numbers.
- [init(name: String, float: GLKVector4)](./init%28name,float%29-9g7j7.md)
  Initializes a new uniform object that holds a vector of four floating-point numbers.
- [init(name: String, float: GLKMatrix2)](./init%28name,float%29-6110m.md)
  Initializes a new uniform object that holds a `2 x 2` matrix of floating-point numbers.
- [init(name: String, float: GLKMatrix3)](./init%28name,float%29-611hs.md)
  Initializes a new uniform object that holds a `3 x 3` matrix of floating-point numbers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skuniform/uniformwithname:float:)*