# Mesh deformation

**Framework**: RealityKit

Reshape and animate the geometry of 3D models at runtime, applying skinning, blend shapes, and subdivision so surfaces bend, flex, and deform as a scene plays.

#### Overview

This collection covers the building blocks for modifying the vertices of a model after it loads, letting you drive lifelike motion such as characters bending, faces emoting, or surfaces smoothing in real time. It includes a configurable pipeline of stages that transform geometry, options for choosing where and how that work runs on the processor or graphics hardware, and lower-level entry points for fine-grained control over the transformation. Reach for these tools when prebaked animation is not enough and you need to compute or adjust a model’s shape dynamically. They give you control over performance trade-offs and the order in which transformations apply.

## Topics

### Deformers
- [struct MeshDeformerComponent](meshdeformercomponent.md)
  The component that applies mesh deformations to an `Entity`.
- [protocol MeshDeformer](meshdeformer.md)
  An interface for all deformation types in a deformation definition, both built-in and custom. The users overrides all functions to implement a custom `MeshDeformer`, and can in general ignore all but the constructors for built-in deformers.
- [struct SkinningDeformer](skinningdeformer.md)
  A deformation that binds a 3D mesh to an underlying skeleton.
- [struct BlendShapeDeformer](blendshapedeformer.md)
  A blend-shape deformation that interpolates between N meshes according to a weighted sum. Consumes information from the `BlendShapeWeightsComponent`
- [struct OpenSubdivisionDeformer](opensubdivisiondeformer.md)
  OpenSubdiv surface deformation
- [struct RenormalizationDeformer](renormalizationdeformer.md)
  Recalculates tangent frame based on current state of positions
- [struct CalculateBoundingBoxDeformer](calculateboundingboxdeformer.md)
  Calculates a bounding box based on the current state of the deformed positions.
### Parameters and options
- [struct MeshDeformerOptions](meshdeformeroptions.md)
  Specifies constant options for `MeshDeformer`
- [struct MeshDeformerVertexOptions](meshdeformervertexoptions.md)
  MeshDeformerVertexOptions allows developers to specify which vertex types in the mesh to allocate in the input and output buffers for mesh deformations.
- [enum MeshDeformerExecutionMode](meshdeformerexecutionmode.md)
  Specifies which `MesDeformer.deform` function will be called when used with custom deformers.
- [struct MeshDeformParameter](meshdeformparameter.md)
  Base class for GPU and CPU custom deform function input
- [struct MeshDeformationStack](meshdeformationstack.md)
  A set of `MeshDeformer`s to apply in order to a mesh, or a proper subset of the mesh specified by `Target`s. If at any point, a deformer in the stack updates, all deformers later in the stack will also update.
- [struct MeshScope](meshscope.md)
  The elements of a mesh resource that a deformation stack applies to.
- [typealias MeshDeformParameterCPU](meshdeformparametercpu.md)
  convenience alias
- [typealias MeshDeformParameterGPU](meshdeformparametergpu.md)
  convenience alias
- [typealias MeshDeformParametersCPU](meshdeformparameterscpu.md)
  convenience alias
- [typealias MeshDeformParametersGPU](meshdeformparametersgpu.md)
  convenience alias
- [typealias MeshDeformCPUBufferInput](meshdeformcpubufferinput.md)
  The underlying type of deformer input data buffers for the CPU functions.
- [typealias MeshDeformGPUBufferInput](meshdeformgpubufferinput.md)
  The underlying type of deformer input data buffers for the GPU functions.
- [typealias MeshDeformCPUBufferOutput](meshdeformcpubufferoutput.md)
  The underlying type of deformer output data buffers for the CPU functions.
- [typealias MeshDeformGPUBufferOutput](meshdeformgpubufferoutput.md)
  The underlying type of deformer input data buffers for the GPU functions.
### Low-level deformation
- [class LowLevelDeformation](lowleveldeformation.md)
  An object that encodes blend-shape, skinning, and renormalization passes into a Metal compute command encoder.
- [class LowLevelDeformationContext](lowleveldeformationcontext.md)
  An object that manages shared resources for [`LowLevelDeformation`](lowleveldeformation.md) instances.
- [class CanaryDescription](canarydescription.md)

## See Also

- [Hello World](../visionOS/World.md)
  Use windows, volumes, and immersive spaces to teach people about the Earth.
- [Enabling video reflections in an immersive environment](../visionOS/enabling-video-reflections-in-an-immersive-environment.md)
  Create a more immersive experience by adding video reflections in a custom environment.
- [Creating a spatial drawing app with RealityKit](creating-a-spatial-drawing-app-with-realitykit.md)
  Use low-level mesh and texture APIs to achieve fast updates to a person’s brush strokes by integrating RealityKit with ARKit and SwiftUI.
- [Generating interactive geometry with RealityKit](generating-interactive-geometry-with-realitykit.md)
  Create an interactive mesh with low-level mesh and low-level texture.
- [Combining 2D and 3D views in an immersive app](combining-2d-and-3d-views-in-an-immersive-app.md)
  Use attachments to place 2D content relative to 3D content in your visionOS app.
- [Transforming RealityKit entities using gestures](transforming-realitykit-entities-with-gestures.md)
  Build a RealityKit component to support standard visionOS gestures on any entity.
- [Responding to gestures on an entity](responding-to-gestures-on-an-entity.md)
  Respond to gestures performed on RealityKit entities using input target and collision components.
- [Models and meshes](scene-content-models-and-meshes.md)
  Display virtual objects in your scene with mesh-based models.
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene-content-mesh-deformation)*