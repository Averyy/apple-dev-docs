# SCNPlane

**Framework**: SceneKit  
**Kind**: class

A rectangular, one-sided plane geometry of specified width and height.

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
class SCNPlane
```

#### Overview

![None](https://docs-assets.developer.apple.com/published/728b1f058100192814f51b3b907e28e7/media-2929811%402x.png)

A plane defines a flat surface in the x- and y-axis dimensions of its local coordinate space according to its [`width`](scnplane/width.md) and [`height`](scnplane/height.md) properties. To orient a plane differently, adjust the [`transform`](scnnode/transform.md) property of the node containing the plane geometry. You can create a rounded rectangular plane using the [`cornerRadius`](scnplane/cornerradius.md) property.

The surface is one-sided. Its surface normal vectors point in the positive z-axis direction of its local coordinate space, so it is only visible from that direction by default. To render both sides of a plane, either set the [`isDoubleSided`](scnmaterial/isdoublesided.md) property of its material to [`true`](https://developer.apple.com/documentation/swift/true) or create two plane geometries and orient them back to back.

Control the level of detail with the [`widthSegmentCount`](scnplane/widthsegmentcount.md), [`heightSegmentCount`](scnplane/heightsegmentcount.md), and [`cornerSegmentCount`](scnplane/cornersegmentcount.md) properties. A higher segment count produces more vertices, which can improve rendering quality for certain lighting models or custom shader effects, but at a cost to rendering performance.

## Topics

### Creating a Plane
- [convenience init(width: CGFloat, height: CGFloat)](scnplane/init(width:height:).md)
  Creates a plane geometry with the specified width and height.
### Adjusting a Plane’s Dimensions
- [var width: CGFloat](scnplane/width.md)
  The extent of the plane along its horizontal axis. Animatable.
- [var height: CGFloat](scnplane/height.md)
  The extent of the plane along its vertical axis. Animatable.
### Adjusting Geometric Detail
- [var widthSegmentCount: Int](scnplane/widthsegmentcount.md)
  The number of subdivisions in the plane’s surface along its horizontal axis. Animatable.
- [var heightSegmentCount: Int](scnplane/heightsegmentcount.md)
  The number of subdivisions in the plane’s surface along its vertical axis. Animatable.
### Adding Rounded Corners
- [var cornerRadius: CGFloat](scnplane/cornerradius.md)
  The radius of curvature for the plane’s corners. Animatable.
- [var cornerSegmentCount: Int](scnplane/cornersegmentcount.md)
  The number of line segments used to create each rounded corner of the plane. Animatable.

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
- [class SCNCylinder](scncylinder.md)
  A right circular cylinder geometry.
- [class SCNPyramid](scnpyramid.md)
  A right rectangular pyramid geometry.
- [class SCNSphere](scnsphere.md)
  A sphere (or ball or globe) geometry.
- [class SCNTorus](scntorus.md)
  A torus, or ring-shaped geometry.
- [class SCNTube](scntube.md)
  A tube or pipe geometry—a right circular cylinder with a circular hole along its central axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnplane)*