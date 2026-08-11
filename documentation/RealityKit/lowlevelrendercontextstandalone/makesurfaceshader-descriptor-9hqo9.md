# makeSurfaceShader(descriptor:)

**Framework**: RealityKit  
**Kind**: method

Asynchronously creates a custom surface shader from a user-authored Metal function descriptor.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
(nonsending) final func makeSurfaceShader(descriptor: LowLevelMaterialResource.SurfaceShader.Descriptor) async throws -> sending LowLevelMaterialResource.SurfaceShader
```

#### Return Value

A compiled [`LowLevelMaterialResource.SurfaceShader`](lowlevelmaterialresource/surfaceshader.md).

#### Discussion

> **Note**: An error if the specified Metal function cannot be found or compiled.

## Parameters

- `descriptor`: The Metal function name, library, and optional constant values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextstandalone/makesurfaceshader(descriptor:)-9hqo9)*