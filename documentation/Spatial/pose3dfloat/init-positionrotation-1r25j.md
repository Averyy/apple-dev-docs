# init(position:rotation:)

**Framework**: Spatial  
**Kind**: init

Creates a pose from double-precision simd primitives that describe the position and rotation.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init(position: simd_float3 = .zero, rotation: simd_quatf)
```

## Parameters

- `position`: The position of the pose.
- `rotation`: The rotation of the pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/pose3dfloat/init(position:rotation:)-1r25j)*