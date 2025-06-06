# SCNBox

**Framework**: SceneKit  
**Kind**: class

A six-sided polyhedron geometry whose faces are all rectangles, optionally with rounded edges and corners.

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
class SCNBox
```

#### Overview

![None](https://docs-assets.developer.apple.com/published/2626bbf0d905da4f946e9f326170a985/media-2929807%402x.png)

Define the shape of the box in the x-, y-, and z-axis dimensions of its local coordinate space by setting its [`width`](scnbox/width.md), [`height`](scnbox/height.md), and [`length`](scnbox/length.md) properties. Add rounded edges and corners to a box with its [`chamferRadius`](scnbox/chamferradius.md) property. To position and orient a box in a scene, attach it to the [`geometry`](scnnode/geometry.md) property of an [`SCNNode`](scnnode.md) object.

Control the level of detail with the [`widthSegmentCount`](scnbox/widthsegmentcount.md), [`heightSegmentCount`](scnbox/heightsegmentcount.md), [`lengthSegmentCount`](scnbox/lengthsegmentcount.md), and [`chamferSegmentCount`](scnbox/chamfersegmentcount.md) properties. A higher segment count produces more vertices, which can improve rendering quality for certain lighting models or custom shader effects, but at a cost to rendering performance.

You can assign up to six [`SCNMaterial`](scnmaterial.md) instances to a box—one for each side—with its [`materials`](scngeometry/materials.md) property. The [`SCNBox`](scnbox.md) class automatically creates [`SCNGeometryElement`](scngeometryelement.md) objects as needed to handle the number of materials.

## Topics

### Creating a Box
- [convenience init(width: CGFloat, height: CGFloat, length: CGFloat, chamferRadius: CGFloat)](scnbox/init(width:height:length:chamferradius:).md)
  Creates a box geometry with the specified width, height, length, and chamfer radius.
### Adjusting a Box’s Dimensions
- [var width: CGFloat](scnbox/width.md)
  The extent of the box along its x-axis. Animatable.
- [var height: CGFloat](scnbox/height.md)
  The extent of the box along its y-axis. Animatable.
- [var length: CGFloat](scnbox/length.md)
  The extent of the box along its z-axis. Animatable.
### Configuring Box Properties
- [var widthSegmentCount: Int](scnbox/widthsegmentcount.md)
  The number of subdivisions in each face of the box along its x-axis. Animatable.
- [var heightSegmentCount: Int](scnbox/heightsegmentcount.md)
  The number of subdivisions in each face of the box along its y-axis. Animatable.
- [var lengthSegmentCount: Int](scnbox/lengthsegmentcount.md)
  The number of subdivisions in each face of the box along its z-axis. Animatable.
### Adding Rounded Edges and Corners
- [var chamferRadius: CGFloat](scnbox/chamferradius.md)
  The radius of curvature for the edges and corners of the box. Animatable.
- [var chamferSegmentCount: Int](scnbox/chamfersegmentcount.md)
  The number of line segments used to create each rounded edge of the box. Animatable.

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
- [class SCNCapsule](scncapsule.md)
  A right circular cylinder geometry whose ends are capped with hemispheres.
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

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnbox)*