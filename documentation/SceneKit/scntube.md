# SCNTube

**Framework**: SceneKit  
**Kind**: class  
**Role**: Class

A tube or pipe geometry—a right circular cylinder with a circular hole along its central axis.

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
class SCNTube
```

```objc
@interface SCNTube : SCNGeometry
```

#### Overview

![](https://developer.apple.com/tutorials/images/com.apple.scenekit/media-2929815@2x.png)

The outer surface of a tube is a cylinder. Define the size of the cylinder’s cross section in the x- and z-axis dimensions of its local coordinate space with the [`outerRadius`](./scntube/outerradius.md) property, and its extent in the y-axis dimension with the [`height`](./scntube/height.md) property. A cylinder becomes a tube through the subtraction of a cylindrical volume along its central axis. Define the size of this circular hole using the tube’s [`innerRadius`](./scntube/innerradius.md) property. To position and orient a tube in a scene, attach it to the [`geometry`](./scnnode/geometry.md) property of an [`SCNNode`](./scnnode.md) object.

Control the level of detail with the [`radialSegmentCount`](./scntube/radialsegmentcount.md) and [`heightSegmentCount`](./scntube/heightsegmentcount.md) properties. A higher radial segment count creates a smoother curve for the tube’s circular inner and outer surfaces. A higher segment count in either direction produces more vertices, which can improve rendering quality for certain lighting models or custom shader effects, but at a cost to rendering performance.

A tube contains four [`SCNGeometryElement`](./scngeometryelement.md) objects: one each for its base and top, one that wraps around its outer surface, and one that wraps around its inner surface. SceneKit can render each element using a different material. For details, see the [`materials`](./scngeometry/materials.md) property in [`SCNGeometry`](./scngeometry.md).

## Topics

### Creating a Tube
- [convenience init(innerRadius: CGFloat, outerRadius: CGFloat, height: CGFloat)](./scntube/init%28innerradius,outerradius,height%29.md)
  Creates a tube geometry with the specified inner radius, outer radius, and height.
### Adjusting a Tube’s Dimensions
- [var outerRadius: CGFloat](./scntube/outerradius.md)
  The radius of the tube’s outer circular cross section. Animatable.
- [var innerRadius: CGFloat](./scntube/innerradius.md)
  The radius of the circular hole through the tube. Animatable.
- [var height: CGFloat](./scntube/height.md)
  The extent of the tube along its y-axis. Animatable.
### Adjusting Geometric Detail
- [var radialSegmentCount: Int](./scntube/radialsegmentcount.md)
  The number of subdivisions around the circumference of the tube. Animatable.
- [var heightSegmentCount: Int](./scntube/heightsegmentcount.md)
  The number of subdivisions in the inner and outer surfaces of the tube along its y-axis. Animatable.

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
- [class SCNPlane](./scnplane.md)
  A rectangular, one-sided plane geometry of specified width and height.
- [class SCNPyramid](./scnpyramid.md)
  A right rectangular pyramid geometry.
- [class SCNSphere](./scnsphere.md)
  A sphere (or ball or globe) geometry.
- [class SCNTorus](./scntorus.md)
  A torus, or ring-shaped geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntube)*