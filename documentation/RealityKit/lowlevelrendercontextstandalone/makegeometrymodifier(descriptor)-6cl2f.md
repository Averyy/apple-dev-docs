# makeGeometryModifier(descriptor:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Synchronous variant of [`makeGeometryModifier(descriptor:)`](./makegeometrymodifier%28descriptor%29-6cl2f.md). Blocks the current thread until compilation completes.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final func makeGeometryModifier(descriptor: LowLevelMaterialResource.GeometryModifier.Descriptor) throws -> sending LowLevelMaterialResource.GeometryModifier
```

**Other overloads**:

```swift
nonisolated(nonsending)
final func makeGeometryModifier(descriptor: LowLevelMaterialResource.GeometryModifier.Descriptor) async throws -> sending LowLevelMaterialResource.GeometryModifier
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextstandalone/makegeometrymodifier(descriptor:)-6cl2f)*