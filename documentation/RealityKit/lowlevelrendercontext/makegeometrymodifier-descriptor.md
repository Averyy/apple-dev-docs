# makeGeometryModifier(descriptor:)

**Framework**: RealityKit  
**Kind**: method  
**Required**: Yes

Synchronous variant of [`makeGeometryModifier(descriptor:)`](lowlevelrendercontext/makegeometrymodifier(descriptor:).md). Blocks the current thread until compilation completes.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func makeGeometryModifier(descriptor: LowLevelMaterialResource.GeometryModifier.Descriptor) throws -> sending LowLevelMaterialResource.GeometryModifier
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontext/makegeometrymodifier(descriptor:))*