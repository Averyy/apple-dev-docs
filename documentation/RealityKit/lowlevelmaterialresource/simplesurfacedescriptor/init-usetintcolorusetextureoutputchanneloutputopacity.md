# init(useTintColor:useTexture:outputChannel:outputOpacity:)

**Framework**: RealityKit  
**Kind**: init

Creates a descriptor for the specified combination of inputs and outputs.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(useTintColor: Bool, useTexture: Bool, outputChannel: LowLevelMaterialResource.SimpleSurfaceDescriptor.OutputChannel, outputOpacity: Bool)
```

## Parameters

- `useTintColor`: If `true`, the shader reads a tint color from the argument table and multiplies it with the surface output.
- `useTexture`: If `true`, the shader samples a texture from the argument table and multiplies it with the surface output.
- `outputChannel`: The surface output channel the shader writes to.
- `outputOpacity`: If `true`, the shader also writes the computed alpha to the surface opacity output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialresource/simplesurfacedescriptor/init(usetintcolor:usetexture:outputchannel:outputopacity:))*