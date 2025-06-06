# MeshResource

**Framework**: RealityKit  
**Kind**: class

A high-level representation of a collection of vertices and edges that define a shape.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency class MeshResource
```

## Mentions

- [Adding procedural assets to a scene](adding-procedural-assets-to-a-scene.md)
- [Reducing CPU Utilization in Your RealityKit App](reducing-cpu-utilization-in-your-realitykit-app.md)
- [Creating a plane with low-level mesh](creating-a-plane-with-low-level-mesh.md)

## Topics

### Creating a mesh resource
- [static func generate(from: MeshResource.Contents) throws -> MeshResource](meshresource/generate(from:)-30q3o.md)
  Create a mesh resource from contents.
- [static func generate(from: [MeshDescriptor]) throws -> MeshResource](meshresource/generate(from:)-6l1q2.md)
  Create a mesh resource from a list of mesh descriptors.
- [convenience init(from: [MeshDescriptor]) async throws](meshresource/init(from:)-b7hb.md)
  Initialize a mesh resource from descriptors asynchronously.
- [convenience init(from: MeshResource.Contents) async throws](meshresource/init(from:)-869q3.md)
  Initialize a mesh resource from contents asynchronously.
- [convenience init(shape: ShapeResource) async](meshresource/init(shape:)-9fxu3.md)
  Generates a MeshResource from a ShapeResource.
- [convenience init(shape: ShapeResource)](meshresource/init(shape:)-9yvj0.md)
  Generates a MeshResource from a ShapeResource.
- [static func generateAsync(from: MeshResource.Contents) -> LoadRequest<MeshResource>](meshresource/generateasync(from:)-5z7ky.md)
  Create a mesh resource from contents asynchronously.
- [static func generateAsync(from: [MeshDescriptor]) -> LoadRequest<MeshResource>](meshresource/generateasync(from:)-9ify3.md)
  Create a mesh resource from a list of mesh descriptors asynchronously.
### Creating a low level resource
- [convenience init(from: LowLevelMesh) async throws](meshresource/init(from:)-1ehyt.md)
  Asynchronously creates a mesh resource from a low-level mesh.
- [convenience init(from: LowLevelMesh) throws](meshresource/init(from:)-9kv7c.md)
  Synchronously creates a mesh resource from a low-level mesh.
- [var lowLevelMesh: LowLevelMesh?](meshresource/lowlevelmesh.md)
  The low-level mesh that this mesh is built from, if any.
### Configuring the resource
- [var expectedMaterialCount: Int](meshresource/expectedmaterialcount.md)
  The number of material entries required to render the mesh resource.
- [func replace(with: MeshResource.Contents) throws](meshresource/replace(with:)-4msjx.md)
  Replace the contents of this mesh resource.
- [func replace(with: MeshResource.Contents) async throws](meshresource/replace(with:)-8uvri.md)
  Replace the contents of this mesh resource asynchronously.
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
### Creating a text mesh resource
- [static func generateText(String, extrusionDepth: Float, font: MeshResource.Font, containerFrame: CGRect, alignment: CTTextAlignment, lineBreakMode: CTLineBreakMode) -> MeshResource](meshresource/generatetext(_:extrusiondepth:font:containerframe:alignment:linebreakmode:)-4fuil.md)
  Generates a 3D mesh for rendering static text.
- [static func generateText(String, extrusionDepth: Float, font: MeshResource.Font, containerFrame: CGRect, alignment: CTTextAlignment, lineBreakMode: CTLineBreakMode) -> MeshResource](meshresource/generatetext(_:extrusiondepth:font:containerframe:alignment:linebreakmode:)-5jn3l.md)
  Generates a 3D mesh for rendering static text.
- [convenience init(extruding: AttributedString, textOptions: MeshResource.GenerateTextOptions, extrusionOptions: MeshResource.ShapeExtrusionOptions) async throws](meshresource/init(extruding:textoptions:extrusionoptions:)-9oks6.md)
  Asynchronously generates a 3D mesh from a string, with options for text layout and custom extrusions.
- [convenience init(extruding: AttributedString, textOptions: MeshResource.GenerateTextOptions, extrusionOptions: MeshResource.ShapeExtrusionOptions) throws](meshresource/init(extruding:textoptions:extrusionoptions:)-5wd7v.md)
  Synchronously generates a 3D mesh from a string, with options for text layout and custom extrusions.
### Creating a 3D mesh by extruding a 2D path
- [convenience init(extruding: Path, extrusionOptions: MeshResource.ShapeExtrusionOptions) async throws](meshresource/init(extruding:extrusionoptions:)-3972u.md)
  Asynchronously generates a 3D mesh by extruding a 2D path.
- [convenience init(extruding: Path, extrusionOptions: MeshResource.ShapeExtrusionOptions) throws](meshresource/init(extruding:extrusionoptions:)-3jrqr.md)
  Synchronously generates a 3D mesh by extruding a 2D path.
### Creating a mesh from an anchor
- [convenience init(from: PlaneAnchor) async throws](meshresource/init(from:)-34188.md)
- [convenience init(from: MeshAnchor) async throws](meshresource/init(from:)-68flm.md)
  Creates a MeshResource from the provided MeshAnchor.
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
### Type Aliases
- [MeshResource.Font](meshresource/font.md)
  A platform-specific type that represents a font for use in generating a text mesh.

## Relationships

### Conforms To
- [Resource](resource.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct ModelComponent](modelcomponent.md)
  A component that contains a mesh and materials for the visual appearance of an entity.
- [class ModelEntity](modelentity.md)
  A representation of a physical object that RealityKit renders and optionally simulates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource)*