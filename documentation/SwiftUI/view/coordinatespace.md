# coordinateSpace(_:)

**Framework**: SwiftUI  
**Kind**: method

Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
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

Here, the [`VStack`](vstack.md) in the `ContentView` named “stack” is composed of a red frame with a custom [`Circle`](circle.md) view [`overlay(_:alignment:)`](view/overlay(_:alignment:).md) at its center.

The `circle` view has an attached [`DragGesture`](draggesture.md) that targets the enclosing VStack’s coordinate space. As the gesture recognizer’s closure registers events inside `circle` it stores them in the shared `location` state variable and the [`VStack`](vstack.md) displays the coordinates in a [`Text`](text.md) view.

![A screenshot showing an example of finding a named view and tracking](https://docs-assets.developer.apple.com/published/a7b7c1917dbc86bfc1787941553b5584/SwiftUI-View-coordinateSpace%402x.png)

## Parameters

- `name`: A name used to identify this coordinate space.

## See Also

- [struct GeometryReader](geometryreader.md)
  A container view that defines its content as a function of its own size and coordinate space.
- [struct GeometryReader3D](geometryreader3d.md)
  A container view that defines its content as a function of its own size and coordinate space.
- [struct GeometryProxy](geometryproxy.md)
  A proxy for access to the size and coordinate space (for anchor resolution) of the container view.
- [struct GeometryProxy3D](geometryproxy3d.md)
  A proxy for access to the size and coordinate space of the container view.
- [enum CoordinateSpace](coordinatespace.md)
  A resolved coordinate space created by the coordinate space protocol.
- [protocol CoordinateSpaceProtocol](coordinatespaceprotocol.md)
  A frame of reference within the layout system.
- [struct PhysicalMetric](physicalmetric.md)
  Provides access to a value in points that corresponds to the specified physical measurement.
- [struct PhysicalMetricsConverter](physicalmetricsconverter.md)
  A physical metrics converter provides conversion between point values and their extent in 3D space, in the form of physical length measurements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/coordinatespace(_:))*