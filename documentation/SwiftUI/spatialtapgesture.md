# SpatialTapGesture

**Framework**: SwiftUI  
**Kind**: struct

A gesture that recognizes one or more taps and reports their location.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct SpatialTapGesture
```

#### Overview

To recognize a tap gesture on a view, create and configure the gesture, and then add it to the view using the [`gesture(_:including:)`](view/gesture(_:including:).md) modifier. The following code adds a tap gesture to a [`Circle`](circle.md) that toggles the color of the circle based on the tap location:

```swift
struct TapGestureView: View {
    @State private var location: CGPoint = .zero

    var tap: some Gesture {
        SpatialTapGesture()
            .onEnded { event in
                self.location = event.location
             }
    }

    var body: some View {
        Circle()
            .fill(self.location.y > 50 ? Color.blue : Color.red)
            .frame(width: 100, height: 100, alignment: .center)
            .gesture(tap)
    }
}
```

## Topics

### Creating a spatial tap gesture
- [init(count: Int, coordinateSpace: some CoordinateSpaceProtocol)](spatialtapgesture/init(count:coordinatespace:)-75s7q.md)
  Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.
- [var coordinateSpace: CoordinateSpace](spatialtapgesture/coordinatespace.md)
  The coordinate space in which to receive location values.
- [var count: Int](spatialtapgesture/count.md)
  The required number of tap events.
### Getting the gesture’s value
- [SpatialTapGesture.Value](spatialtapgesture/value.md)
  The attributes of a tap gesture.
### Deprecated initializers
- [init(count: Int, coordinateSpace: CoordinateSpace)](spatialtapgesture/init(count:coordinatespace:)-1b85g.md)
  Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.
### Initializers
- [init(count:coordinateSpace:)](spatialtapgesture/init(count:coordinatespace:).md)
  Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.

## Relationships

### Conforms To
- [Gesture](gesture.md)

## See Also

- [func onTapGesture(count: Int, perform: () -> Void) -> some View](view/ontapgesture(count:perform:).md)
  Adds an action to perform when this view recognizes a tap gesture.
- [func onTapGesture(count:coordinateSpace:perform:)](view/ontapgesture(count:coordinatespace:perform:).md)
  Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction.
- [struct TapGesture](tapgesture.md)
  A gesture that recognizes one or more taps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spatialtapgesture)*