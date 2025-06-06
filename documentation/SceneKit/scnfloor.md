# SCNFloor

**Framework**: SceneKit  
**Kind**: class

A plane that can optionally display a reflection of the scene above it.

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
class SCNFloor
```

#### Overview

![None](https://docs-assets.developer.apple.com/published/a6e68c528e0ad20b9b78fb21c14430d8/media-2929804%402x.png)

By default, a floor extends infinitely in the x- and z-axis dimensions of its local coordinate space, and is located in the plane whose y-coordinate is zero. To position and orient a floor in a scene, attach it to the [`geometry`](scnnode/geometry.md) property of an [`SCNNode`](scnnode.md) object. Often, you use a floor to provide a background for a scene.

If a floor’s [`reflectivity`](scnfloor/reflectivity.md) property is greater than zero, SceneKit automatically renders reflections for all geometries above it. Optionally, you can add an opacity gradient so that reflections of scene contents closer to the floor appear more clearly than those of scene contents further from it. You control the floor’s reflectivity using the properties listed in Adding Reflections to a Floor.

## Topics

### Adding Reflections to a Floor
- [var reflectivity: CGFloat](scnfloor/reflectivity.md)
  The intensity of the scene’s reflection on the floor. Animatable.
- [var reflectionFalloffEnd: CGFloat](scnfloor/reflectionfalloffend.md)
  The distance from the floor at which scene contents are no longer reflected. Animatable.
- [var reflectionFalloffStart: CGFloat](scnfloor/reflectionfalloffstart.md)
  The distance from the floor at which scene contents are reflected at full intensity. Animatable.
- [var reflectionResolutionScaleFactor: CGFloat](scnfloor/reflectionresolutionscalefactor.md)
  The resolution scale factor of the offscreen buffer that SceneKit uses to render reflections.
- [var reflectionCategoryBitMask: Int](scnfloor/reflectioncategorybitmask.md)
  A mask that defines which categories of other objects show reflections on the floor.
### Adjusting a Floor’s Size
- [var width: CGFloat](scnfloor/width.md)
  The extent of the floor along its x-axis. Animatable.
- [var length: CGFloat](scnfloor/length.md)
  The extent of the floor along its z-axis. Animatable.

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
- [class SCNTorus](scntorus.md)
  A torus, or ring-shaped geometry.
- [class SCNTube](scntube.md)
  A tube or pipe geometry—a right circular cylinder with a circular hole along its central axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnfloor)*