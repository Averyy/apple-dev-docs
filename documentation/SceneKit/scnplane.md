# SCNPlane

**Framework**: SceneKit  
**Kind**: class  
**Role**: Class

A rectangular, one-sided plane geometry of specified width and height.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
class SCNPlane
```

```objc
@interface SCNPlane : SCNGeometry
```

#### Overview

![](https://developer.apple.com/tutorials/images/com.apple.scenekit/media-2929811@2x.png)

A plane defines a flat surface in the x- and y-axis dimensions of its local coordinate space according to its [`width`](./scnplane/width.md) and [`height`](./scnplane/height.md) properties. To orient a plane differently, adjust the [`transform`](./scnnode/transform.md) property of the node containing the plane geometry. You can create a rounded rectangular plane using the [`cornerRadius`](./scnplane/cornerradius.md) property.

The surface is one-sided. Its surface normal vectors point in the positive z-axis direction of its local coordinate space, so it is only visible from that direction by default. To render both sides of a plane, either set the [`isDoubleSided`](./scnmaterial/isdoublesided.md) property of its material to [`true`](../Swift/true.md) or create two plane geometries and orient them back to back.

Control the level of detail with the [`widthSegmentCount`](./scnplane/widthsegmentcount.md), [`heightSegmentCount`](./scnplane/heightsegmentcount.md), and [`cornerSegmentCount`](./scnplane/cornersegmentcount.md) properties. A higher segment count produces more vertices, which can improve rendering quality for certain lighting models or custom shader effects, but at a cost to rendering performance.

## Topics

### Creating a Plane
- [convenience init(width: CGFloat, height: CGFloat)](./scnplane/init%28width,height%29.md)
  Creates a plane geometry with the specified width and height.
### Adjusting a Plane’s Dimensions
- [var width: CGFloat](./scnplane/width.md)
  The extent of the plane along its horizontal axis. Animatable.
- [var height: CGFloat](./scnplane/height.md)
  The extent of the plane along its vertical axis. Animatable.
### Adjusting Geometric Detail
- [var widthSegmentCount: Int](./scnplane/widthsegmentcount.md)
  The number of subdivisions in the plane’s surface along its horizontal axis. Animatable.
- [var heightSegmentCount: Int](./scnplane/heightsegmentcount.md)
  The number of subdivisions in the plane’s surface along its vertical axis. Animatable.
### Adding Rounded Corners
- [var cornerRadius: CGFloat](./scnplane/cornerradius.md)
  The radius of curvature for the plane’s corners. Animatable.
- [var cornerSegmentCount: Int](./scnplane/cornersegmentcount.md)
  The number of line segments used to create each rounded corner of the plane. Animatable.

## Relationships

### Inherits From
- [SCNGeometry](./scngeometry.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [SCNAnimatable](./scnanimatable.md)
- [SCNBoundingVolume](./scnboundingvolume.md)
- [SCNShadable](./scnshadable.md)

## See Also

### Basic Shapes
- [class SCNFloor](./scnfloor.md)
  A plane that can optionally display a reflection of the scene above it.
- [class SCNBox](./scnbox.md)
  A six-sided polyhedron geometry whose faces are all rectangles, optionally with rounded edges and corners.
- [class SCNCapsule](./scncapsule.md)
  A right circular cylinder geometry whose ends are capped with hemispheres.
- [class SCNCone](./scncone.md)
  A right circular cone or frustum geometry.
- [class SCNCylinder](./scncylinder.md)
  A right circular cylinder geometry.
- [class SCNPyramid](./scnpyramid.md)
  A right rectangular pyramid geometry.
- [class SCNSphere](./scnsphere.md)
  A sphere (or ball or globe) geometry.
- [class SCNTorus](./scntorus.md)
  A torus, or ring-shaped geometry.
- [class SCNTube](./scntube.md)
  A tube or pipe geometry—a right circular cylinder with a circular hole along its central axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnplane)*