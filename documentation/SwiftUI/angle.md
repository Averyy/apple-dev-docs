# Angle

**Framework**: SwiftUI  
**Kind**: struct

A geometric angle whose value you access in either radians or degrees.

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
struct Angle
```

## Topics

### Getting constant angles
- [static var zero: Angle](angle/zero.md)
- [static func degrees(Double) -> Angle](angle/degrees(_:).md)
- [static func radians(Double) -> Angle](angle/radians(_:).md)
### Creating an angle
- [init()](angle/init.md)
- [init(degrees: Double)](angle/init(degrees:).md)
- [init(radians: Double)](angle/init(radians:).md)
- [init(Angle2D)](angle/init(_:).md)
### Getting the angle size
- [var degrees: Double](angle/degrees.md)
- [var radians: Double](angle/radians.md)

## Relationships

### Conforms To
- [Animatable](animatable.md)
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Comparable](../Swift/Comparable.md)
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum Axis](axis.md)
  The horizontal or vertical dimension in a 2D coordinate system.
- [struct UnitPoint](unitpoint.md)
  A normalized 2D point in a view’s coordinate space.
- [struct UnitPoint3D](unitpoint3d.md)
  A normalized 3D point in a view’s coordinate space.
- [struct Anchor](anchor.md)
  An opaque value derived from an anchor source and a particular view.
- [protocol DepthAlignmentID](depthalignmentid.md)
- [struct Alignment3D](alignment3d.md)
  An alignment in all three axes.
- [struct GeometryProxyCoordinateSpace3D](geometryproxycoordinatespace3d.md)
  A representation of a `GeometryProxy3D` which can be used for `CoordinateSpace3D` based conversions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/angle)*