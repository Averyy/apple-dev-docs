# init(count:coordinateSpace:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
init(count: Int = 1, coordinateSpace: some CoordinateSpaceProtocol = .local)
```

**Other overloads**:

```swift
nonisolated
init(count: Int = 1, coordinateSpace: CoordinateSpace = .local)
```

## Parameters

- `count`: The required number of taps to complete the tap gesture.
- `coordinateSpace`: The coordinate space of the tap gesture’s location.

## See Also

### Creating a spatial tap gesture
- [init(count: Int, coordinateSpace3D: some CoordinateSpace3D)](./init%28count,coordinatespace3d%29.md)
  Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.
- [init(count: Int, coordinateSpace: some CoordinateSpaceProtocol, inputKinds: GestureInputKinds)](./init%28count,coordinatespace,inputkinds%29.md)
  Creates a tap gesture with the number of required taps, the coordinate space of the gesture’s location, and the input kinds the gesture recognizes.
- [var coordinateSpace: CoordinateSpace](./coordinatespace.md)
  The coordinate space in which to receive location values.
- [var count: Int](./count.md)
  The required number of tap events.
- [init(count:coordinateSpace:)](./init%28count,coordinatespace%29.md)
  Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.
- [init(count: Int, coordinateSpace: CoordinateSpace)](./init%28count,coordinatespace%29-1b85g.md)
  Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spatialtapgesture/init(count:coordinatespace:)-75s7q)*