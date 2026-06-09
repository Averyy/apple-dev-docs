# init(count:coordinateSpace:inputKinds:)

**Framework**: SwiftUI  
**Kind**: init

Creates a tap gesture with the number of required taps, the coordinate space of the gesture’s location, and the input kinds the gesture recognizes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

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

- [init(count: Int, coordinateSpace: some CoordinateSpaceProtocol)](spatialtapgesture/init(count:coordinatespace:)-75s7q.md)
  Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.
- [init(count:coordinateSpace:)](spatialtapgesture/init(count:coordinatespace:).md)
  Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.
- [init(count: Int, coordinateSpace3D: some CoordinateSpace3D)](spatialtapgesture/init(count:coordinatespace3d:).md)
  Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.
- [var coordinateSpace: CoordinateSpace](spatialtapgesture/coordinatespace.md)
  The coordinate space in which to receive location values.
- [var count: Int](spatialtapgesture/count.md)
  The required number of tap events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spatialtapgesture/init(count:coordinatespace:inputkinds:))*