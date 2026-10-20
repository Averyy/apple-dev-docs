# TapGesture

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A gesture that recognizes one or more taps.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
struct TapGesture
```

#### Overview

To recognize a tap gesture on a view, create and configure the gesture, and then add it to the view using the [`gesture(_:including:)`](./view/gesture%28_,including%29.md) modifier. The following code adds a tap gesture to a [`Circle`](./circle.md) that toggles the color of the circle:

```swift
struct TapGestureView: View {
    @State private var tapped = false

    var tap: some Gesture {
        TapGesture(count: 1)
            .onEnded { _ in self.tapped = !self.tapped }
    }

    var body: some View {
        Circle()
            .fill(self.tapped ? Color.blue : Color.red)
            .frame(width: 100, height: 100, alignment: .center)
            .gesture(tap)
    }
}
```

## Topics

### Creating a tap gesture
- [init(count: Int)](./tapgesture/init%28count%29.md)
  Creates a tap gesture with the number of required taps.
- [init(count: Int, inputKinds: GestureInputKinds)](./tapgesture/init%28count,inputkinds%29.md)
  Creates a tap gesture with the number of required taps and the input kinds the gesture recognizes.
- [var count: Int](./tapgesture/count.md)
  The required number of tap events.

## Relationships

### Conforms To
- [Gesture](./gesture.md)

## See Also

### Recognizing tap gestures
- [func onTapGesture(count: Int, perform: () -> Void) -> some View](./view/ontapgesture%28count,perform%29.md)
  Adds an action to perform when this view recognizes a tap gesture.
- [func onTapGesture(count: Int, coordinateSpace: some CoordinateSpaceProtocol, inputKinds: GestureInputKinds, perform: (CGPoint) -> Void) -> some View](./view/ontapgesture%28count,coordinatespace,inputkinds,perform%29.md)
  Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction.
- [struct SpatialTapGesture](./spatialtapgesture.md)
  A gesture that recognizes one or more taps and reports their location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tapgesture)*