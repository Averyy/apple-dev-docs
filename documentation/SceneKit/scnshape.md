# SCNShape

**Framework**: SceneKit  
**Kind**: class

A geometry based on a two-dimensional path, optionally extruded to create a three-dimensional object.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class SCNShape
```

#### Overview

SceneKit creates a three-dimensional geometry by extruding a Bézier path, which extends in the x- and y-axis directions of its local coordinate space, along the z-axis by a specified amount. For example, if you create a shape with an extrusion depth of `1.0`, it extends from `-0.5` to `0.5` along the z-axis. An extrusion depth of zero creates a flat, one-sided shape—the geometry is confined to the plane whose z-coordinate is `0.0`, and viewable only from its front unless its material’s [`isDoubleSided`](scnmaterial/isdoublesided.md) property is [`true`](https://developer.apple.com/documentation/swift/true).

A shape geometry may contain between one and five geometry elements:

- If its [`extrusionDepth`](scnshape/extrusiondepth.md) property is `0.0`, the shape geometry has one element corresponding to its one visible side.
- If its extrusion depth is greater than zero and its [`chamferRadius`](scnshape/chamferradius.md) property is `0.0`, the shape geometry has three elements, corresponding to its front, back, and extruded sides.
- If both extrusion depth and chamfer radius are greater than zero, the text geometry can have four or five elements depending on its [`chamferMode`](scnshape/chamfermode.md) property, corresponding to its front, back, extruded sides, front chamfer, and back chamfer.

SceneKit can render each element using a different material. For details, see the description of the [`materials`](scngeometry/materials.md) property in [`SCNGeometry`](scngeometry.md).

## Topics

### Creating a Shape
- [convenience init(path: UIBezierPath?, extrusionDepth: CGFloat)](scnshape/init(path:extrusiondepth:).md)
  Creates a shape geometry with the specified path and extrusion depth.
### Modifying a Shape
- [var extrusionDepth: CGFloat](scnshape/extrusiondepth.md)
  The thickness of the extruded shape along the z-axis. Animatable.
- [var path: UIBezierPath?](scnshape/path.md)
  The two-dimensional path forming the basis of the shape.
### Chamfering a Shape
- [var chamferMode: SCNChamferMode](scnshape/chamfermode.md)
  A constant specifying which ends of the extruded shape’s profile are chamfered.
- [enum SCNChamferMode](scnchamfermode.md)
  Options for which edges of an extruded shape are chamfered, used by the [`chamferMode`](scnshape/chamfermode.md) property.
- [var chamferProfile: UIBezierPath?](scnshape/chamferprofile.md)
  A path that determines the cross-sectional contour of each chamfered edge.
- [var chamferRadius: CGFloat](scnshape/chamferradius.md)
  The width or depth of each chamfered edge. Animatable.

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

- [class SCNText](scntext.md)
  A geometry based on a string of text, optionally extruded to create a three-dimensional object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnshape)*