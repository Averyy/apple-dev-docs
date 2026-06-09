# makeMaterialResource(descriptor:)

**Framework**: RealityKit  
**Kind**: method  
**Required**: Yes

Asynchronously compiles a material resource from a geometry modifier, surface shader, and lighting function.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
(nonsending) func makeMaterialResource(descriptor: LowLevelMaterialResource.Descriptor) async throws -> sending LowLevelMaterialResource
```

#### Return Value

A newly compiled [`LowLevelMaterialResource`](lowlevelmaterialresource.md).

#### Discussion

> **Note**: An error if shader compilation fails.

## Parameters

- `descriptor`: The geometry modifier, surface shader, and lighting function to compile into a material.

## See Also

- [func makeBufferResource(descriptor: LowLevelBufferResource.Descriptor) throws -> LowLevelBufferResource](lowlevelrendercontext/makebufferresource(descriptor:).md)
  Creates a GPU-managed buffer resource from the given descriptor.
- [func makeTextureResource(descriptor: LowLevelTextureResource.Descriptor) throws -> LowLevelTextureResource](lowlevelrendercontext/maketextureresource(descriptor:).md)
  Creates a texture resource from the given descriptor.
- [func makeMaterialResource(descriptor: LowLevelMaterialResource.Descriptor) throws -> sending LowLevelMaterialResource](lowlevelrendercontext/makematerialresource(descriptor:)-8hizx.md)
  Synchronous variant of [`makeMaterialResource(descriptor:)`](lowlevelrendercontext/makematerialresource(descriptor:)-8hizx.md). Blocks the current thread until compilation completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontext/makematerialresource(descriptor:)-9nufj)*