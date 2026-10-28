# makeSurfaceShader(descriptor:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Synchronous variant of [`makeSurfaceShader(descriptor:)`](./makesurfaceshader%28descriptor%29.md). Blocks the current thread until compilation completes.

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
nonisolated(nonsending)
func makeSurfaceShader(descriptor: LowLevelMaterialResource.SurfaceShader.Descriptor) async throws -> sending LowLevelMaterialResource.SurfaceShader
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontext/makesurfaceshader(descriptor:))*