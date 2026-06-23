# LowLevelDeformation

**Framework**: RealityKit  
**Kind**: class

An object that encodes blend-shape, skinning, and renormalization passes into a Metal compute command encoder.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class LowLevelDeformation
```

## Topics

### Creating a deformation
- [let descriptor: LowLevelDeformation.Descriptor](lowleveldeformation/descriptor-swift.property.md)
  The descriptor used to create this deformation.
- [LowLevelDeformation.Descriptor](lowleveldeformation/descriptor-swift.struct.md)
  An object that describes the per-frame data requirements for a [`LowLevelDeformation`](lowleveldeformation.md).
### Accessing mesh data
- [var input: LowLevelDeformation.Mesh](lowleveldeformation/input.md)
  The input vertex data for this deformation.
- [var output: LowLevelDeformation.Mesh](lowleveldeformation/output.md)
  The output vertex data for this deformation.
- [LowLevelDeformation.Mesh](lowleveldeformation/mesh.md)
  A handle to the input or output vertex data of a [`LowLevelDeformation`](lowleveldeformation.md).
- [var vertexCount: Int](lowleveldeformation/vertexcount.md)
  The number of vertices in the mesh.
- [LowLevelDeformation.VertexSemantic](lowleveldeformation/vertexsemantic.md)
  Designates the intended usage of a vertex attribute.
- [LowLevelDeformation.VertexAttribute](lowleveldeformation/vertexattribute.md)
  An object that describes the format and stride of a single vertex attribute.
### Configuring deformation stages
- [var skinning: LowLevelDeformation.Skinning](lowleveldeformation/skinning-swift.property.md)
  The skinning data accessors for this deformation.
- [LowLevelDeformation.Skinning](lowleveldeformation/skinning-swift.struct.md)
  An accessor for the skinning buffers of a [`LowLevelDeformation`](lowleveldeformation.md).
### Encoding deformation work
- [func encode(into: any MTLComputeCommandEncoder) throws](lowleveldeformation/encode(into:).md)
  Encodes the configured deformation passes into the given command encoder.
- [LowLevelDeformation.Pipeline](lowleveldeformation/pipeline.md)
  A compiled compute pipeline for a specific combination of mesh layouts and deformer stages.
- [LowLevelDeformation.Error](lowleveldeformation/error.md)
  The error type thrown by every throwing method and initializer.
### Structures
- [LowLevelDeformation.BlendShape](lowleveldeformation/blendshape-swift.struct.md)
  An accessor for the blend-shape buffers of a [`LowLevelDeformation`](lowleveldeformation.md).
- [LowLevelDeformation.Renormalization](lowleveldeformation/renormalization-swift.struct.md)
  An accessor for the renormalization buffers of a [`LowLevelDeformation`](lowleveldeformation.md).
### Instance Properties
- [var blendShape: LowLevelDeformation.BlendShape](lowleveldeformation/blendshape-swift.property.md)
  The blend-shape data accessors for this deformation.
- [var renormalization: LowLevelDeformation.Renormalization](lowleveldeformation/renormalization-swift.property.md)
  The renormalization data accessors for this deformation.

## See Also

- [class LowLevelDeformationContext](lowleveldeformationcontext.md)
  An object that manages shared resources for [`LowLevelDeformation`](lowleveldeformation.md) instances.
- [class CanaryDescription](canarydescription.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation)*