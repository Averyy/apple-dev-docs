# makeSurfaceShader(descriptor:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Synchronous variant of [`makeSurfaceShader(descriptor:)`](./makesurfaceshader%28descriptor%29-66tq8.md). Blocks the current thread until compilation completes.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func makeSurfaceShader(descriptor: LowLevelMaterialResource.SurfaceShader.Descriptor) throws -> sending LowLevelMaterialResource.SurfaceShader
```

**Other overloads**:

```swift
nonisolated
(nonsending) func makeSurfaceShader(descriptor: LowLevelMaterialResource.SurfaceShader.Descriptor) async throws -> sending LowLevelMaterialResource.SurfaceShader
```

## See Also

### Creating surface shaders
- [func makeSurfaceShader(descriptor: LowLevelMaterialResource.SurfaceShader.Descriptor) async throws -> sending LowLevelMaterialResource.SurfaceShader](./makesurfaceshader%28descriptor%29-9kdy6.md)
  Asynchronously creates a custom surface shader from a user-authored Metal function descriptor.
- [func makeSimpleSurfaceShader(descriptor: LowLevelMaterialResource.SimpleSurfaceDescriptor) throws -> sending LowLevelMaterialResource.SurfaceShader](./makesimplesurfaceshader%28descriptor%29-74vhb.md)
  Synchronous variant of [`makeSimpleSurfaceShader(descriptor:)`](./makesimplesurfaceshader%28descriptor%29-74vhb.md). Blocks the current thread until compilation completes.
- [func makeSimpleSurfaceShader(descriptor: LowLevelMaterialResource.SimpleSurfaceDescriptor) async throws -> sending LowLevelMaterialResource.SurfaceShader](./makesimplesurfaceshader%28descriptor%29-14ppx.md)
  Asynchronously creates a simple surface shader using a built-in tint color or texture implementation, as described by the given descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontext/makesurfaceshader(descriptor:)-66tq8)*