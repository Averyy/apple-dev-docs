# init(_:)

**Framework**: Spatial  
**Kind**: init

Creates a scaled pose with the specified single-precision 4 x 4 matrix

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
init?(_ matrix: simd_float4x4)
```

#### Discussion

> **Note**: This function can’t extract rotation from a non-scale-rotate-translate affine transform. In that case, the function returns `nil`.  If the specified matrix doesn’t have uniform scale the function returns `nil`.

## Parameters

- `matrix`: The source matrix


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/scaledpose3dfloat/init(_:)-4hh5z)*