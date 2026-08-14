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

- [Creating a plane with low-level mesh](creating-a-plane-with-low-level-mesh.md)
- [Reducing CPU Utilization in Your RealityKit App](reducing-cpu-utilization-in-your-realitykit-app.md)

#### Overview

Use [`MeshResource`](meshresource.md) to create procedural geometry from built-in primitives like boxes, spheres, planes, and cylinders, or from custom mesh data. Assign a mesh resource to an entity’s [`ModelComponent`](modelcomponent.md) alongside an array of [`Material`](material.md) instances to render the shape in a scene.

Check [`expectedMaterialCount`](meshresource/expectedmaterialcount.md) to determine how many materials the mesh requires.

## Topics

### Creating a mesh resource
- [static func generate(from: MeshResource.Contents) throws -> MeshResource](meshresource/generate(from:)-4aahn.md)
  Create a mesh resource from contents.
- [static func generate(from: MeshResource.Contents) throws -> MeshResource](meshresource/generate(from:)-4aahn.md)
  Create a mesh resource from contents.
- [convenience init(from: LowLevelMesh) async throws](meshresource/init(from:)-1i7c9.md)
  Asynchronously creates a mesh resource from a low-level mesh.
- [convenience init(from: LowLevelMesh) async throws](meshresource/init(from:)-1i7c9.md)
  Asynchronously creates a mesh resource from a low-level mesh.
- [convenience init(shape: ShapeResource)](meshresource/init(shape:)-3rtda.md)
  Generates a MeshResource from a ShapeResource.
- [convenience init(shape: ShapeResource)](meshresource/init(shape:)-3rtda.md)
  Generates a MeshResource from a ShapeResource.
- [static func generateAsync(from: MeshResource.Contents) -> LoadRequest<MeshResource>](meshresource/generateasync(from:)-1n2vv.md)
  Create a mesh resource from contents asynchronously.
- [static func generateAsync(from: MeshResource.Contents) -> LoadRequest<MeshResource>](meshresource/generateasync(from:)-1n2vv.md)
  Create a mesh resource from contents asynchronously.
### Creating a low level resource
- [convenience init(from: LowLevelMesh) async throws](meshresource/init(from:)-1i7c9.md)
  Asynchronously creates a mesh resource from a low-level mesh.
- [convenience init(from: LowLevelMesh) async throws](meshresource/init(from:)-1i7c9.md)
  Asynchronously creates a mesh resource from a low-level mesh.
- [var lowLevelMesh: LowLevelMesh?](meshresource/lowlevelmesh.md)
  The low-level mesh that this mesh is built from, if any.
### Configuring the resource
- [var expectedMaterialCount: Int](meshresource/expectedmaterialcount.md)
  The number of material entries required to render the mesh resource.
- [func replace(with: MeshResource.Contents) throws](meshresource/replace(with:)-g0kn.md)
  Replace the contents of this mesh resource.
- [func replace(with: MeshResource.Contents) throws](meshresource/replace(with:)-g0kn.md)
  Replace the contents of this mesh resource.
- [func replaceAsync(with: MeshResource.Contents) -> LoadRequest<MeshResource>](meshresource/replaceasync(with:).md)
  Replace the contents of this mesh resource asynchronously.
### Accessing resource data
- [var contents: MeshResource.Contents](meshresource/contents-swift.property.md)
  Get the contents of the mesh asset.
### Getting a bounding box
- [var bounds: BoundingBox](meshresource/bounds.md)
  A box that bounds the mesh in local coordinate space.
### Creating a box
- [static func generateBox(size: Float, cornerRadius: Float) -> MeshResource](meshresource/generatebox(size:cornerradius:)-8em0v.md)
  Creates a box mesh from a length for the box’s width, height, and depth, and a radius for the corners.
- [static func generateBox(size: SIMD3<Float>, cornerRadius: Float) -> MeshResource](meshresource/generatebox(size:cornerradius:)-2ovma.md)
  Creates a box mesh from a vector of three scalar values that represent width, height, and depth, respectively, and a radius for the corners.
- [static func generateBox(width: Float, height: Float, depth: Float, cornerRadius: Float, splitFaces: Bool) -> MeshResource](meshresource/generatebox(width:height:depth:cornerradius:splitfaces:).md)
  Creates a box mesh from a width, height, depth and a corner radius, with the ability to assign different materials to each face.
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
### Creating a text mesh resource
- [static func generateText(String, extrusionDepth: Float, font: MeshResource.Font, containerFrame: CGRect, alignment: CTTextAlignment, lineBreakMode: CTLineBreakMode) -> MeshResource](meshresource/generatetext(_:extrusiondepth:font:containerframe:alignment:linebreakmode:)-3py6y.md)
  Generates a 3D mesh for rendering static text.
- [static func generateText(String, extrusionDepth: Float, font: MeshResource.Font, containerFrame: CGRect, alignment: CTTextAlignment, lineBreakMode: CTLineBreakMode) -> MeshResource](meshresource/generatetext(_:extrusiondepth:font:containerframe:alignment:linebreakmode:)-3py6y.md)
  Generates a 3D mesh for rendering static text.
- [convenience init(extruding: AttributedString, textOptions: MeshResource.GenerateTextOptions, extrusionOptions: MeshResource.ShapeExtrusionOptions) throws](meshresource/init(extruding:textoptions:extrusionoptions:)-7xk2s.md)
  Synchronously generates a 3D mesh from a string, with options for text layout and custom extrusions.
- [convenience init(extruding: AttributedString, textOptions: MeshResource.GenerateTextOptions, extrusionOptions: MeshResource.ShapeExtrusionOptions) throws](meshresource/init(extruding:textoptions:extrusionoptions:)-7xk2s.md)
  Synchronously generates a 3D mesh from a string, with options for text layout and custom extrusions.
### Creating a 3D mesh by extruding a 2D path
- [convenience init(extruding: Path, extrusionOptions: MeshResource.ShapeExtrusionOptions) throws](meshresource/init(extruding:extrusionoptions:)-6640v.md)
  Synchronously generates a 3D mesh by extruding a 2D path.
- [convenience init(extruding: Path, extrusionOptions: MeshResource.ShapeExtrusionOptions) throws](meshresource/init(extruding:extrusionoptions:)-6640v.md)
  Synchronously generates a 3D mesh by extruding a 2D path.
### Creating a mesh from an anchor
- [convenience init(from: LowLevelMesh) async throws](meshresource/init(from:)-1i7c9.md)
  Asynchronously creates a mesh resource from a low-level mesh.
- [convenience init(from: LowLevelMesh) async throws](meshresource/init(from:)-1i7c9.md)
  Asynchronously creates a mesh resource from a low-level mesh.
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
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [Creating 3D entities with RealityKit](../visionos/creating-3d-entities-with-realitykit.md)
  Display a horizontal row of three-dimensional shapes in your visionOS app, using predefined mesh and white material.
- [Creating 3D models as movable windows](../visionos/creating-a-volumetric-window-in-visionos.md)
  Display 3D content with a volumetric window that people can move.
- [Creating a 3D painting space](../visionos/creating-a-painting-space-in-visionos.md)
  Implement a painting canvas entity, and update its mesh to represent a stroke.
- [Tracking and visualizing hand movement](../visionos/tracking-and-visualizing-hand-movement.md)
  Use hand-tracking anchors to display a visual representation of hand transforms in visionOS.
- [Applying mesh to real-world surroundings](../visionos/applying-mesh-to-real-world-surroundings.md)
  Add a layer of mesh to objects in the real world, using scene reconstruction in ARKit.
- [Obscuring virtual items in a scene behind real-world items](../visionos/obscuring-virtual-items-in-a-scene-behind-real-world-items.md)
  Increase the realism of an immersive experience by adding entities with invisible materials  real-world objects.
- [Manipulating models with RealityKit](manipulating-models-with-realitykit.md)
  Interact with detailed 3D models using manipulation and clipping controls.
- [struct ModelComponent](modelcomponent.md)
  A component that contains a mesh and materials for the visual appearance of an entity.
- [class ModelEntity](modelentity.md)
  A representation of a physical object that RealityKit renders and optionally simulates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource)*