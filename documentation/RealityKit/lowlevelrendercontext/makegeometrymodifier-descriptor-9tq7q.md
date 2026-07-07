# makeGeometryModifier(descriptor:)

**Framework**: RealityKit  
**Kind**: method  
**Required**: Yes

Asynchronously creates a geometry modifier from a user-authored Metal function described by the given descriptor.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
(nonsending) func makeGeometryModifier(descriptor: LowLevelMaterialResource.GeometryModifier.Descriptor) async throws -> sending LowLevelMaterialResource.GeometryModifier
```

#### Return Value

A compiled [`LowLevelMaterialResource.GeometryModifier`](lowlevelmaterialresource/geometrymodifier.md).

#### Discussion

> **Note**: An error if the specified Metal function cannot be found or compiled.

## Parameters

- `descriptor`: The Metal function name, library, and optional constant values.

## See Also

- [func makeGeometryModifier(descriptor: LowLevelMaterialResource.GeometryModifier.Descriptor) throws -> sending LowLevelMaterialResource.GeometryModifier](lowlevelrendercontext/makegeometrymodifier(descriptor:)-307ec.md)
  Synchronous variant of [`makeGeometryModifier(descriptor:)`](lowlevelrendercontext/makegeometrymodifier(descriptor:)-307ec.md). Blocks the current thread until compilation completes.
- [func makeDefaultGeometryModifier() -> sending LowLevelMaterialResource.GeometryModifier](lowlevelrendercontext/makedefaultgeometrymodifier.md)
  Returns a pass-through geometry modifier that performs no vertex transformation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontext/makegeometrymodifier(descriptor:)-9tq7q)*