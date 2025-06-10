# transform(from:)

**Framework**: Spatial  
**Kind**: method  
**Required**: Yes

Returns a transform of this coordinate space from the target coordinate space.

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
func transform(from targetCoordinateSpace: Self) throws -> ProjectiveTransform3D
```

#### Discussion

This method is dedicated for converting between coordinate spaces of the same type. Implementations may be more efficient than the general purpose convert functions, but results should be the same. A default implementation is provided which uses root level conversions.

## Parameters

- `targetCoordinateSpace`: Another coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/coordinatespace3d/transform(from:))*