# makeSimpleSurfaceShader(descriptor:)

**Framework**: RealityKit  
**Kind**: method

Asynchronously creates a simple surface shader using a built-in tint color or texture implementation, as described by the given descriptor.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
(nonsending) final func makeSimpleSurfaceShader(descriptor: LowLevelMaterialResource.SimpleSurfaceDescriptor) async throws -> sending LowLevelMaterialResource.SurfaceShader
```

#### Return Value

A compiled [`LowLevelMaterialResource.SurfaceShader`](lowlevelmaterialresource/surfaceshader.md).

#### Discussion

> **Note**: An error if shader compilation fails.

## Parameters

- `descriptor`: The combination of tint color, texture, output channel, and opacity flags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextstandalone/makesimplesurfaceshader(descriptor:)-3f0mt)*