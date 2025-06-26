# Models and meshes

**Framework**: RealityKit

Display virtual objects in your scene with mesh-based models.

#### Overview

Meshes are the building blocks for every visible geometric shape and model in RealityKit, including those that come from a USDZ file. Create primitive shapes by calling a [`MeshResource`](meshresource.md) factory method, such as [`generateBox(size:cornerRadius:)`](meshresource/generatebox(size:cornerradius:)-8em0v.md), or define your own mesh by creating and configuring a [`MeshDescriptor`](meshdescriptor.md) or a [`LowLevelMesh`](lowlevelmesh.md) instance.

Display meshes in your scene by creating a [`ModelComponent`](modelcomponent.md) for each mesh, and add that component to an entity. You can also add [`Material`](material.md) instances to your mesh by adding them to the same `ModelComponent` instance.

## Topics

### Model display
- [struct ModelComponent](modelcomponent.md)
  A component that contains a mesh and materials for the visual appearance of an entity.
- [class MeshResource](meshresource.md)
  A high-level representation of a collection of vertices and edges that define a shape.
- [class ModelEntity](modelentity.md)
  A representation of a physical object that RealityKit renders and optionally simulates.
### Render configuration
- [struct ModelSortGroupComponent](modelsortgroupcomponent.md)
  A component that configures the rendering order for an entity’s model.
- [struct ModelSortGroup](modelsortgroup.md)
  A group that you assign to multiple entities to tell the renderer what order and how to render the entities in the group.
- [struct OpacityComponent](opacitycomponent.md)
  A component that controls the opacity of an entity and its descendants.
- [struct AdaptiveResolutionComponent](adaptiveresolutioncomponent.md)
  A component that provides the suggested pixels per meter necessary to render an object.
- [struct ModelDebugOptionsComponent](modeldebugoptionscomponent.md)
  A component that changes how RealityKit renders its entity to help with debugging.
- [struct MeshInstancesComponent](meshinstancescomponent.md)
  A component that performs GPU instancing on the ModelComponent on the same Entity.
### Static meshes
- [struct MeshDescriptor](meshdescriptor.md)
  Defines a 3D mesh’s structure and data.
- [MeshDescriptor.Primitives](meshdescriptor/primitives-swift.enum.md)
  Indicates which primitive shape type a mesh applies to its vertex indices.
- [MeshDescriptor.Materials](meshdescriptor/materials-swift.enum.md)
### Updatable meshes
- [Creating a spatial drawing app with RealityKit](creating-a-spatial-drawing-app-with-realitykit.md)
  Use low-level mesh and texture APIs to achieve fast updates to a person’s brush strokes by integrating RealityKit with ARKit and SwiftUI.
- [Creating a plane with low-level mesh](creating-a-plane-with-low-level-mesh.md)
  Create a low-level mesh and set its vertex positions and normals to form a plane.
- [class LowLevelMesh](lowlevelmesh.md)
  A container for vertex data that you can use to create and update meshes using your own format.
- [LowLevelMesh.Descriptor](lowlevelmesh/descriptor-swift.struct.md)
  An object that describes the data format and layout of the buffers in a low-level mesh.
- [LowLevelMesh.Part](lowlevelmesh/part.md)
  An object that describes a range of primitives to display, and their material index.
- [LowLevelMesh.Layout](lowlevelmesh/layout.md)
  An object that describes a set of attributes that share a buffer index, offset, and stride.
- [LowLevelMesh.Attribute](lowlevelmesh/attribute.md)
  An object that determines how to store vertex attribute data in memory and map it to RealityKit shader attributes.
- [LowLevelMesh.VertexSemantic](lowlevelmesh/vertexsemantic.md)
  Designates the intended usage of a vertex attribute.
- [LowLevelMesh.PartsCollection](lowlevelmesh/partscollection.md)
  An object that holds a mutable collection low-level mesh parts.
- [class LowLevelBuffer](lowlevelbuffer.md)
- [class LowLevelInstanceData](lowlevelinstancedata.md)
### Bounding box retrieval
- [struct BoundingBox](boundingbox.md)
  An axis-aligned bounding box (AABB).
- [struct OrientedBoundingBox](orientedboundingbox.md)
  Representation for an oriented bounding box. Uses a combination of an axis-aligned bounding box and a rotation vector around the centroid of the said axis-aligned bounding box to represent an oriented bounding box.
### Mesh description
- [struct MeshBuffer](meshbuffer.md)
  Mesh buffer containing elements of any type.
- [protocol MeshBufferContainer](meshbuffercontainer.md)
  Conforming objects contain a table of mesh buffers.
- [protocol MeshBufferSemantic](meshbuffersemantic.md)
  A protocol that holds an identifier value for mesh buffers.
- [enum MeshBuffers](meshbuffers.md)
  An object that holds the data for an model entity’s mesh.
- [struct AnyMeshBuffer](anymeshbuffer.md)
  Mesh buffer stored in the container.
- [struct MeshInstanceCollection](meshinstancecollection.md)
  An object that holds a collection of mesh resource instances.
- [struct MeshModelCollection](meshmodelcollection.md)
  An object that holds a collection of mesh models.
- [struct MeshPartCollection](meshpartcollection.md)
  An object that holds a collection of mesh parts.
### Mesh skeletons
- [struct MeshSkeletonCollection](meshskeletoncollection.md)
  An object that holds a collection of skeletons used by a mesh resource.
- [struct MeshJointInfluence](meshjointinfluence.md)
  A binding to a joint, which consists of the joint’s index and the weight of that joint’s influence on a vertex.
### Blend shape management
- [struct BlendShapeWeightsComponent](blendshapeweightscomponent.md)
  A component that provides access to the current weights associated with all blend shape meshes on an entity.
- [class BlendShapeWeightsMapping](blendshapeweightsmapping.md)
  A mapping of blend weights to the target meshes that those weights affect.
- [struct BlendShapeWeights](blendshapeweights.md)
  A set of animatable weight values that collectively represent the blending amounts for all the blend shapes’ blend targets.
- [struct BlendShapeWeightsData](blendshapeweightsdata.md)
  A structure that encapsulates the blend shape name, blend shape weights and the names of those weights to be stored by the blend shape weights set.
- [struct BlendShapeWeightsSet](blendshapeweightsset.md)
  A custom collection of named blend shape weights.
### Entity compliance
- [protocol HasModel](hasmodel.md)
  An interface that provides meshes and materials to define the visual appearance of an entity.

## See Also

- [Hello World](../visionOS/World.md)
  Use windows, volumes, and immersive spaces to teach people about the Earth.
- [Creating a spatial drawing app with RealityKit](creating-a-spatial-drawing-app-with-realitykit.md)
  Use low-level mesh and texture APIs to achieve fast updates to a person’s brush strokes by integrating RealityKit with ARKit and SwiftUI.
- [Generating interactive geometry with RealityKit](generating-interactive-geometry-with-realitykit.md)
  Create an interactive mesh with low-level mesh and low-level texture.
- [Combining 2D and 3D views in an immersive app](combining-2d-and-3d-views-in-an-immersive-app.md)
  Use attachments to place 2D content relative to 3D content in your visionOS app.
- [Transforming RealityKit entities using gestures](transforming-realitykit-entities-with-gestures.md)
  Build a RealityKit component to support standard visionOS gestures on any entity.
- [Materials, textures, and shaders](scene-content-materials-and-shaders.md)
  Apply textures to the surface of your scene’s 3D objects to give each object a unique appearance.
- [Anchors](scene-content-anchors.md)
  Lock virtual content to the real world.
- [Lights and cameras](scene-content-lights-and-cameras.md)
  Control the lighting and point of view for a scene.
- [Content synchronization](scene-content-content-synchronization.md)
  Synchronize the contents of entities locally or across the network.
- [Audio](scene-content-audio.md)
  Create personalized and realistic spatial audio experiences.
- [Videos](scene-content-videos.md)
  Present videos in your RealityKit experiences.
- [Images](scene-content-images.md)
  Present images and spatial scenes in your RealityKit experiences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene-content-models-and-meshes)*