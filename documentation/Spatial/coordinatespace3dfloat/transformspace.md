# transformSpace(_:)

**Framework**: Spatial  
**Kind**: method

Returns a modified version of the coordinate space.

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
func transformSpace(_ baseFromMapTransform: @escaping (Self) -> ProjectiveTransform3DFloat) -> some CoordinateSpace3DFloat
```

## Parameters

- `baseFromMapTransform`: A closure which takes in the base coordinate space   and returns a transform that represents the modification to that space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/coordinatespace3dfloat/transformspace(_:))*