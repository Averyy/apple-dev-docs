# makeGeometryModifier(descriptor:)

**Framework**: RealityKit  
**Kind**: method

Asynchronously creates a geometry modifier from a user-authored Metal function described by the given descriptor.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
(nonsending) final func makeGeometryModifier(descriptor: LowLevelMaterialResource.GeometryModifier.Descriptor) async throws -> sending LowLevelMaterialResource.GeometryModifier
```

#### Return Value

A compiled [`LowLevelMaterialResource.GeometryModifier`](lowlevelmaterialresource/geometrymodifier.md).

#### Discussion

> **Note**: An error if the specified Metal function cannot be found or compiled.

## Parameters

- `descriptor`: The Metal function name, library, and optional constant values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextstandalone/makegeometrymodifier(descriptor:)-4p20q)*