# SCNGeometry

**Framework**: SceneKit  
**Kind**: class

A three-dimensional shape (also called a model or mesh) that can be displayed in a scene, with attached materials that define its appearance.

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
class SCNGeometry
```

#### Overview

In SceneKit, geometries attached to [`SCNNode`](scnnode.md) objects form the visible elements of a scene, and [`SCNMaterial`](scnmaterial.md) objects attached to a geometry determine its appearance.

##### Working with Geometry Objects

You control a geometry’s appearance in a scene with nodes and materials. A geometry object provides only the form of a visible object rendered by SceneKit. You specify color and texture for a geometry’s surface, control how it responds to light, and add special effects by attaching materials (for details, see the methods in Managing a Geometry’s Materials). You position and orient a geometry in a scene by attaching it to an [`SCNNode`](scnnode.md) object. Multiple nodes can reference the same geometry object, allowing it to appear at different positions in a scene.

You can easily copy geometries and change their materials. A geometry object manages the association between immutable vertex data and a mutable assignment of materials. To make a geometry appear more than once in the same scene with a different set of materials, use its inherited [`copy()`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/copy()) method. The copy shares the underlying vertex data of the original, but can be assigned materials independently. You can thus make many copies of a geometry without incurring a significant cost to rendering performance.

You can animate a geometry object. The vertex data associated with a geometry is immutable, but SceneKit provides several ways to animate geometry. You can use a [`SCNMorpher`](scnmorpher.md) or [`SCNSkinner`](scnskinner.md) object to deform a geometry’s surface, or run animations created in an external 3D authoring tool and loaded from a scene file. You can also use methods in the [`SCNShadable`](scnshadable.md) protocol to add custom GLSL shader programs that alter SceneKit’s rendering of a geometry.

##### Obtaining a Geometry Object

SceneKit provides several ways to introduce geometry objects to your app:

| Action | For further information |
| --- | --- |
| Load from a scene file created using external 3D authoring tools | [`SCNScene`](scnscene.md), [`SCNSceneSource`](scnscenesource.md) |
| Use and customize SceneKit’s built-in primitive shapes | [`SCNPlane`](scnplane.md), [`SCNBox`](scnbox.md), [`SCNSphere`](scnsphere.md), [`SCNPyramid`](scnpyramid.md), [`SCNCone`](scncone.md), [`SCNCylinder`](scncylinder.md), [`SCNCapsule`](scncapsule.md), [`SCNTube`](scntube.md), and [`SCNTorus`](scntorus.md) |
| Create 3D geometry from 2D text or Bézier curves | [`SCNText`](scntext.md), [`SCNShape`](scnshape.md) |
| Create a custom geometry from vertex data | [`SCNGeometrySource`](scngeometrysource.md), [`SCNGeometryElement`](scngeometryelement.md), [`init(sources:elements:)`](scngeometry/init(sources:elements:).md), Managing Geometry Data |

## Topics

### Creating a Geometry Object
- [convenience init(sources: [SCNGeometrySource], elements: [SCNGeometryElement]?)](scngeometry/init(sources:elements:).md)
  Creates a new geometry built from the specified geometry sources and elements.
### Managing Geometry Attributes
- [var name: String?](scngeometry/name.md)
  A name associated with the geometry object.
- [protocol SCNBoundingVolume](scnboundingvolume.md)
  Methods common to the [`SCNNode`](scnnode.md) and [`SCNGeometry`](scngeometry.md) classes for measuring location and size.
### Managing a Geometry’s Materials
- [var materials: [SCNMaterial]](scngeometry/materials.md)
  An array of [`SCNMaterial`](scnmaterial.md) objects that determine the geometry’s appearance when rendered.
- [var firstMaterial: SCNMaterial?](scngeometry/firstmaterial.md)
  The first material attached to the geometry.
- [func material(named: String) -> SCNMaterial?](scngeometry/material(named:).md)
  Returns the first material attached to the geometry with the specified name.
- [func insertMaterial(SCNMaterial, at: Int)](scngeometry/insertmaterial(_:at:).md)
  Attaches a material to the geometry at the specified index.
- [func removeMaterial(at: Int)](scngeometry/removematerial(at:).md)
  Removes a material attached to the geometry.
- [func replaceMaterial(at: Int, with: SCNMaterial)](scngeometry/replacematerial(at:with:).md)
  Replaces a material attached to the geometry with another.
### Managing Geometry Data
- [var elements: [SCNGeometryElement]](scngeometry/elements.md)
  An array of geometry elements that describe the geometry’s shape.
- [var sources: [SCNGeometrySource]](scngeometry/sources.md)
  An array of geometry sources that provide vertex data for the geometry.
- [var elementCount: Int](scngeometry/elementcount.md)
  The number of geometry elements in the geometry.
- [func element(at: Int) -> SCNGeometryElement](scngeometry/element(at:).md)
  Returns the geometry element at a specified index.
- [func sources(for: SCNGeometrySource.Semantic) -> [SCNGeometrySource]](scngeometry/sources(for:).md)
  Returns the geometry sources for a specified semantic.
### Optimizing Level of Detail
- [var levelsOfDetail: [SCNLevelOfDetail]?](scngeometry/levelsofdetail.md)
  An array of [`SCNLevelOfDetail`](scnlevelofdetail.md) objects for managing the geometry’s appearance when viewed from far away.
- [class SCNLevelOfDetail](scnlevelofdetail.md)
  An alternate resolution for a geometry that SceneKit automatically substitutes to improve rendering performance.
### Smoothing and Subdividing Geometry
- [var subdivisionLevel: Int](scngeometry/subdivisionlevel.md)
  The number of subdivisions SceneKit uses to smooth the geometry’s surface at render time.
- [var edgeCreasesElement: SCNGeometryElement?](scngeometry/edgecreaseselement.md)
  The geometry element identifying which edges of the geometry’s surface should remain sharp after subdivision.
- [var edgeCreasesSource: SCNGeometrySource?](scngeometry/edgecreasessource.md)
  The geometry source specifying the smoothness or sharpness of edges after surface subdivision.
- [var wantsAdaptiveSubdivision: Bool](scngeometry/wantsadaptivesubdivision.md)
### Managing Tessellation
- [var tessellator: SCNGeometryTessellator?](scngeometry/tessellator.md)
- [class SCNGeometryTessellator](scngeometrytessellator.md)
### Initializers
- [convenience init(sources: [SCNGeometrySource], elements: [SCNGeometryElement]?, sourceChannels: [NSNumber]?)](scngeometry/init(sources:elements:sourcechannels:).md)
### Instance Properties
- [var geometrySourceChannels: [NSNumber]?](scngeometry/geometrysourcechannels.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [SCNBox](scnbox.md)
- [SCNCapsule](scncapsule.md)
- [SCNCone](scncone.md)
- [SCNCylinder](scncylinder.md)
- [SCNFloor](scnfloor.md)
- [SCNPlane](scnplane.md)
- [SCNPyramid](scnpyramid.md)
- [SCNShape](scnshape.md)
- [SCNSphere](scnsphere.md)
- [SCNText](scntext.md)
- [SCNTorus](scntorus.md)
- [SCNTube](scntube.md)
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

- [class SCNGeometrySource](scngeometrysource.md)
  A container for vertex data forming part of the definition for a three-dimensional object, or geometry.
- [class SCNGeometryElement](scngeometryelement.md)
  A container for index data describing how vertices connect to define a three-dimensional object, or geometry.
- [Built-in Geometry Types](built-in-geometry-types.md)
  Basic shapes—such as spheres, boxes, and planes—and features for generating 3D objects from 2D text and Bézier curves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometry)*