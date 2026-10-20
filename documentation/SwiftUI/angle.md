# Angle

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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
- [static var zero: Angle](./angle/zero.md)
- [static func degrees(Double) -> Angle](./angle/degrees%28_%29.md)
- [static func radians(Double) -> Angle](./angle/radians%28_%29.md)
### Creating an angle
- [init()](./angle/init%28%29.md)
- [init(degrees: Double)](./angle/init%28degrees%29.md)
- [init(radians: Double)](./angle/init%28radians%29.md)
- [init(Angle2D)](./angle/init%28_%29.md)
### Getting the angle size
- [var degrees: Double](./angle/degrees.md)
- [var radians: Double](./angle/radians.md)

## Relationships

### Conforms To
- [Animatable](./animatable.md)
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Comparable](../Swift/comparable.md)
- [Copyable](../Swift/copyable.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing geometric constructs
- [enum Axis](./axis.md)
  The horizontal or vertical dimension in a 2D coordinate system.
- [struct UnitPoint](./unitpoint.md)
  A normalized 2D point in a view’s coordinate space.
- [struct UnitPoint3D](./unitpoint3d.md)
  A normalized 3D point in a view’s coordinate space.
- [struct Anchor](./anchor.md)
  An opaque value derived from an anchor source and a particular view.
- [protocol DepthAlignmentID](./depthalignmentid.md)
  A type that defines a custom depth alignment guide.
- [struct Alignment3D](./alignment3d.md)
  An alignment in all three axes.
- [struct GeometryProxyCoordinateSpace3D](./geometryproxycoordinatespace3d.md)
  A representation of a `GeometryProxy3D` which can be used for `CoordinateSpace3D` based conversions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/angle)*