# SCNPyramid

**Framework**: SceneKit  
**Kind**: class

A right rectangular pyramid geometry.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class SCNPyramid
```

#### Overview

![None](https://docs-assets.developer.apple.com/published/faa953ca36abc955499e04ebcf672469/media-2929810%402x.png)

A pyramid defines the surface of a solid whose base is a rectangle, and whose four triangular side faces converge at a point centered above its base. Define the shape of the pyramid’s base in the x- and z-axis dimensions of its local coordinate space with the [`width`](scnpyramid/width.md) and [`length`](scnpyramid/length.md) properties, and its extent in the y-axis dimension with the [`height`](scnpyramid/height.md) property. To position and orient a pyramid in a scene, attach it to the [`geometry`](scnnode/geometry.md) property of an [`SCNNode`](scnnode.md) object.

Control the level of detail with the [`widthSegmentCount`](scnpyramid/widthsegmentcount.md), [`lengthSegmentCount`](scnpyramid/lengthsegmentcount.md), and [`heightSegmentCount`](scnpyramid/heightsegmentcount.md) properties. A higher segment count produces more vertices, which can improve rendering quality for certain lighting models or custom shader effects, but at a cost to rendering performance.

A pyramid contains five [`SCNGeometryElement`](scngeometryelement.md) objects, corresponding to its base and each of its four sides. SceneKit can render each element using a different material. For details, see the [`materials`](scngeometry/materials.md) property in [`SCNGeometry`](scngeometry.md).

## Topics

### Creating a Pyramid
- [convenience init(width: CGFloat, height: CGFloat, length: CGFloat)](scnpyramid/init(width:height:length:).md)
  Creates a pyramid geometry with the specified width, height, and length.
### Adjusting a Pyramid’s Dimensions
- [var width: CGFloat](scnpyramid/width.md)
  The extent of the pyramid along its x-axis. Animatable.
- [var height: CGFloat](scnpyramid/height.md)
  The extent of the pyramid along its y-axis. Animatable.
- [var length: CGFloat](scnpyramid/length.md)
  The extent of the pyramid along its z-axis. Animatable.
### Adjusting Geometric Detail
- [var widthSegmentCount: Int](scnpyramid/widthsegmentcount.md)
  The number of subdivisions in each face of the pyramid along its x-axis. Animatable.
- [var heightSegmentCount: Int](scnpyramid/heightsegmentcount.md)
  The number of subdivisions in each face of the pyramid along its y-axis. Animatable.
- [var lengthSegmentCount: Int](scnpyramid/lengthsegmentcount.md)
  The number of subdivisions in each face of the pyramid along its z-axis. Animatable.

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
- [class SCNPlane](scnplane.md)
  A rectangular, one-sided plane geometry of specified width and height.
- [class SCNSphere](scnsphere.md)
  A sphere (or ball or globe) geometry.
- [class SCNTorus](scntorus.md)
  A torus, or ring-shaped geometry.
- [class SCNTube](scntube.md)
  A tube or pipe geometry—a right circular cylinder with a circular hole along its central axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnpyramid)*