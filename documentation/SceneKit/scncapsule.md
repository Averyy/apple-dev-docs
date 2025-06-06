# SCNCapsule

**Framework**: SceneKit  
**Kind**: class

A right circular cylinder geometry whose ends are capped with hemispheres.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class SCNCapsule
```

#### Overview

![None](https://docs-assets.developer.apple.com/published/90b8dce3e43df2a5cac61f9bbb933d7a/media-2929808%402x.png)

Define the size of the two hemispheres forming the ends of a capsule with the [`capRadius`](scncapsule/capradius.md) property. Because the cylindrical body of the capsule stretches between the its two hemispherical ends, its circular cross section in the x- and z-axis dimensions has the same radius. Define the capsule’s extent in the z-axis dimension of its local coordinate space with the [`height`](scncapsule/height.md) property. To change the orientation of a capsule, adjust the [`transform`](scnnode/transform.md) property of the node containing the capsule geometry.

Control the level of detail with the [`heightSegmentCount`](scncapsule/heightsegmentcount.md), [`capSegmentCount`](scncapsule/capsegmentcount.md), and [`height`](scncapsule/height.md) properties. Higher radial and cap segment counts create smoother curves for the cylinder’s circular sides and hemispherical ends. A higher segment count in any direction produces more vertices, which can improve rendering quality for certain lighting models or custom shader effects, but at a cost to rendering performance.

## Topics

### Creating a Capsule
- [convenience init(capRadius: CGFloat, height: CGFloat)](scncapsule/init(capradius:height:).md)
  Creates a capsule geometry with the specified radius and height.
### Adjusting a Capsule’s Dimensions
- [var capRadius: CGFloat](scncapsule/capradius.md)
  The radius both of the capsule’s circular center cross section and of its hemispherical ends. Animatable.
- [var height: CGFloat](scncapsule/height.md)
  The extent of the capsule along its y-axis. Animatable.
### Adjusting Geometric Detail
- [var radialSegmentCount: Int](scncapsule/radialsegmentcount.md)
  The number of subdivisions around the lateral circumference of the capsule. Animatable.
- [var capSegmentCount: Int](scncapsule/capsegmentcount.md)
  The number of subdivisions in the height of each hemispherical end of the capsule. Animatable.
- [var heightSegmentCount: Int](scncapsule/heightsegmentcount.md)
  The number of subdivisions in the sides of the capsule along its y-axis. Animatable.

## Relationships

### Inherits From
- [SCNGeometry](scngeometry.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [SCNAnimatable](scnanimatable.md)
- [SCNBoundingVolume](scnboundingvolume.md)
- [SCNShadable](scnshadable.md)

## See Also

- [class SCNFloor](scnfloor.md)
  A plane that can optionally display a reflection of the scene above it.
- [class SCNBox](scnbox.md)
  A six-sided polyhedron geometry whose faces are all rectangles, optionally with rounded edges and corners.
- [class SCNCone](scncone.md)
  A right circular cone or frustum geometry.
- [class SCNCylinder](scncylinder.md)
  A right circular cylinder geometry.
- [class SCNPlane](scnplane.md)
  A rectangular, one-sided plane geometry of specified width and height.
- [class SCNPyramid](scnpyramid.md)
  A right rectangular pyramid geometry.
- [class SCNSphere](scnsphere.md)
  A sphere (or ball or globe) geometry.
- [class SCNTorus](scntorus.md)
  A torus, or ring-shaped geometry.
- [class SCNTube](scntube.md)
  A tube or pipe geometry—a right circular cylinder with a circular hole along its central axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncapsule)*