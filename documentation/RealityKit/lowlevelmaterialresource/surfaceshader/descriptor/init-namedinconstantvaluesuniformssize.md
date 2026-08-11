# init(named:in:constantValues:uniformsSize:)

**Framework**: RealityKit  
**Kind**: init

Creates a descriptor for a surface shader that accepts a custom uniforms argument buffer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(named name: String, in library: any MTLLibrary, constantValues: MTLFunctionConstantValues = .init(), uniformsSize: Int)
```

#### Discussion

Use this initializer when your Metal surface shader function reads per-draw parameters through a custom uniforms argument buffer, using the same mechanism as [`CustomMaterial/withMutableUniforms(ofType:stage:_:)`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/custommaterial/withmutableuniforms(oftype:stage:_:)). The function must be `[[stitchable]]` and declare the uniforms as a second `constant T &customParams` parameter:

```cpp
[[stitchable]]
void mySurfaceShader(realitykit::surface_parameters params,
                     constant MyUniforms &customParams) { ... }
```

The renderer sizes the uniforms buffer to `uniformsSize` bytes and configures the argument table automatically.

## Parameters

- `name`: The name of the Metal function in the library.
- `library`: The Metal library that contains the function.
- `constantValues`: The Metal function constant values to specialize the function with. The function descriptor takes a snapshot of the constant values passed in.
- `uniformsSize`: The size of the custom uniforms buffer, in bytes.

## See Also

- [init(named: String, in: any MTLLibrary, constantValues: MTLFunctionConstantValues)](lowlevelmaterialresource/surfaceshader/descriptor/init(named:in:constantvalues:).md)
  Creates a descriptor referencing the named function in the given library, with the provided function constant values.
- [init<UniformsType>(named: String, in: any MTLLibrary, constantValues: MTLFunctionConstantValues, uniformsType: UniformsType.Type)](lowlevelmaterialresource/surfaceshader/descriptor/init(named:in:constantvalues:uniformstype:).md)
  Creates a descriptor for a surface shader that accepts a custom uniforms argument buffer, deriving the buffer size from `uniformsType`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialresource/surfaceshader/descriptor/init(named:in:constantvalues:uniformssize:))*