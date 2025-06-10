# GeometryProxy3D

**Framework**: SwiftUI  
**Kind**: struct

A proxy for access to the size and coordinate space of the container view.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct GeometryProxy3D
```

#### Overview

You can use a proxy for anchor resolution.

## Topics

### Accessing geometry characteristics
- [func frame(in: some CoordinateSpaceProtocol) -> Rect3D](geometryproxy3d/frame(in:).md)
  The container view’s bounds rectangle converted to a defined coordinate space.
- [var size: Size3D](geometryproxy3d/size.md)
  The size of the container view.
- [var safeAreaInsets: EdgeInsets3D](geometryproxy3d/safeareainsets.md)
  The safe area inset of the container view.
- [subscript<T>(Anchor<T>) -> T](geometryproxy3d/subscript(_:).md)
  Resolves the value of an anchor to the container view.
- [func transform(in: some CoordinateSpaceProtocol) -> AffineTransform3D?](geometryproxy3d/transform(in:).md)
  The container view’s 3D transform converted to a defined coordinate space.
### Instance Methods
- [func coordinateSpace3D(for: any CoordinateSpaceProtocol) -> GeometryProxyCoordinateSpace3D](geometryproxy3d/coordinatespace3d(for:).md)
  Returns a value that can be used for `CoordinateSpace3D` based coordinate conversions.

## See Also

- [struct GeometryReader](geometryreader.md)
  A container view that defines its content as a function of its own size and coordinate space.
- [struct GeometryReader3D](geometryreader3d.md)
  A container view that defines its content as a function of its own size and coordinate space.
- [struct GeometryProxy](geometryproxy.md)
  A proxy for access to the size and coordinate space (for anchor resolution) of the container view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/geometryproxy3d)*