# LowLevelMaterialResource.GeometryModifier.Descriptor

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

The name and library for a user-authored Metal geometry modifier function.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Descriptor
```

## Topics

### Creating a descriptor
- [init(named: String, in: any MTLLibrary, constantValues: MTLFunctionConstantValues)](./descriptor/init%28named,in,constantvalues%29.md)
  Creates a descriptor referencing the named function in the given library, with the provided function constant values.
- [init(named: String, in: any MTLLibrary, constantValues: MTLFunctionConstantValues, uniformsSize: Int)](./descriptor/init%28named,in,constantvalues,uniformssize%29.md)
  Creates a descriptor for a geometry modifier that accepts a custom uniforms argument buffer.
- [init<UniformsType>(named: String, in: any MTLLibrary, constantValues: MTLFunctionConstantValues, uniformsType: UniformsType.Type)](./descriptor/init%28named,in,constantvalues,uniformstype%29.md)
  Creates a descriptor for a geometry modifier that accepts a custom uniforms argument buffer, deriving the buffer size from `uniformsType`.
### Inspecting the configuration
- [var library: any MTLLibrary](./descriptor/library.md)
  The Metal library that contains the function.
- [var constantValues: MTLFunctionConstantValues](./descriptor/constantvalues.md)
  The constant values to use when creating the function. These correspond to constants defined in your Metal code.
### Initializers
- [init(named: String, in: any MTLLibrary)](./descriptor/init%28named,in%29.md)
  Creates a descriptor referencing the named function in the given library.
### Instance Properties
- [var name: String](./descriptor/name.md)
  The name of the Metal function in the library.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialresource/geometrymodifier/descriptor)*