# SKUniform

**Framework**: SpriteKit  
**Kind**: class

A container for uniform shader data.

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
class SKUniform
```

## Mentions

- [Creating a Custom Fragment Shader](creating-a-custom-fragment-shader.md)

#### Overview

An [`SKUniform`](skuniform.md) object is used to hold uniform data for a custom OpenGL or OpenGL ES shader. The uniform data is accessible from all shaders that include the uniform.To use a uniform variable in your shader, create the [`SKUniform`](skuniform.md) object and set its initial value. Once its value is specified, the [`uniformType`](skuniform/uniformtype.md) property changes to match the type of the initial value you provided and can never change afterward. To use the uniform object, add it to an [`SKShader`](skshader.md) object that needs to access the uniform variable. To update the uniform variable’s value, choose the appropriate property on the uniform object based on the data type it encapsulates.

## Topics

### Creating and Initializing Uniform Objects
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
- [init(name: String, float: GLKMatrix3)](skuniform/init(name:float:)-611hs.md)
  Initializes a new uniform object that holds a `3 x 3` matrix of floating-point numbers.
- [init(name: String, float: GLKMatrix4)](skuniform/init(name:float:)-60zbm.md)
  Initializes a new uniform object that holds a `4 x 4` matrix of floating-point numbers.
- [init(name: String, texture: SKTexture?)](skuniform/init(name:texture:).md)
  Initializes a new uniform object that holds a reference to a texture.
### Reading Information About a Uniform
- [var name: String](skuniform/name.md)
  The uniform’s name.
- [var uniformType: SKUniformType](skuniform/uniformtype.md)
  The uniform object’s data type.
### Reading and Writing an Uniform Object’s Value
- [var floatValue: Float](skuniform/floatvalue.md)
  The receiver’s value as a floating-point value.
- [var floatVector2Value: GLKVector2](skuniform/floatvector2value.md)
  The receiver’s value as a vector of two floating-point values.
- [var floatVector3Value: GLKVector3](skuniform/floatvector3value.md)
  The receiver’s value as a vector of three floating-point values.
- [var floatVector4Value: GLKVector4](skuniform/floatvector4value.md)
  The receiver’s value as a vector of four floating-point values.
- [var floatMatrix2Value: GLKMatrix2](skuniform/floatmatrix2value.md)
  The receiver’s value as a `2 x 2` matrix of floating-point values.
- [var floatMatrix3Value: GLKMatrix3](skuniform/floatmatrix3value.md)
  The receiver’s value as a `3 x 3` matrix of floating-point values.
- [var floatMatrix4Value: GLKMatrix4](skuniform/floatmatrix4value.md)
  The receiver’s value as a `4 x 4` matrix of floating-point values.
- [var textureValue: SKTexture?](skuniform/texturevalue.md)
  The receiver’s value as a SpriteKit texture.
### Constants
- [enum SKUniformType](skuniformtype.md)
  An enumerated type to identify the type of a uniform object.
### Initializers
- [init(name: String, matrixFloat2x2: matrix_float2x2)](skuniform/init(name:matrixfloat2x2:).md)
- [init(name: String, matrixFloat3x3: matrix_float3x3)](skuniform/init(name:matrixfloat3x3:).md)
- [init(name: String, matrixFloat4x4: matrix_float4x4)](skuniform/init(name:matrixfloat4x4:).md)
- [init(name: String, vectorFloat2: vector_float2)](skuniform/init(name:vectorfloat2:).md)
- [init(name: String, vectorFloat3: vector_float3)](skuniform/init(name:vectorfloat3:).md)
- [init(name: String, vectorFloat4: vector_float4)](skuniform/init(name:vectorfloat4:).md)
### Instance Properties
- [var matrixFloat2x2Value: matrix_float2x2](skuniform/matrixfloat2x2value.md)
- [var matrixFloat3x3Value: matrix_float3x3](skuniform/matrixfloat3x3value.md)
- [var matrixFloat4x4Value: matrix_float4x4](skuniform/matrixfloat4x4value.md)
- [var vectorFloat2Value: vector_float2](skuniform/vectorfloat2value.md)
- [var vectorFloat3Value: vector_float3](skuniform/vectorfloat3value.md)
- [var vectorFloat4Value: vector_float4](skuniform/vectorfloat4value.md)

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
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class SKShader](skshader.md)
  An object that allows you to apply a custom fragment shader.
- [class SKAttribute](skattribute.md)
  A specification for dynamic per-node data used with a custom shader.
- [class SKAttributeValue](skattributevalue.md)
  A container for dynamic shader data associated with a node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skuniform)*