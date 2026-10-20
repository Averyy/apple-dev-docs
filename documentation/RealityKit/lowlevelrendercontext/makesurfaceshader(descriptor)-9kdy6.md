# makeSurfaceShader(descriptor:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asynchronously creates a custom surface shader from a user-authored Metal function descriptor.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
nonisolated
(nonsending) func makeSurfaceShader(descriptor: LowLevelMaterialResource.SurfaceShader.Descriptor) async throws -> sending LowLevelMaterialResource.SurfaceShader
```

**Other overloads**:

```swift
func makeSurfaceShader(descriptor: LowLevelMaterialResource.SurfaceShader.Descriptor) throws -> sending LowLevelMaterialResource.SurfaceShader
```

#### Return Value

A compiled [`LowLevelMaterialResource.SurfaceShader`](../lowlevelmaterialresource/surfaceshader.md).

#### Discussion

> **Throws**: An error if the specified Metal function cannot be found or compiled.

## Parameters

- `descriptor`: The Metal function name, library, and optional constant values.

## See Also

### Creating surface shaders
- [func makeSurfaceShader(descriptor: LowLevelMaterialResource.SurfaceShader.Descriptor) throws -> sending LowLevelMaterialResource.SurfaceShader](./makesurfaceshader%28descriptor%29-66tq8.md)
  Synchronous variant of [`makeSurfaceShader(descriptor:)`](./makesurfaceshader%28descriptor%29-66tq8.md). Blocks the current thread until compilation completes.
- [func makeSimpleSurfaceShader(descriptor: LowLevelMaterialResource.SimpleSurfaceDescriptor) throws -> sending LowLevelMaterialResource.SurfaceShader](./makesimplesurfaceshader%28descriptor%29-74vhb.md)
  Synchronous variant of [`makeSimpleSurfaceShader(descriptor:)`](./makesimplesurfaceshader%28descriptor%29-74vhb.md). Blocks the current thread until compilation completes.
- [func makeSimpleSurfaceShader(descriptor: LowLevelMaterialResource.SimpleSurfaceDescriptor) async throws -> sending LowLevelMaterialResource.SurfaceShader](./makesimplesurfaceshader%28descriptor%29-14ppx.md)
  Asynchronously creates a simple surface shader using a built-in tint color or texture implementation, as described by the given descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontext/makesurfaceshader(descriptor:)-9kdy6)*