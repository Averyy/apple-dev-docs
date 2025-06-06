# SCNCylinder

**Framework**: SceneKit  
**Kind**: class

A right circular cylinder geometry.

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
class SCNCylinder
```

#### Overview

![None](https://docs-assets.developer.apple.com/published/ac3acc88eb04c91eed6d3765814046e9/media-2929812%402x.png)

A cylinder defines the surface of a solid whose every cross section along a linear axis is a circle of equal size. Define the size of the cylinder’s cross section in the x- and z-axis dimensions of its local coordinate space with the [`radius`](scncylinder/radius.md) property, and its extent in the y-axis dimension with the [`height`](scncylinder/height.md) property. To position and orient a cylinder in a scene, attach it to the [`geometry`](scnnode/geometry.md) property of an [`SCNNode`](scnnode.md) object.

Control the level of detail with the [`radialSegmentCount`](scncylinder/radialsegmentcount.md) and [`heightSegmentCount`](scncylinder/heightsegmentcount.md) properties. A higher radial segment count creates a smoother curve for the cylinder’s circular sides. A higher segment count in either direction produces more vertices, which can improve rendering quality for certain lighting models or custom shader effects, but at a cost to rendering performance.

A cylinder contains three [`SCNGeometryElement`](scngeometryelement.md) objects: one each for its base and top, and one that wraps around its sides. SceneKit can render each element using a different material. For details, see the [`materials`](scngeometry/materials.md) property in [`SCNGeometry`](scngeometry.md).

## Topics

### Creating a Cylinder
- [convenience init(radius: CGFloat, height: CGFloat)](scncylinder/init(radius:height:).md)
  Creates a cylinder geometry with the specified radius and height.
### Adjusting a Cylinder’s Dimensions
- [var radius: CGFloat](scncylinder/radius.md)
  The radius of the cylinder’s circular cross section. Animatable.
- [var height: CGFloat](scncylinder/height.md)
  The extent of the cylinder along its y-axis. Animatable.
### Adjusting Geometric Detail
- [var radialSegmentCount: Int](scncylinder/radialsegmentcount.md)
  The number of subdivisions around the circumference of the cylinder. Animatable.
- [var heightSegmentCount: Int](scncylinder/heightsegmentcount.md)
  The number of subdivisions in the sides of the cylinder along its y-axis. Animatable.

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
- [class SCNCapsule](scncapsule.md)
  A right circular cylinder geometry whose ends are capped with hemispheres.
- [class SCNCone](scncone.md)
  A right circular cone or frustum geometry.
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

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncylinder)*