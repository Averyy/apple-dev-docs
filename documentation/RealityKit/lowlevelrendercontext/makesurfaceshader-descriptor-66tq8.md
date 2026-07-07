# makeSurfaceShader(descriptor:)

**Framework**: RealityKit  
**Kind**: method  
**Required**: Yes

Synchronous variant of [`makeSurfaceShader(descriptor:)`](lowlevelrendercontext/makesurfaceshader(descriptor:)-66tq8.md). Blocks the current thread until compilation completes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func makeSurfaceShader(descriptor: LowLevelMaterialResource.SurfaceShader.Descriptor) throws -> sending LowLevelMaterialResource.SurfaceShader
```

## See Also

- [func makeSurfaceShader(descriptor: LowLevelMaterialResource.SurfaceShader.Descriptor) async throws -> sending LowLevelMaterialResource.SurfaceShader](lowlevelrendercontext/makesurfaceshader(descriptor:)-9kdy6.md)
  Asynchronously creates a custom surface shader from a user-authored Metal function descriptor.
- [func makeSimpleSurfaceShader(descriptor: LowLevelMaterialResource.SimpleSurfaceDescriptor) throws -> sending LowLevelMaterialResource.SurfaceShader](lowlevelrendercontext/makesimplesurfaceshader(descriptor:)-74vhb.md)
  Synchronous variant of [`makeSimpleSurfaceShader(descriptor:)`](lowlevelrendercontext/makesimplesurfaceshader(descriptor:)-74vhb.md). Blocks the current thread until compilation completes.
- [func makeSimpleSurfaceShader(descriptor: LowLevelMaterialResource.SimpleSurfaceDescriptor) async throws -> sending LowLevelMaterialResource.SurfaceShader](lowlevelrendercontext/makesimplesurfaceshader(descriptor:)-14ppx.md)
  Asynchronously creates a simple surface shader using a built-in tint color or texture implementation, as described by the given descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontext/makesurfaceshader(descriptor:)-66tq8)*