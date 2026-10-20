# coordinateSpace(name:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- macOS 10.15+ - Deprecated in 27.2
- tvOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 6.0+ - Deprecated in 27.2

> **Deprecated**: Use [`coordinateSpace(_:)`](./coordinatespace%28_%29.md) instead.

## Declaration

```swift
nonisolated
func coordinateSpace<T>(name: T) -> some View where T : Hashable
```

#### Discussion

Use `coordinateSpace(name:)` to allow another function to find and operate on a view and operate on dimensions relative to that view.

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
        .coordinateSpace(name: "stack")
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

Here, the [`VStack`](../vstack.md) in the `ContentView` named “stack” is composed of a red frame with a custom [`Circle`](../circle.md) view [`overlay(_:alignment:)`](./overlay%28_,alignment%29.md) at its center.

The `circle` view has an attached [`DragGesture`](../draggesture.md) that targets the enclosing VStack’s coordinate space. As the gesture recognizer’s closure registers events inside `circle` it stores them in the shared `location` state variable and the [`VStack`](../vstack.md) displays the coordinates in a [`Text`](../text.md) view.

![A screenshot showing an example of finding a named view and tracking](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-View-coordinateSpace@2x.png)

## Parameters

- `name`: A name used to identify this coordinate space.

## See Also

### Layout modifiers
- [func frame() -> some View](./frame%28%29.md)
  Positions this view within an invisible frame.
- [func edgesIgnoringSafeArea(Edge.Set) -> some View](./edgesignoringsafearea%28_%29.md)
  Changes the view’s proposed area to extend outside the screen’s safe areas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/coordinatespace(name:))*