# init(count:coordinateSpace3D:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
nonisolated
init(count: Int = 1, coordinateSpace3D: some CoordinateSpace3D)
```

## Parameters

- `count`: The required number of taps to complete the tap gesture.
- `coordinateSpace3D`: The coordinate space 3D of the tap gesture’s location.

## See Also

### Creating a spatial tap gesture
- [init(count: Int, coordinateSpace: some CoordinateSpaceProtocol, inputKinds: GestureInputKinds)](./init%28count,coordinatespace,inputkinds%29.md)
  Creates a tap gesture with the number of required taps, the coordinate space of the gesture’s location, and the input kinds the gesture recognizes.
- [var coordinateSpace: CoordinateSpace](./coordinatespace.md)
  The coordinate space in which to receive location values.
- [var count: Int](./count.md)
  The required number of tap events.
- [init(count: Int, coordinateSpace: some CoordinateSpaceProtocol)](./init%28count,coordinatespace%29-75s7q.md)
  Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.
- [init(count:coordinateSpace:)](./init%28count,coordinatespace%29.md)
  Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.
- [init(count: Int, coordinateSpace: CoordinateSpace)](./init%28count,coordinatespace%29-1b85g.md)
  Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spatialtapgesture/init(count:coordinatespace3d:))*