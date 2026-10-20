# init(minimumDistance:coordinateSpace3D:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

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

### Creating a drag gesture
- [init(minimumDistance: CGFloat, coordinateSpace: some CoordinateSpaceProtocol, inputKinds: GestureInputKinds)](./init%28minimumdistance,coordinatespace,inputkinds%29.md)
  Creates a dragging gesture with the minimum dragging distance before the gesture succeeds, the coordinate space of the gesture’s location, and the input kinds the gesture recognizes.
- [var minimumDistance: CGFloat](./minimumdistance.md)
  The minimum dragging distance before the gesture succeeds.
- [var coordinateSpace: CoordinateSpace](./coordinatespace.md)
  The coordinate space in which to receive location values.
- [init(minimumDistance: CGFloat, coordinateSpace: some CoordinateSpaceProtocol)](./init%28minimumdistance,coordinatespace%29-8ffe5.md)
  Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.
- [init(minimumDistance:coordinateSpace:)](./init%28minimumdistance,coordinatespace%29.md)
  Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.
- [init(minimumDistance: CGFloat, coordinateSpace: CoordinateSpace)](./init%28minimumdistance,coordinatespace%29-3804h.md)
  Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/draggesture/init(minimumdistance:coordinatespace3d:))*