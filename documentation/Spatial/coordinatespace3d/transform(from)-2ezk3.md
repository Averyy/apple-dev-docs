# transform(from:)

**Framework**: Spatial  
**Kind**: method  
**Role**: Instance Method

Returns a transform of this coordinate space from the target coordinate space.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func transform<Space>(from target: Space) throws -> ProjectiveTransform3D where Space : CoordinateSpace3D
```

## Parameters

- `target`: Another coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/coordinatespace3d/transform(from:)-2ezk3)*