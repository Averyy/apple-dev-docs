# init(transform:)

**Framework**: Spatial  
**Kind**: init

Creates a pose with with a position and rotation that are defined by a projective transform.

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
init?(transform: ProjectiveTransform3DFloat)
```

#### Return Value

A pose with a position and rotation that are defined by a projective transform.

#### Discussion

> **Note**: This function can’t extract rotation from a non-scale-rotate-translate affine transform. In that case, the function returns `nil`.

## Parameters

- `transform`: The source transform. The function only considers the transform’s   rotation and translation components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/pose3dfloat/init(transform:)-94kwr)*