# MeshResource

**Framework**: RealityKit  
**Kind**: class

A high-level representation of a collection of vertices and edges that define a shape.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency class MeshResource
```

## Mentions

- [Adding procedural assets to a scene](adding-procedural-assets-to-a-scene.md)
- [Creating a plane with low-level mesh](creating-a-plane-with-low-level-mesh.md)
- [Reducing CPU Utilization in Your RealityKit App](reducing-cpu-utilization-in-your-realitykit-app.md)

## Topics

### Creating a low level resource
- [var lowLevelMesh: LowLevelMesh?](meshresource/lowlevelmesh.md)
  The low-level mesh that this mesh is built from, if any.
### Configuring the resource
- [var expectedMaterialCount: Int](meshresource/expectedmaterialcount.md)
  The number of material entries required to render the mesh resource.
- [func replaceAsync(with: MeshResource.Contents) -> LoadRequest<MeshResource>](meshresource/replaceasync(with:).md)
  Replace the contents of this mesh resource asynchronously.
### Accessing resource data
- [var contents: MeshResource.Contents](meshresource/contents-swift.property.md)
  Get the contents of the mesh asset.
### Getting a bounding box
- [var bounds: BoundingBox](meshresource/bounds.md)
  A box that bounds the mesh.
### Creating a box
- [static func generateBox(size: Float, cornerRadius: Float) -> MeshResource](meshresource/generatebox(size:cornerradius:)-8em0v.md)
  Creates a box mesh from a length for the box’s width, height, and depth, and a radius for the corners.
- [static func generateBox(size: SIMD3<Float>, cornerRadius: Float) -> MeshResource](meshresource/generatebox(size:cornerradius:)-2ovma.md)
  Creates a box mesh from a vector of three scalar values that represent width, height, and depth, respectively, and a radius for the corners.
- [static func generateBox(width: Float, height: Float, depth: Float, cornerRadius: Float, splitFaces: Bool) -> MeshResource](meshresource/generatebox(width:height:depth:cornerradius:splitfaces:).md)
  Creates a box mesh from a width, height, depth, a radius for the corners, and a Boolean option that splits faces.
- [static func generateBox(size: SIMD3<Float>, majorCornerRadius: Float, minorCornerRadius: Float) -> MeshResource](meshresource/generatebox(size:majorcornerradius:minorcornerradius:).md)
  Creates a box mesh from a vector of three scalar values that represent width, height, and depth, respectively, and radii for the corners.
### Creating a plane
- [static func generatePlane(width: Float, height: Float, cornerRadius: Float) -> MeshResource](meshresource/generateplane(width:height:cornerradius:).md)
  Creates a new rectangle mesh with the specified dimensions in the entity’s xy-plane.
- [static func generatePlane(width: Float, depth: Float, cornerRadius: Float) -> MeshResource](meshresource/generateplane(width:depth:cornerradius:).md)
  Creates a new rectangle mesh with the specified dimensions in the entity’s xz-plane.
### Creating a primitive shape
- [static func generateSphere(radius: Float) -> MeshResource](meshresource/generatesphere(radius:).md)
  Creates a new sphere mesh with the specified radius.
- [static func generateCone(height: Float, radius: Float) -> MeshResource](meshresource/generatecone(height:radius:).md)
  Creates a new cone mesh with the specified dimensions.
- [static func generateCylinder(height: Float, radius: Float) -> MeshResource](meshresource/generatecylinder(height:radius:).md)
  Creates a new cylinder mesh with the specified dimensions.
### Structures
- [MeshResource.Contents](meshresource/contents-swift.struct.md)
  Value of the contents of the resource.
- [MeshResource.GenerateTextOptions](meshresource/generatetextoptions.md)
  A type that determines the configuration for rendering text in 2D, before it is extruded.
- [MeshResource.Instance](meshresource/instance.md)
  An object that transforms a model to a location.
- [MeshResource.JointInfluences](meshresource/jointinfluences.md)
  A buffer of vertex-joint influences which bind the mesh part’s vertices to a skeleton via a skinning deformation.
- [MeshResource.Model](meshresource/model.md)
  A model consists of a list of parts.
- [MeshResource.Part](meshresource/part.md)
  A part of a model consisting of a single material.
- [MeshResource.ShapeExtrusionOptions](meshresource/shapeextrusionoptions.md)
  A type that determines the extrusion, chamfering, and material assignment of an extruded shape.
- [MeshResource.Skeleton](meshresource/skeleton.md)
  A skeleton consists of a hierarchy of joints. Each joint defines a coordinate space. Portions of a model may be thought of as having a position in a joint’s local space.
### Initializers
- [convenience(extruding:extrusionOptions:)](meshresource/init(extruding:extrusionoptions:).md)
  Synchronously generates a 3D mesh by extruding a 2D path.
- [convenience(extruding:textOptions:extrusionOptions:)](meshresource/init(extruding:textoptions:extrusionoptions:).md)
  Synchronously generates a 3D mesh from a string, with options for text layout and custom extrusions.
- [convenience(from:)](meshresource/init(from:).md)
  Asynchronously creates a mesh resource from a low-level mesh.
- [convenience(shape:)](meshresource/init(shape:).md)
  Generates a MeshResource from a ShapeResource.
### Instance Methods
- [func meshPartIndex(modelID: String, partID: String) -> Int?](meshresource/meshpartindex(modelid:partid:).md)
  Get the mesh part index for a given model and part identifier.
- [func replace(with:)](meshresource/replace(with:).md)
  Replace the contents of this mesh resource.
### Type Aliases
- [MeshResource.Font](meshresource/font.md)
  A platform-specific type that represents a font for use in generating a text mesh.
### Type Methods
- [static generate(from:)](meshresource/generate(from:).md)
  Create a mesh resource from contents.
- [static generateAsync(from:)](meshresource/generateasync(from:).md)
  Create a mesh resource from contents asynchronously.
- [static generateBox(size:cornerRadius:)](meshresource/generatebox(size:cornerradius:).md)
  Creates a box mesh from a length for the box’s width, height, and depth, and a radius for the corners.
- [static generateText(_:extrusionDepth:font:containerFrame:alignment:lineBreakMode:)](meshresource/generatetext(_:extrusiondepth:font:containerframe:alignment:linebreakmode:).md)
  Generates a 3D mesh for rendering static text.

## Relationships

### Conforms To
- [Resource](resource.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct ModelComponent](modelcomponent.md)
  A component that contains a mesh and materials for the visual appearance of an entity.
- [class ModelEntity](modelentity.md)
  A representation of a physical object that RealityKit renders and optionally simulates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource)*