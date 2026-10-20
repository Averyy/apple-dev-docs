# makeMaterialResource(descriptor:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asynchronously compiles a material resource from a geometry modifier, surface shader, and lighting function.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
nonisolated
(nonsending) func makeMaterialResource(descriptor: LowLevelMaterialResource.Descriptor) async throws -> sending LowLevelMaterialResource
```

**Other overloads**:

```swift
func makeMaterialResource(descriptor: LowLevelMaterialResource.Descriptor) throws -> sending LowLevelMaterialResource
```

#### Return Value

A newly compiled [`LowLevelMaterialResource`](../lowlevelmaterialresource.md).

#### Discussion

> **Throws**: An error if shader compilation fails.

## Parameters

- `descriptor`: The geometry modifier, surface shader, and lighting function to compile into a material.

## See Also

### Creating resources
- [func makeBufferResource(descriptor: LowLevelBufferResource.Descriptor) throws -> LowLevelBufferResource](./makebufferresource%28descriptor%29.md)
  Creates a GPU-managed buffer resource from the given descriptor.
- [func makeTextureResource(descriptor: LowLevelTextureResource.Descriptor) throws -> LowLevelTextureResource](./maketextureresource%28descriptor%29.md)
  Creates a texture resource from the given descriptor.
- [func makeMaterialResource(descriptor: LowLevelMaterialResource.Descriptor) throws -> sending LowLevelMaterialResource](./makematerialresource%28descriptor%29-8hizx.md)
  Synchronous variant of [`makeMaterialResource(descriptor:)`](./makematerialresource%28descriptor%29-8hizx.md). Blocks the current thread until compilation completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontext/makematerialresource(descriptor:)-9nufj)*