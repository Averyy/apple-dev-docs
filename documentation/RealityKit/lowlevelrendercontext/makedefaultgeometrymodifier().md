# makeDefaultGeometryModifier()

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a pass-through geometry modifier that performs no vertex transformation.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func makeDefaultGeometryModifier() -> sending LowLevelMaterialResource.GeometryModifier
```

## Return Value

A pass-through [`LowLevelMaterialResource.GeometryModifier`](../lowlevelmaterialresource/geometrymodifier.md).

## See Also

### Creating geometry modifiers
- [func makeGeometryModifier(descriptor: LowLevelMaterialResource.GeometryModifier.Descriptor) throws -> sending LowLevelMaterialResource.GeometryModifier](./makegeometrymodifier%28descriptor%29-307ec.md)
  Synchronous variant of [`makeGeometryModifier(descriptor:)`](./makegeometrymodifier%28descriptor%29-307ec.md). Blocks the current thread until compilation completes.
- [func makeGeometryModifier(descriptor: LowLevelMaterialResource.GeometryModifier.Descriptor) async throws -> sending LowLevelMaterialResource.GeometryModifier](./makegeometrymodifier%28descriptor%29-9tq7q.md)
  Asynchronously creates a geometry modifier from a user-authored Metal function described by the given descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontext/makedefaultgeometrymodifier())*