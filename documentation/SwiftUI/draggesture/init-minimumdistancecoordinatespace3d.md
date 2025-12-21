# init(minimumDistance:coordinateSpace3D:)

**Framework**: SwiftUI  
**Kind**: init

Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
init(minimumDistance: CGFloat = 0, coordinateSpace3D: some CoordinateSpace3D)
```

## Parameters

- `minimumDistance`: The minimum dragging distance for the gesture to   succeed. Ensure this unit is in the same scale as the   provided  , the default value is 0 to avoid issues   around differing coordinate space scales.
- `coordinateSpace3D`: The coordinate space 3D of the dragging gesture’s   location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/draggesture/init(minimumdistance:coordinatespace3d:))*