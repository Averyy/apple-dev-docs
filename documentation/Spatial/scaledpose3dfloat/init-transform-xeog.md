# init(transform:)

**Framework**: Spatial  
**Kind**: init

Creates a pose with with a position, rotation, and scale that are defined by a projective transform.

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

A pose with a position, rotation, and scale that are defined by a projective transform.

#### Discussion

> **Note**: This function can’t extract rotation from a non-scale-rotate-translate affine transform. In that case, the function returns `nil`.  If the specified  [`ProjectiveTransform3DFloat`](projectivetransform3dfloat.md) doesn’t have uniform scale, the function returns `nil`.

## Parameters

- `transform`: The source transform. The function only considers the transform’s   rotation and translation components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/scaledpose3dfloat/init(transform:)-xeog)*