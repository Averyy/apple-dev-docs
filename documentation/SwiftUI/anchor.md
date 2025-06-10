# Anchor

**Framework**: SwiftUI  
**Kind**: struct

An opaque value derived from an anchor source and a particular view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@frozen
struct Anchor<Value>
```

#### Overview

You can convert the anchor to a `Value` in the coordinate space of a target view by using a [`GeometryProxy`](geometryproxy.md) to specify the target view.

## Topics

### Getting the anchor’s source
- [Anchor.Source](anchor/source.md)
  A type-erased geometry value that produces an anchored value of a given type.

## Relationships

### Conforms To
- [CoordinateSpaceValue3D](../Spatial/CoordinateSpaceValue3D.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum Axis](axis.md)
  The horizontal or vertical dimension in a 2D coordinate system.
- [struct Angle](angle.md)
  A geometric angle whose value you access in either radians or degrees.
- [struct UnitPoint](unitpoint.md)
  A normalized 2D point in a view’s coordinate space.
- [struct UnitPoint3D](unitpoint3d.md)
  A normalized 3D point in a view’s coordinate space.
- [protocol DepthAlignmentID](depthalignmentid.md)
- [struct Alignment3D](alignment3d.md)
  An alignment in all three axes.
- [struct GeometryProxyCoordinateSpace3D](geometryproxycoordinatespace3d.md)
  A representation of a `GeometryProxy3D` which can be used for `CoordinateSpace3D` based conversions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/anchor)*