# GeometryReader3D

**Framework**: SwiftUI  
**Kind**: struct

A container view that defines its content as a function of its own size and coordinate space.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@frozen
struct GeometryReader3D<Content> where Content : View
```

#### Overview

This view returns a flexible preferred size to its own container view.

This container differs from [`GeometryReader`](geometryreader.md) in that it also reads available depth, and thus also returns a flexible preferred depth to its parent layout. Use the 3D version only in situations where you need to read depth, because it affects depth layout when used in a container like a [`ZStack`](zstack.md).

## Topics

### Creating a geometry reader
- [init(content: (GeometryProxy3D) -> Content)](geometryreader3d/init(content:).md)
- [var content: (GeometryProxy3D) -> Content](geometryreader3d/content.md)

## Relationships

### Conforms To
- [View](view.md)

## See Also

- [struct GeometryReader](geometryreader.md)
  A container view that defines its content as a function of its own size and coordinate space.
- [struct GeometryProxy](geometryproxy.md)
  A proxy for access to the size and coordinate space (for anchor resolution) of the container view.
- [struct GeometryProxy3D](geometryproxy3d.md)
  A proxy for access to the size and coordinate space of the container view.
- [func coordinateSpace(NamedCoordinateSpace) -> some View](view/coordinatespace(_:).md)
  Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.
- [enum CoordinateSpace](coordinatespace.md)
  A resolved coordinate space created by the coordinate space protocol.
- [protocol CoordinateSpaceProtocol](coordinatespaceprotocol.md)
  A frame of reference within the layout system.
- [struct PhysicalMetric](physicalmetric.md)
  Provides access to a value in points that corresponds to the specified physical measurement.
- [struct PhysicalMetricsConverter](physicalmetricsconverter.md)
  A physical metrics converter provides conversion between point values and their extent in 3D space, in the form of physical length measurements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/geometryreader3d)*