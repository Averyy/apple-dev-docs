# SCNGeometryElement

**Framework**: SceneKit  
**Kind**: class

A container for index data describing how vertices connect to define a three-dimensional object, or geometry.

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
class SCNGeometryElement
```

#### Overview

You use geometry elements together with [`SCNGeometrySource`](scngeometrysource.md) objects to define custom [`SCNGeometry`](scngeometry.md) objects or to inspect the data that composes an existing geometry. You create a custom geometry using a three-step process:

1. Create one or more [`SCNGeometrySource`](scngeometrysource.md) objects, each of which defines per-vertex information such as position, surface normal, or texture coordinates for all vertices in the geometry.
2. Create at least one [`SCNGeometryElement`](scngeometryelement.md) object, containing an array of indices identifying vertices in the geometry sources and describing the drawing primitive that SceneKit uses to connect the vertices when rendering the geometry.
3. Create an [`SCNGeometry`](scngeometry.md) instance from the geometry sources and geometry elements.

When SceneKit renders a geometry, each geometry element corresponds to a drawing command sent to the GPU. Because different rendering states require separate drawing commands, you can define a geometry using multiple geometry elements. For example, the teapot geometry shown below has four geometry elements, so you can assign up to four [`SCNMaterial`](scnmaterial.md) objects in order to render each element with a different appearance. But because each drawing command incurs a CPU time overhead when rendering, minimizing the number of elements in a custom geometry can improve rendering performance.

![None](https://docs-assets.developer.apple.com/published/4cd3b44ccbea79bf52cb77c6d99edcff/media-2929778%402x.png)

## Topics

### Creating a Geometry Element
- [convenience init<IndexType>(indices: [IndexType], primitiveType: SCNGeometryPrimitiveType)](scngeometryelement/init(indices:primitivetype:).md)
  Creates a geometry element from the specified array of index values.
- [convenience init(data: Data?, primitiveType: SCNGeometryPrimitiveType, primitiveCount: Int, bytesPerIndex: Int)](scngeometryelement/init(data:primitivetype:primitivecount:bytesperindex:).md)
  Creates a geometry element from the specified data and options.
### Working with Indexes
- [var data: Data](scngeometryelement/data.md)
  The data describing the geometry element.
- [var bytesPerIndex: Int](scngeometryelement/bytesperindex.md)
  The number of bytes that represent each index value in the element’s data.
- [var primitiveType: SCNGeometryPrimitiveType](scngeometryelement/primitivetype.md)
  The drawing primitive that connects vertices when rendering the geometry element.
- [enum SCNGeometryPrimitiveType](scngeometryprimitivetype.md)
  The drawing primitive that connects vertices when rendering a geometry element, used by the [`primitiveType`](scngeometryelement/primitivetype.md) property to specify how SceneKit interprets the geometry element’s data.
- [var primitiveCount: Int](scngeometryelement/primitivecount.md)
  The number of primitives in the element.
- [var primitiveRange: NSRange](scngeometryelement/primitiverange.md)
  The range of primitives from the geometry element to render.
### Rendering Point Clouds
- [var pointSize: CGFloat](scngeometryelement/pointsize.md)
  The width of each point in the geometry element, as measured in the geometry’s local 3D coordinate space.
- [var minimumPointScreenSpaceRadius: CGFloat](scngeometryelement/minimumpointscreenspaceradius.md)
  The smallest radius, measured in screen points, at which to render any point in the geometry element.
- [var maximumPointScreenSpaceRadius: CGFloat](scngeometryelement/maximumpointscreenspaceradius.md)
  The largest radius, measured in screen points, at which to render any point in the geometry element.
### Initializers
- [convenience init(buffer: any MTLBuffer, primitiveType: SCNGeometryPrimitiveType, primitiveCount: Int, bytesPerIndex: Int)](scngeometryelement/init(buffer:primitivetype:primitivecount:bytesperindex:).md)
- [convenience init(buffer: any MTLBuffer, primitiveType: SCNGeometryPrimitiveType, primitiveCount: Int, indicesChannelCount: Int, interleavedIndicesChannels: Bool, bytesPerIndex: Int)](scngeometryelement/init(buffer:primitivetype:primitivecount:indiceschannelcount:interleavedindiceschannels:bytesperindex:).md)
- [convenience init(data: Data?, primitiveType: SCNGeometryPrimitiveType, primitiveCount: Int, indicesChannelCount: Int, interleavedIndicesChannels: Bool, bytesPerIndex: Int)](scngeometryelement/init(data:primitivetype:primitivecount:indiceschannelcount:interleavedindiceschannels:bytesperindex:).md)
### Instance Properties
- [var hasInterleavedIndicesChannels: Bool](scngeometryelement/hasinterleavedindiceschannels.md)
- [var indicesChannelCount: Int](scngeometryelement/indiceschannelcount.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class SCNGeometry](scngeometry.md)
  A three-dimensional shape (also called a model or mesh) that can be displayed in a scene, with attached materials that define its appearance.
- [class SCNGeometrySource](scngeometrysource.md)
  A container for vertex data forming part of the definition for a three-dimensional object, or geometry.
- [Built-in Geometry Types](built-in-geometry-types.md)
  Basic shapes—such as spheres, boxes, and planes—and features for generating 3D objects from 2D text and Bézier curves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometryelement)*