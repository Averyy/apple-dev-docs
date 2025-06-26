# coordinateSpace(_:)

**Framework**: FamilyControls  
**Kind**: method

Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func coordinateSpace(_ name: NamedCoordinateSpace) -> some View
```

#### Discussion

Use `coordinateSpace(_:)` to allow another function to find and operate on a view and operate on dimensions relative to that view.

The example below demonstrates how a nested view can find and operate on its enclosing view’s coordinate space:

```swift
struct ContentView: View {
    @State private var location = CGPoint.zero

    var body: some View {
        VStack {
            Color.red.frame(width: 100, height: 100)
                .overlay(circle)
            Text("Location: \(Int(location.x)), \(Int(location.y))")
        }
        .coordinateSpace(.named("stack"))
    }

    var circle: some View {
        Circle()
            .frame(width: 25, height: 25)
            .gesture(drag)
            .padding(5)
    }

    var drag: some Gesture {
        DragGesture(coordinateSpace: .named("stack"))
            .onChanged { info in location = info.location }
    }
}
```

Here, the `VStack` in the `ContentView` named “stack” is composed of a red frame with a custom `Circle` view `View/overlay(_:alignment:)` at its center.

The `circle` view has an attached `DragGesture` that targets the enclosing VStack’s coordinate space. As the gesture recognizer’s closure registers events inside `circle` it stores them in the shared `location` state variable and the `VStack` displays the coordinates in a `Text` view.

## Parameters

- `name`: A name used to identify this coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivityiconview/coordinatespace(_:))*