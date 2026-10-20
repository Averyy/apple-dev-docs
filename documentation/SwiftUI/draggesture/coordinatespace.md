# coordinateSpace

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The coordinate space in which to receive location values.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@MainActor
@preconcurrency var coordinateSpace: CoordinateSpace
```

## See Also

### Creating a drag gesture
- [init(minimumDistance: CGFloat, coordinateSpace3D: some CoordinateSpace3D)](./init%28minimumdistance,coordinatespace3d%29.md)
  Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.
- [init(minimumDistance: CGFloat, coordinateSpace: some CoordinateSpaceProtocol, inputKinds: GestureInputKinds)](./init%28minimumdistance,coordinatespace,inputkinds%29.md)
  Creates a dragging gesture with the minimum dragging distance before the gesture succeeds, the coordinate space of the gesture’s location, and the input kinds the gesture recognizes.
- [var minimumDistance: CGFloat](./minimumdistance.md)
  The minimum dragging distance before the gesture succeeds.
- [init(minimumDistance: CGFloat, coordinateSpace: some CoordinateSpaceProtocol)](./init%28minimumdistance,coordinatespace%29-8ffe5.md)
  Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.
- [init(minimumDistance:coordinateSpace:)](./init%28minimumdistance,coordinatespace%29.md)
  Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.
- [init(minimumDistance: CGFloat, coordinateSpace: CoordinateSpace)](./init%28minimumdistance,coordinatespace%29-3804h.md)
  Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/draggesture/coordinatespace)*