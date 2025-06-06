# CoordinateSpaceProtocol

**Framework**: SwiftUI  
**Kind**: protocol

A frame of reference within the layout system.

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
protocol CoordinateSpaceProtocol
```

#### Overview

All geometric properties of a view, including size, position, and transform, are defined within the local coordinate space of the view’s parent. These values can be converted into other coordinate spaces by passing types conforming to this protocol into functions such as `GeometryProxy.frame(in:)`.

For example, a named coordinate space allows you to convert the frame of a view into the local coordinate space of an ancestor view by defining a named coordinate space using the `coordinateSpace(_:)` modifier, then passing that same named coordinate space into the `frame(in:)` function.

```swift
VStack {
    GeometryReader { geometryProxy in
        let distanceFromTop = geometryProxy.frame(in: "container").origin.y
        Text("This view is \(distanceFromTop) points from the top of the VStack")
    }
    .padding()
}
.coordinateSpace(.named("container"))
```

You don’t typically create types conforming to this protocol yourself. Instead, use the system-provided `.global`, `.local`, and `.named(_:)` implementations.

## Topics

### Getting built-in coordinate spaces
- [static var immersiveSpace: NamedCoordinateSpace](coordinatespaceprotocol/immersivespace.md)
  The named coordinate space that represents the currently opened [`ImmersiveSpace`](immersivespace.md) scene. If no immersive space is currently opened, this CoordinateSpace provides the same behavior as the `.global` coordinate space.
- [static var global: GlobalCoordinateSpace](coordinatespaceprotocol/global.md)
  The global coordinate space at the root of the view hierarchy.
- [static var local: LocalCoordinateSpace](coordinatespaceprotocol/local.md)
  The local coordinate space of the current view.
- [static func named(some Hashable) -> NamedCoordinateSpace](coordinatespaceprotocol/named(_:).md)
  Creates a named coordinate space using the given value.
- [static var scrollView: NamedCoordinateSpace](coordinatespaceprotocol/scrollview.md)
  The named coordinate space that is added by the system for the innermost containing scroll view.
- [static func scrollView(axis: Axis) -> Self](coordinatespaceprotocol/scrollview(axis:).md)
  The named coordinate space that is added by the system for the innermost containing scroll view that allows scrolling along the provided axis.
### Getting the resolved coordinate space
- [var coordinateSpace: CoordinateSpace](coordinatespaceprotocol/coordinatespace.md)
  The resolved coordinate space.
### Supporting types
- [struct GlobalCoordinateSpace](globalcoordinatespace.md)
  The global coordinate space at the root of the view hierarchy.
- [struct LocalCoordinateSpace](localcoordinatespace.md)
  The local coordinate space of the current view.
- [struct NamedCoordinateSpace](namedcoordinatespace.md)
  A named coordinate space.

## Relationships

### Conforming Types
- [GlobalCoordinateSpace](globalcoordinatespace.md)
- [LocalCoordinateSpace](localcoordinatespace.md)
- [NamedCoordinateSpace](namedcoordinatespace.md)

## See Also

- [struct GeometryReader](geometryreader.md)
  A container view that defines its content as a function of its own size and coordinate space.
- [struct GeometryReader3D](geometryreader3d.md)
  A container view that defines its content as a function of its own size and coordinate space.
- [struct GeometryProxy](geometryproxy.md)
  A proxy for access to the size and coordinate space (for anchor resolution) of the container view.
- [struct GeometryProxy3D](geometryproxy3d.md)
  A proxy for access to the size and coordinate space of the container view.
- [func coordinateSpace(NamedCoordinateSpace) -> some View](view/coordinatespace(_:).md)
  Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.
- [enum CoordinateSpace](coordinatespace.md)
  A resolved coordinate space created by the coordinate space protocol.
- [struct PhysicalMetric](physicalmetric.md)
  Provides access to a value in points that corresponds to the specified physical measurement.
- [struct PhysicalMetricsConverter](physicalmetricsconverter.md)
  A physical metrics converter provides conversion between point values and their extent in 3D space, in the form of physical length measurements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/coordinatespaceprotocol)*