# ReverbMeshResource

**Framework**: RealityKit  
**Kind**: class

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class ReverbMeshResource
```

## Topics

### Creating standard room shapes
- [static func shoebox(size: SIMD3<Float>) -> Self](reverbmeshresource/shoebox(size:).md)
- [static func box(size: SIMD3<Float>) -> Self](reverbmeshresource/box(size:).md)
- [static func plane(width: Float, depth: Float) -> Self](reverbmeshresource/plane(width:depth:).md)
### Creating a custom mesh
- [convenience init(positions: [SIMD3<Float>], triangleIndices: [UInt32], materials: [UInt32]) throws](reverbmeshresource/init(positions:triangleindices:materials:).md)
### Initializers
- [convenience(from:)](reverbmeshresource/init(from:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Resource](resource.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class AudioPlaybackGroupController](audioplaybackgroupcontroller.md)
  A controller that manages synchronized playback for a group of audio resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/reverbmeshresource)*