# makeMaterialResource(descriptor:)

**Framework**: RealityKit  
**Kind**: method  
**Required**: Yes

Synchronous variant of [`makeMaterialResource(descriptor:)`](lowlevelrendercontext/makematerialresource(descriptor:)-8hizx.md). Blocks the current thread until compilation completes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func makeMaterialResource(descriptor: LowLevelMaterialResource.Descriptor) throws -> sending LowLevelMaterialResource
```

## See Also

- [func makeBufferResource(descriptor: LowLevelBufferResource.Descriptor) throws -> LowLevelBufferResource](lowlevelrendercontext/makebufferresource(descriptor:).md)
  Creates a GPU-managed buffer resource from the given descriptor.
- [func makeTextureResource(descriptor: LowLevelTextureResource.Descriptor) throws -> LowLevelTextureResource](lowlevelrendercontext/maketextureresource(descriptor:).md)
  Creates a texture resource from the given descriptor.
- [func makeMaterialResource(descriptor: LowLevelMaterialResource.Descriptor) async throws -> sending LowLevelMaterialResource](lowlevelrendercontext/makematerialresource(descriptor:)-9nufj.md)
  Asynchronously compiles a material resource from a geometry modifier, surface shader, and lighting function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontext/makematerialresource(descriptor:)-8hizx)*