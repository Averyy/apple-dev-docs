# makeSimpleSurfaceShader(descriptor:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Synchronous variant of [`makeSimpleSurfaceShader(descriptor:)`](./makesimplesurfaceshader%28descriptor%29.md). Blocks the current thread until compilation completes.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func makeSimpleSurfaceShader(descriptor: LowLevelMaterialResource.SimpleSurfaceDescriptor) throws -> sending LowLevelMaterialResource.SurfaceShader
```

**Other overloads**:

```swift
nonisolated(nonsending)
func makeSimpleSurfaceShader(descriptor: LowLevelMaterialResource.SimpleSurfaceDescriptor) async throws -> sending LowLevelMaterialResource.SurfaceShader
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontext/makesimplesurfaceshader(descriptor:))*