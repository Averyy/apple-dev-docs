# Cube Image (RealityKit)

**Framework**: ShaderGraph  
**Kind**: subscript

A texturecube with RealityKit properties.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

#### Overview

Adjustable level of detail. Input image must be in KTX file format

#### Parameter Types

#### Parameter Descriptions

#### Discussion

The `Cube Image` node produces a texture using the contents of the image file specified in the `File` parameter. It has a variety of parameters that affect the properties of the rendered textures.

> **Note**: Create the input file in a `.ktx` format or the node won’t work properly.

The possible values for the wrap mode parameters are:

> ⚠️ **Warning**: You can only use `clamp-to-zero` if the `Border Color` parameter is set to `transparent_black`; otherwise, the behavior of the node is undefined.

The possible values for `Mag Filter` and `Min Filter` are:

The `Mip Filter` parameter has the same possible values, with the addition of the option to allow for the value of `None`, which specifies that it doesn’t use mipmapping. Below is an example of a node graph that uses the `Cube Image Node` to take a `.ktx` file and create a cube image texture:

![None](https://docs-assets.developer.apple.com/published/73251fda502d95e648e767e15c053d18/CubeImageGraph.png)

Below, the resulting texture applies to a cube:

![None](https://docs-assets.developer.apple.com/published/809047cef616912077b426791ba2fc1e/CubeImageMaterial.png)

This example functions for all of the Cube Image nodes. The only difference is the various inputs used to modify how the cube image renders.

## See Also

- [Unlit Surface (RealityKit)](realitykit/unlit-surface-(realitykit).md)
  A surface shader that defines properties for a RealityKit Unlit material.
- [PBR Surface (RealityKit)](realitykit/pbr-surface-(realitykit).md)
  A surface shader that defines properties for a RealityKit Physically Based Rendering material.
- [Occlusion Surface (RealityKit)](realitykit/occlusion-surface-(realitykit).md)
  A surface shader that defines properties for a RealityKit Occlusion material that does not receive dynamic lighting.
- [Shadow Receiving Occlusion Surface (RealityKit)](realitykit/shadow-receiving-occlusion-surface-(realitykit).md)
  A surface shader that defines properties for a RealityKit Occlusion material that receives dynamic lighting.
- [View Direction (RealityKit)](realitykit/view-direction-(realitykit).md)
  A vector from a position in the scene to the view reference point.
- [Camera Position (RealityKit)](realitykit/camera-position-(realitykit).md)
  The position of the camera in the scene.
- [Geometry Modifier Model To World (RealityKit)](realitykit/geometry-modifier-model-to-world-(realitykit).md)
  The model-to-world transformation Matrix4x4 (Float).
- [Geometry Modifier World To Model (RealityKit)](realitykit/geometry-modifier-world-to-model-(realitykit).md)
  The world-to-model transformation Matrix4x4 (Float).
- [Geometry Modifier Normal To World (RealityKit)](realitykit/geometry-modifier-normal-to-world-(realitykit).md)
  The normal-to-world transformation Matrix3x3 (Float).
- [Geometry Modifier Model To View (RealityKit)](realitykit/geometry-modifier-model-to-view-(realitykit).md)
  The model-to-view transformation Matrix4x4 (Float).
- [Geometry Modifier View To Projection (RealityKit)](realitykit/geometry-modifier-view-to-projection-(realitykit).md)
  The view-to-projection transformation Matrix4x4 (Float).
- [Geometry Modifier Projection To View (RealityKit)](realitykit/geometry-modifier-projection-to-view-(realitykit).md)
  The projection-to-view transformation Matrix4x4 (Float).
- [Geometry Modifier Vertex ID (RealityKit)](realitykit/geometry-modifier-vertex-id-(realitykit).md)
  The integer index of the vertex.
- [Surface Model To World (RealityKit)](realitykit/surface-model-to-world-(realitykit).md)
  The model-to-world transformation Matrix4x4 (Float).
- [Surface Model To View (RealityKit)](realitykit/surface-model-to-view-(realitykit).md)
  The model-to-view transformation Matrix4x4 (Float).


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/realitykit/cube-image-(realitykit))*