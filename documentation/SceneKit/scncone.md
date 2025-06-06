# SCNCone

**Framework**: SceneKit  
**Kind**: class

A right circular cone or frustum geometry.

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
class SCNCone
```

#### Overview

![None](https://docs-assets.developer.apple.com/published/c98604b0c5b0a6a33ac4e0c4c7d4e68a/media-2929809%402x.png)

A cone defines the surface of a solid whose base is a circle and whose side surface tapers to a point centered above its base. A frustum also has a circular base and tapered sides but has a circular top, similar to a cone cut off below its apex.

Define the size of the cone’s base in the x- and z-axis dimensions of its local coordinate space with its [`bottomRadius`](scncone/bottomradius.md) property, and its extent in the y-axis dimension with its [`height`](scncone/height.md) property. Create a cone that tapers to a point by setting its [`topRadius`](scncone/topradius.md) property to zero, or a frustum that tapers (or expands) to a circular top by setting the [`topRadius`](scncone/topradius.md) property to a different value.

To position and orient a cone in a scene, attach it to the [`geometry`](scnnode/geometry.md) property of an [`SCNNode`](scnnode.md) object.

Control the level of detail with the [`radialSegmentCount`](scncone/radialsegmentcount.md) and [`heightSegmentCount`](scncone/heightsegmentcount.md) properties. A higher radial segment count creates a smoother curve for the cone’s circular sides. A higher segment count in either direction produces more vertices, which can improve rendering quality for certain lighting models or custom shader effects, but at a cost to rendering performance.

A cone geometry may contain two or three [`SCNGeometryElement`](scngeometryelement.md) objects, corresponding to its outer surface, its base and its top (or base only or top only, if the [`topRadius`](scncone/topradius.md) or [`bottomRadius`](scncone/bottomradius.md) property is zero). SceneKit can render each element using a different material. For details, see the [`materials`](scngeometry/materials.md) property in [`SCNGeometry`](scngeometry.md).

## Topics

### Creating a Cone
- [convenience init(topRadius: CGFloat, bottomRadius: CGFloat, height: CGFloat)](scncone/init(topradius:bottomradius:height:).md)
  Creates a cone geometry with the given top radius, bottom radius, and height.
### Adjusting a Cone’s Dimensions
- [var topRadius: CGFloat](scncone/topradius.md)
  The radius of the cone’s circular top. Animatable.
- [var bottomRadius: CGFloat](scncone/bottomradius.md)
  The radius of the cone’s circular base. Animatable.
- [var height: CGFloat](scncone/height.md)
  The extent of the cylinder along its y-axis. Animatable.
### Adjusting Geometric Detail
- [var radialSegmentCount: Int](scncone/radialsegmentcount.md)
  The number of subdivisions around the circumference of the cone. Animatable.
- [var heightSegmentCount: Int](scncone/heightsegmentcount.md)
  The number of subdivisions in the sides of the cone along its y-axis. Animatable.

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

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncone)*