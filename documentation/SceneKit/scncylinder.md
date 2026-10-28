# SCNCylinder

**Framework**: SceneKit  
**Kind**: class  
**Role**: Class

A right circular cylinder geometry.

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
class SCNCylinder
```

```objc
@interface SCNCylinder : SCNGeometry
```

## Overview

![](https://developer.apple.com/tutorials/images/com.apple.scenekit/media-2929812@2x.png)

A cylinder defines the surface of a solid whose every cross section along a linear axis is a circle of equal size. Define the size of the cylinder’s cross section in the x- and z-axis dimensions of its local coordinate space with the [`radius`](./scncylinder/radius.md) property, and its extent in the y-axis dimension with the [`height`](./scncylinder/height.md) property. To position and orient a cylinder in a scene, attach it to the [`geometry`](./scnnode/geometry.md) property of an [`SCNNode`](./scnnode.md) object.

Control the level of detail with the [`radialSegmentCount`](./scncylinder/radialsegmentcount.md) and [`heightSegmentCount`](./scncylinder/heightsegmentcount.md) properties. A higher radial segment count creates a smoother curve for the cylinder’s circular sides. A higher segment count in either direction produces more vertices, which can improve rendering quality for certain lighting models or custom shader effects, but at a cost to rendering performance.

A cylinder contains three [`SCNGeometryElement`](./scngeometryelement.md) objects: one each for its base and top, and one that wraps around its sides. SceneKit can render each element using a different material. For details, see the [`materials`](./scngeometry/materials.md) property in [`SCNGeometry`](./scngeometry.md).

## Topics

### Creating a Cylinder
- [convenience init(radius: CGFloat, height: CGFloat)](./scncylinder/init%28radius,height%29.md)
  Creates a cylinder geometry with the specified radius and height.
### Adjusting a Cylinder’s Dimensions
- [var radius: CGFloat](./scncylinder/radius.md)
  The radius of the cylinder’s circular cross section. Animatable.
- [var height: CGFloat](./scncylinder/height.md)
  The extent of the cylinder along its y-axis. Animatable.
### Adjusting Geometric Detail
- [var radialSegmentCount: Int](./scncylinder/radialsegmentcount.md)
  The number of subdivisions around the circumference of the cylinder. Animatable.
- [var heightSegmentCount: Int](./scncylinder/heightsegmentcount.md)
  The number of subdivisions in the sides of the cylinder along its y-axis. Animatable.

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
- [class SCNPlane](./scnplane.md)
  A rectangular, one-sided plane geometry of specified width and height.
- [class SCNPyramid](./scnpyramid.md)
  A right rectangular pyramid geometry.
- [class SCNSphere](./scnsphere.md)
  A sphere (or ball or globe) geometry.
- [class SCNTorus](./scntorus.md)
  A torus, or ring-shaped geometry.
- [class SCNTube](./scntube.md)
  A tube or pipe geometry—a right circular cylinder with a circular hole along its central axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncylinder)*