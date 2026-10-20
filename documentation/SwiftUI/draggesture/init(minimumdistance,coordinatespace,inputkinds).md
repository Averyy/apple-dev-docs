# init(minimumDistance:coordinateSpace:inputKinds:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a dragging gesture with the minimum dragging distance before the gesture succeeds, the coordinate space of the gesture’s location, and the input kinds the gesture recognizes.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
@MainActor
@preconcurrency init(minimumDistance: CGFloat = 10, coordinateSpace: some CoordinateSpaceProtocol = .local, inputKinds: GestureInputKinds = .all)
```

## Parameters

- `minimumDistance`: The minimum distance a person needs to drag before the drag gesture begins.
- `coordinateSpace`: The coordinate space of the dragging gesture’s location.
- `inputKinds`: A set of input kinds that this gesture recognizes. If not specified, the gesture will recognize all applicable input kinds that a person can use to perform it.

## See Also

### Creating a drag gesture
- [init(minimumDistance: CGFloat, coordinateSpace3D: some CoordinateSpace3D)](./init%28minimumdistance,coordinatespace3d%29.md)
  Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/draggesture/init(minimumdistance:coordinatespace:inputkinds:))*