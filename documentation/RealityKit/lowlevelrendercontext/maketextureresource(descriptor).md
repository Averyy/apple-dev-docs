# makeTextureResource(descriptor:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a texture resource from the given descriptor.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func makeTextureResource(descriptor: LowLevelTextureResource.Descriptor) throws -> LowLevelTextureResource
```

#### Return Value

A newly created [`LowLevelTextureResource`](../lowleveltextureresource.md).

#### Discussion

> **Throws**: An error if the descriptor is invalid or if the underlying GPU allocation fails.

## Parameters

- `descriptor`: The texture type, pixel format, dimensions, and usage flags.

## See Also

### Creating resources
- [func makeBufferResource(descriptor: LowLevelBufferResource.Descriptor) throws -> LowLevelBufferResource](./makebufferresource%28descriptor%29.md)
  Creates a GPU-managed buffer resource from the given descriptor.
- [func makeMaterialResource(descriptor: LowLevelMaterialResource.Descriptor) throws -> sending LowLevelMaterialResource](./makematerialresource%28descriptor%29-8hizx.md)
  Synchronous variant of [`makeMaterialResource(descriptor:)`](./makematerialresource%28descriptor%29-8hizx.md). Blocks the current thread until compilation completes.
- [func makeMaterialResource(descriptor: LowLevelMaterialResource.Descriptor) async throws -> sending LowLevelMaterialResource](./makematerialresource%28descriptor%29-9nufj.md)
  Asynchronously compiles a material resource from a geometry modifier, surface shader, and lighting function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontext/maketextureresource(descriptor:))*