# SCNTorus

**Framework**: SceneKit  
**Kind**: class

A torus, or ring-shaped geometry.

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
class SCNTorus
```

#### Overview

![None](https://docs-assets.developer.apple.com/published/efa6172dd2b7015ddd7ccb23e381513b/media-2929816%402x.png)

A torus is mathematically defined as a surface of revolution formed by revolving a circle around a coplanar axis. It is the product of two circles: a large ring and a pipe that encircles the ring. SceneKit uses these terms to define the dimensions of a torus geometry in its local coordinate space. The torus’ [`ringRadius`](scntorus/ringradius.md) property defines a circle in the x- and z-axis dimensions, centered at the origin, and its [`pipeRadius`](scntorus/piperadius.md) property defines the width of the surface encircling the ring. To change the orientation of a torus, adjust the [`transform`](scnnode/transform.md) property of the node containing the torus geometry.

Control the level of detail with the [`ringSegmentCount`](scntorus/ringsegmentcount.md) and [`pipeSegmentCount`](scntorus/pipesegmentcount.md) properties. Higher segment counts produce more vertices and a more smoothly curved surface, which can improve rendering quality at a cost to rendering performance.

## Topics

### Creating a Torus
- [convenience init(ringRadius: CGFloat, pipeRadius: CGFloat)](scntorus/init(ringradius:piperadius:).md)
  Creates a torus geometry with the specified ring radius and pipe radius.
### Adjusting a Torus’ Dimensions
- [var ringRadius: CGFloat](scntorus/ringradius.md)
  The major radius of the torus, defining a circle in the x- and z-axis dimensions. Animatable.
- [var pipeRadius: CGFloat](scntorus/piperadius.md)
  The minor radius of the torus, defining the pipe that encircles the torus ring. Animatable.
### Configuring Torus Properties
- [var ringSegmentCount: Int](scntorus/ringsegmentcount.md)
  The number of subdivisions around the torus ring. Animatable.
- [var pipeSegmentCount: Int](scntorus/pipesegmentcount.md)
  The number of subdivisions around the torus pipe. Animatable.

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
- [class SCNPyramid](scnpyramid.md)
  A right rectangular pyramid geometry.
- [class SCNSphere](scnsphere.md)
  A sphere (or ball or globe) geometry.
- [class SCNTube](scntube.md)
  A tube or pipe geometry—a right circular cylinder with a circular hole along its central axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntorus)*