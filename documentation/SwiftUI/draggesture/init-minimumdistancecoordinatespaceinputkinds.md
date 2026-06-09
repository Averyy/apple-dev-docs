# init(minimumDistance:coordinateSpace:inputKinds:)

**Framework**: SwiftUI  
**Kind**: init

Creates a dragging gesture with the minimum dragging distance before the gesture succeeds, the coordinate space of the gesture’s location, and the input kinds the gesture recognizes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

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

- [init(minimumDistance: CGFloat, coordinateSpace: some CoordinateSpaceProtocol)](draggesture/init(minimumdistance:coordinatespace:)-8ffe5.md)
  Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.
- [init(minimumDistance:coordinateSpace:)](draggesture/init(minimumdistance:coordinatespace:).md)
  Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.
- [init(minimumDistance: CGFloat, coordinateSpace3D: some CoordinateSpace3D)](draggesture/init(minimumdistance:coordinatespace3d:).md)
  Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.
- [var minimumDistance: CGFloat](draggesture/minimumdistance.md)
  The minimum dragging distance before the gesture succeeds.
- [var coordinateSpace: CoordinateSpace](draggesture/coordinatespace.md)
  The coordinate space in which to receive location values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/draggesture/init(minimumdistance:coordinatespace:inputkinds:))*