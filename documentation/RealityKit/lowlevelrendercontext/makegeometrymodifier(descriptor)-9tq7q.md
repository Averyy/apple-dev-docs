# makeGeometryModifier(descriptor:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asynchronously creates a geometry modifier from a user-authored Metal function described by the given descriptor.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
nonisolated(nonsending)
func makeGeometryModifier(descriptor: LowLevelMaterialResource.GeometryModifier.Descriptor) async throws -> sending LowLevelMaterialResource.GeometryModifier
```

**Other overloads**:

```swift
func makeGeometryModifier(descriptor: LowLevelMaterialResource.GeometryModifier.Descriptor) throws -> sending LowLevelMaterialResource.GeometryModifier
```

## Return Value

A compiled [`LowLevelMaterialResource.GeometryModifier`](../lowlevelmaterialresource/geometrymodifier.md).

## Discussion

> **Throws**: An error if the specified Metal function cannot be found or compiled.

## Parameters

- `descriptor`: The Metal function name, library, and optional constant values.

## See Also

### Creating geometry modifiers
- [func makeGeometryModifier(descriptor: LowLevelMaterialResource.GeometryModifier.Descriptor) throws -> sending LowLevelMaterialResource.GeometryModifier](./makegeometrymodifier%28descriptor%29-307ec.md)
  Synchronous variant of [`makeGeometryModifier(descriptor:)`](./makegeometrymodifier%28descriptor%29-307ec.md). Blocks the current thread until compilation completes.
- [func makeDefaultGeometryModifier() -> sending LowLevelMaterialResource.GeometryModifier](./makedefaultgeometrymodifier%28%29.md)
  Returns a pass-through geometry modifier that performs no vertex transformation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontext/makegeometrymodifier(descriptor:)-9tq7q)*