# init(center:size:)

**Framework**: Spatial  
**Kind**: init

Creates a rectangle from single-precision vectors that describe the center and size.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
init(center: simd_double3 = .zero, size: simd_double3)
```

#### Discussion

> **Note**: This function is provided as a convenience. All Spatial storage and calculations are single-precision.

## Parameters

- `center`: The center of the rectangle.
- `size`: The size of the rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rect3dfloat/init(center:size:)-1gsbj)*