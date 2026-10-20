# init(count:coordinateSpace:inputKinds:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a tap gesture with the number of required taps, the coordinate space of the gesture’s location, and the input kinds the gesture recognizes.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
nonisolated
init(count: Int = 1, coordinateSpace: some CoordinateSpaceProtocol = .local, inputKinds: GestureInputKinds = .all)
```

## Parameters

- `count`: The required number of taps to complete the tap gesture.
- `coordinateSpace`: The coordinate space of the tap gesture’s location.
- `inputKinds`: A set of input kinds that this gesture recognizes. If not specified, the gesture will recognize all applicable input kinds that a person can use to perform it.

## See Also

### Creating a spatial tap gesture
- [init(count: Int, coordinateSpace3D: some CoordinateSpace3D)](./init%28count,coordinatespace3d%29.md)
  Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spatialtapgesture/init(count:coordinatespace:inputkinds:))*