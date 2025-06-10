# transformSpace(_:)

**Framework**: Spatial  
**Kind**: method

Returns a modified version of the coordinate space.

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
func transformSpace(_ baseFromMapTransform: @escaping (Self) -> ProjectiveTransform3D) -> some CoordinateSpace3D
```

## Parameters

- `baseFromMapTransform`: A closure which takes in the base coordinate space   and returns a transform that represents the modification to that space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/coordinatespace3d/transformspace(_:))*