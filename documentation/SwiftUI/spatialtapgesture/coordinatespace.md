# coordinateSpace

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The coordinate space in which to receive location values.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var coordinateSpace: CoordinateSpace
```

## See Also

### Creating a spatial tap gesture
- [init(count: Int, coordinateSpace3D: some CoordinateSpace3D)](./init%28count,coordinatespace3d%29.md)
  Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.
- [init(count: Int, coordinateSpace: some CoordinateSpaceProtocol, inputKinds: GestureInputKinds)](./init%28count,coordinatespace,inputkinds%29.md)
  Creates a tap gesture with the number of required taps, the coordinate space of the gesture’s location, and the input kinds the gesture recognizes.
- [var count: Int](./count.md)
  The required number of tap events.
- [init(count: Int, coordinateSpace: some CoordinateSpaceProtocol)](./init%28count,coordinatespace%29-75s7q.md)
  Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.
- [init(count:coordinateSpace:)](./init%28count,coordinatespace%29.md)
  Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.
- [init(count: Int, coordinateSpace: CoordinateSpace)](./init%28count,coordinatespace%29-1b85g.md)
  Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spatialtapgesture/coordinatespace)*