# init(minimumDistance:coordinateSpace:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 6.0+ - Deprecated in 27.2

> **Deprecated**: Use [`init(minimumDistance:coordinateSpace:)`](./init%28minimumdistance,coordinatespace%29-8ffe5.md) instead.

## Declaration

```swift
@MainActor
@preconcurrency init(minimumDistance: CGFloat = 10, coordinateSpace: CoordinateSpace = .local)
```

**Other overloads**:

```swift
@MainActor
@preconcurrency init(minimumDistance: CGFloat = 10, coordinateSpace: some CoordinateSpaceProtocol = .local)
```

## Parameters

- `minimumDistance`: The minimum dragging distance for the gesture to succeed.
- `coordinateSpace`: The coordinate space of the dragging gesture’s location.

## See Also

### Creating a drag gesture
- [init(minimumDistance: CGFloat, coordinateSpace3D: some CoordinateSpace3D)](./init%28minimumdistance,coordinatespace3d%29.md)
  Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/draggesture/init(minimumdistance:coordinatespace:)-3804h)*