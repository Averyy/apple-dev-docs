# LowLevelMaterialResource.GeometryModifier.Descriptor

**Framework**: RealityKit  
**Kind**: struct

The name and library for a user-authored Metal geometry modifier function.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Descriptor
```

## Topics

### Creating a descriptor
- [init(named: String, in: any MTLLibrary, constantValues: MTLFunctionConstantValues)](lowlevelmaterialresource/geometrymodifier/descriptor/init(named:in:constantvalues:).md)
  Creates a descriptor referencing the named function in the given library, with the provided function constant values.
- [init(named: String, in: any MTLLibrary, constantValues: MTLFunctionConstantValues, uniformsSize: Int)](lowlevelmaterialresource/geometrymodifier/descriptor/init(named:in:constantvalues:uniformssize:).md)
  Creates a descriptor for a geometry modifier that accepts a custom uniforms argument buffer.
- [init<UniformsType>(named: String, in: any MTLLibrary, constantValues: MTLFunctionConstantValues, uniformsType: UniformsType.Type)](lowlevelmaterialresource/geometrymodifier/descriptor/init(named:in:constantvalues:uniformstype:).md)
  Creates a descriptor for a geometry modifier that accepts a custom uniforms argument buffer, deriving the buffer size from `uniformsType`.
### Inspecting the configuration
- [var library: any MTLLibrary](lowlevelmaterialresource/geometrymodifier/descriptor/library.md)
  The Metal library that contains the function.
- [var constantValues: MTLFunctionConstantValues](lowlevelmaterialresource/geometrymodifier/descriptor/constantvalues.md)
  The constant values to use when creating the function. These correspond to constants defined in your metal code.
### Initializers
- [init(named: String, in: any MTLLibrary)](lowlevelmaterialresource/geometrymodifier/descriptor/init(named:in:).md)
  Creates a descriptor referencing the named function in the given library.
### Instance Properties
- [var name: String](lowlevelmaterialresource/geometrymodifier/descriptor/name.md)
  The name of the Metal function in the library.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialresource/geometrymodifier/descriptor)*