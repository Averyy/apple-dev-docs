# init(named:in:constantValues:)

**Framework**: RealityKit  
**Kind**: init

Creates a descriptor referencing the named function in the given library, with the provided function constant values.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(named name: String, in library: any MTLLibrary, constantValues: MTLFunctionConstantValues)
```

## Parameters

- `name`: The name of the Metal function in the library.
- `library`: The Metal library that contains the function.
- `constantValues`: The Metal function constant values to specialize the function with.

## See Also

- [init(named: String, in: any MTLLibrary, constantValues: MTLFunctionConstantValues, uniformsSize: Int)](lowlevelmaterialresource/surfaceshader/descriptor/init(named:in:constantvalues:uniformssize:).md)
  Creates a descriptor for a surface shader that accepts a custom uniforms argument buffer.
- [init<UniformsType>(named: String, in: any MTLLibrary, constantValues: MTLFunctionConstantValues, uniformsType: UniformsType.Type)](lowlevelmaterialresource/surfaceshader/descriptor/init(named:in:constantvalues:uniformstype:).md)
  Creates a descriptor for a surface shader that accepts a custom uniforms argument buffer, deriving the buffer size from `uniformsType`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialresource/surfaceshader/descriptor/init(named:in:constantvalues:))*