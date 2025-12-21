# init(origin:direction:)

**Framework**: Spatial  
**Kind**: init

Creates a ray from single-precision simd vectors that describe the origin and direction.

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
init(origin: simd_float3 = .zero, direction: simd_float3)
```

#### Discussion

> **Note**: This function normalizes the direction vector.

## Parameters

- `origin`: The origin of the ray.
- `direction`: Direction of the rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/ray3dfloat/init(origin:direction:)-6g59d)*