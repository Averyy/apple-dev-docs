# init(count:coordinateSpace3D:)

**Framework**: SwiftUI  
**Kind**: init

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

- [init(count: Int, coordinateSpace: some CoordinateSpaceProtocol)](spatialtapgesture/init(count:coordinatespace:)-75s7q.md)
  Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.
- [init(count:coordinateSpace:)](spatialtapgesture/init(count:coordinatespace:).md)
  Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.
- [init(count: Int, coordinateSpace: some CoordinateSpaceProtocol, inputKinds: GestureInputKinds)](spatialtapgesture/init(count:coordinatespace:inputkinds:).md)
  Creates a tap gesture with the number of required taps, the coordinate space of the gesture’s location, and the input kinds the gesture recognizes.
- [var coordinateSpace: CoordinateSpace](spatialtapgesture/coordinatespace.md)
  The coordinate space in which to receive location values.
- [var count: Int](spatialtapgesture/count.md)
  The required number of tap events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spatialtapgesture/init(count:coordinatespace3d:))*