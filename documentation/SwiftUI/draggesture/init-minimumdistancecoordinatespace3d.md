# init(minimumDistance:coordinateSpace3D:)

**Framework**: SwiftUI  
**Kind**: init

Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency init(minimumDistance: CGFloat = 0, coordinateSpace3D: some CoordinateSpace3D)
```

## Parameters

- `minimumDistance`: The minimum dragging distance for the gesture to succeed. Ensure this unit is in the same scale as the provided `CoordinateSpace3D`, the default value is 0 to avoid issues around differing coordinate space scales.
- `coordinateSpace3D`: The coordinate space 3D of the dragging gesture’s location.

## See Also

- [init(minimumDistance: CGFloat, coordinateSpace: some CoordinateSpaceProtocol)](draggesture/init(minimumdistance:coordinatespace:)-8ffe5.md)
  Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.
- [init(minimumDistance:coordinateSpace:)](draggesture/init(minimumdistance:coordinatespace:).md)
  Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.
- [init(minimumDistance: CGFloat, coordinateSpace: some CoordinateSpaceProtocol, inputKinds: GestureInputKinds)](draggesture/init(minimumdistance:coordinatespace:inputkinds:).md)
  Creates a dragging gesture with the minimum dragging distance before the gesture succeeds, the coordinate space of the gesture’s location, and the input kinds the gesture recognizes.
- [var minimumDistance: CGFloat](draggesture/minimumdistance.md)
  The minimum dragging distance before the gesture succeeds.
- [var coordinateSpace: CoordinateSpace](draggesture/coordinatespace.md)
  The coordinate space in which to receive location values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/draggesture/init(minimumdistance:coordinatespace3d:))*