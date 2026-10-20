# RealityKit

**Framework**: ShaderGraph  
**Kind**: dictionary  
**Role**: ShaderGraph Node Group

Add RealityKit surfaces or textures to your material and access and manipulate scene geometry.

#### Overview

Incorporate RealityKit-specific content into your graph and modify that content visually. You can use geometry modifiers to change the vertices of your models. You can also create and configure RealityKit surfaces and textures and use them in your graph.

## Topics

### Nodes
- [Unlit Surface (RealityKit)](./realitykit/unlit-surface-%28realitykit%29.md)
  A surface shader that defines properties for a RealityKit Unlit material.
- [PBR Surface (RealityKit)](./realitykit/pbr-surface-%28realitykit%29.md)
  A surface shader that defines properties for a RealityKit Physically Based Rendering material.
- [Hair Surface (RealityKit)](./realitykit/hair-surface-%28realitykit%29.md)
  A surface shader that defines properties for a RealityKit Hair material.
- [Occlusion Surface (RealityKit)](./realitykit/occlusion-surface-%28realitykit%29.md)
  A surface shader that defines properties for a RealityKit Occlusion material that does not receive dynamic lighting.
- [Shadow Receiving Occlusion Surface (RealityKit)](./realitykit/shadow-receiving-occlusion-surface-%28realitykit%29.md)
  A surface shader that defines properties for a RealityKit Occlusion material that receives dynamic lighting.
- [View Direction (RealityKit)](./realitykit/view-direction-%28realitykit%29.md)
  A vector from a position in the scene to the view reference point.
- [Camera Position (RealityKit)](./realitykit/camera-position-%28realitykit%29.md)
  The position of the camera in the scene.
- [Geometry Modifier Model To World (RealityKit)](./realitykit/geometry-modifier-model-to-world-%28realitykit%29.md)
  The model-to-world transformation Matrix4x4 (Float).
- [Geometry Modifier World To Model (RealityKit)](./realitykit/geometry-modifier-world-to-model-%28realitykit%29.md)
  The world-to-model transformation Matrix4x4 (Float).
- [Geometry Modifier Normal To World (RealityKit)](./realitykit/geometry-modifier-normal-to-world-%28realitykit%29.md)
  The normal-to-world transformation Matrix3x3 (Float).
- [Geometry Modifier Model To View (RealityKit)](./realitykit/geometry-modifier-model-to-view-%28realitykit%29.md)
  The model-to-view transformation Matrix4x4 (Float).
- [Geometry Modifier View To Projection (RealityKit)](./realitykit/geometry-modifier-view-to-projection-%28realitykit%29.md)
  The view-to-projection transformation Matrix4x4 (Float).
- [Geometry Modifier Projection To View (RealityKit)](./realitykit/geometry-modifier-projection-to-view-%28realitykit%29.md)
  The projection-to-view transformation Matrix4x4 (Float).
- [Geometry Modifier Vertex ID (RealityKit)](./realitykit/geometry-modifier-vertex-id-%28realitykit%29.md)
  The integer index of the vertex.
- [Surface Model To World (RealityKit)](./realitykit/surface-model-to-world-%28realitykit%29.md)
  The model-to-world transformation Matrix4x4 (Float).
- [Surface Model To View (RealityKit)](./realitykit/surface-model-to-view-%28realitykit%29.md)
  The model-to-view transformation Matrix4x4 (Float).
- [Surface World To View (RealityKit)](./realitykit/surface-world-to-view-%28realitykit%29.md)
  The world-to-view transformation Matrix4x4 (Float).
- [Surface View To Projection (RealityKit)](./realitykit/surface-view-to-projection-%28realitykit%29.md)
  The view-to-projection transformation Matrix4x4 (Float).
- [Surface Projection To View (RealityKit)](./realitykit/surface-projection-to-view-%28realitykit%29.md)
  The projection-to-view transformation Matrix4x4 (Float).
- [Surface Screen Position (RealityKit)](./realitykit/surface-screen-position-%28realitykit%29.md)
  The coordinates of the currently-processed data in screen space.
- [Surface View Direction (RealityKit)](./realitykit/surface-view-direction-%28realitykit%29.md)
  A vector from a position in the scene to the view reference point.
- [Environment Radiance (RealityKit)](./realitykit/environment-radiance-%28realitykit%29.md)
  Returns an environment’s diffuse and specular radiance value based on real-world environment, and an IBL map that is either a developer-provided map or a default map.
- [Hover State (RealityKit)](./realitykit/hover-state-%28realitykit%29.md)
  Hover State to define custom hover effects.
- [Blurred Background (RealityKit)](./realitykit/blurred-background-%28realitykit%29.md)
  Returns a sample of the blurred background.
- [Geometry Modifier (RealityKit)](./realitykit/geometry-modifier-%28realitykit%29.md)
  A function that manipulates the location of a model’s vertices, run once per vertex.
- [Camera Index Switch (RealityKit)](./realitykit/camera-index-switch-%28realitykit%29.md)
  Render different results for each eye in a stereoscopic render.
- [Image 2D (RealityKit)](./realitykit/image-2d-%28realitykit%29.md)
  A texture with RealityKit properties.
- [Image 2D LOD (RealityKit)](./realitykit/image-2d-lod-%28realitykit%29.md)
  A texture with RealityKit properties and a explicit level of detail.
- [Image 2D Gradient (RealityKit)](./realitykit/image-2d-gradient-%28realitykit%29.md)
  A texture with RealityKit properties and a specified LOD gradient.
- [Image 2D Pixel (RealityKit)](./realitykit/image-2d-pixel-%28realitykit%29.md)
  A texture with RealityKit properties and pixel texture coordinates.
- [Image 2D LOD Pixel (RealityKit)](./realitykit/image-2d-lod-pixel-%28realitykit%29.md)
  A texture with RealityKit properties, a explicit level of detail, and pixel texture coordinates.
- [Image 2D Gradient Pixel (RealityKit)](./realitykit/image-2d-gradient-pixel-%28realitykit%29.md)
  A texture with RealityKit properties, a specified LOD gradient, and pixel texture coordinates.
- [Cube Image (RealityKit)](./realitykit/cube-image-%28realitykit%29.md)
  A texturecube with RealityKit properties.
- [Cube Image LOD (RealityKit)](./realitykit/cube-image-lod-%28realitykit%29.md)
  A texturecube with RealityKit properties and a explicit level of detail.
- [Cube Image Gradient (RealityKit)](./realitykit/cube-image-gradient-%28realitykit%29.md)
  A texturecube with RealityKit properties and a specified LOD gradient.
- [Image 2D Read (RealityKit)](./realitykit/image-2d-read-%28realitykit%29.md)
  Direct texture read.
- [Image 3D (RealityKit)](./realitykit/image-3d-%28realitykit%29.md)
  A texture with RealityKit properties.
- [Image 3D LOD (RealityKit)](./realitykit/image-3d-lod-%28realitykit%29.md)
  A texture with RealityKit properties.
- [Image 3D Gradient (RealityKit)](./realitykit/image-3d-gradient-%28realitykit%29.md)
  A texture with RealityKit properties.
- [Image 3D Pixel (RealityKit)](./realitykit/image-3d-pixel-%28realitykit%29.md)
  A texture with RealityKit properties.
- [Image 3D LOD Pixel (RealityKit)](./realitykit/image-3d-lod-pixel-%28realitykit%29.md)
  A texture with RealityKit properties.
- [Image 3D Gradient Pixel (RealityKit)](./realitykit/image-3d-gradient-pixel-%28realitykit%29.md)
  A texture with RealityKit properties.
- [Image 2D Array (RealityKit)](./realitykit/image-2d-array-%28realitykit%29.md)
  A texture with RealityKit properties.
- [Image 2D Array LOD (RealityKit)](./realitykit/image-2d-array-lod-%28realitykit%29.md)
  A texture with RealityKit properties.
- [Image 2D Array Gradient (RealityKit)](./realitykit/image-2d-array-gradient-%28realitykit%29.md)
  A texture with RealityKit properties.
- [Image 2D Array Pixel (RealityKit)](./realitykit/image-2d-array-pixel-%28realitykit%29.md)
  A texture with RealityKit properties.
- [Image 2D Array LOD Pixel (RealityKit)](./realitykit/image-2d-array-lod-pixel-%28realitykit%29.md)
  A texture with RealityKit properties.
- [Image 2D Array Gradient Pixel (RealityKit)](./realitykit/image-2d-array-gradient-pixel-%28realitykit%29.md)
  A texture with RealityKit properties.
- [Image 2D Array Read (RealityKit)](./realitykit/image-2d-array-read-%28realitykit%29.md)
  Direct texture read.
- [Image 3D Read (RealityKit)](./realitykit/image-3d-read-%28realitykit%29.md)
  Direct texture read.
- [Screen-Space X Partial Derivative (RealityKit)](./realitykit/screen-space-x-partial-derivative-%28realitykit%29.md)
  Returns a high-precision partial derivative of the specified value with respect to the screen space X coordinate.
- [Screen-Space Y Partial Derivative (RealityKit)](./realitykit/screen-space-y-partial-derivative-%28realitykit%29.md)
  Returns a high-precision partial derivative of the specified value with respect to the screen space Y coordinate.
- [Absolute Derivatives Sum (RealityKit)](./realitykit/absolute-derivatives-sum-%28realitykit%29.md)
  Returns the sum of the absolute derivatives in X and Y using local differencing for p; that is, fabs(dfdx(p)) + fabs(dfdy(p)).
- [Power Positive (RealityKit)](./realitykit/power-positive-%28realitykit%29.md)
  Computes X to the power of Y, where X is >= 0.
- [Round Integral (RealityKit)](./realitykit/round-integral-%28realitykit%29.md)
  Rounds X to integral value using round ties to even rounding mode in floating-point format.
- [Reflection Diffuse (RealityKit)](./realitykit/reflection-diffuse-%28realitykit%29.md)
  Diffuse component of reflection.
- [Reflection Specular (RealityKit)](./realitykit/reflection-specular-%28realitykit%29.md)
  Specular component of reflection.
- [Fortran Difference and Minimum (RealityKit)](./realitykit/fortran-difference-and-minimum-%28realitykit%29.md)
  Returns X – Y if X > Y, or +0 if X <= Y.
- [Is Finite (RealityKit)](./realitykit/is-finite-%28realitykit%29.md)
  Returns true if the incoming value is finite.
- [Is Infinite (RealityKit)](./realitykit/is-infinite-%28realitykit%29.md)
  Returns true if the incoming value is infinite.
- [Is Not a Number (RealityKit)](./realitykit/is-not-a-number-%28realitykit%29.md)
  Returns true if the incoming value is a not a number (NaN).
- [Is Normal (RealityKit)](./realitykit/is-normal-%28realitykit%29.md)
  Test if the incoming value is a normalized floating-point value.
- [Is Ordered (RealityKit)](./realitykit/is-ordered-%28realitykit%29.md)
  Test if arguments are ordered.
- [Is Unordered (RealityKit)](./realitykit/is-unordered-%28realitykit%29.md)
  Test if arguments are unordered.
- [Sign Bit (RealityKit)](./realitykit/sign-bit-%28realitykit%29.md)
  Tests for sign bit.
### Subscripts
- [Multiply 24 (RealityKit)](./realitykit/multiply-24-%28realitykit%29.md)
  Multiplies two 24-bit integer values X and Y and returns the 32-bit integer result.
- [Multiply Add 24 (RealityKit)](./realitykit/multiply-add-24-%28realitykit%29.md)
  Multiplies two 24-bit integer values X and Y and returns the 32-bit integer result with 32-bit Z value added.

## See Also

### Node Categories
- [2D-Procedural](./api-2d-procedural.md)
  Generate 2D gradients, noise, and other patterns programmatically for your material.
- [2D-Texture](./api-2d-texture.md)
  Load and configure 2D texture files.
- [3D-Procedural](./api-3d-procedural.md)
  Generate 3D noise patterns programmatically for your material.
- [3D-Texture](./api-3d-texture.md)
  Project multiple 2D images onto a surface to create a 3D texture.
- [Adjustment](./adjustment.md)
  Modify or convert values, or ranges of values, from one form to another.
- [Application](./application.md)
  Get system values such as the current time or the direction of the up vector.
- [Compositing](./compositing.md)
  Generate a single output from the combination of multiple data values.
- [Data](./data.md)
  Convert data values to different formats, or manipulate individual elements within a data structure.
- [Geometric](./geometric.md)
  Access scene geometry while your graph runs.
- [Logic](./logic.md)
  Perform Boolean operations and other logical comparisons on data values.
- [Material](./material.md)
  Encapsulate a set of shader graph nodes into a single module.
- [Math](./math.md)
  Perform a wide variety of mathematical and transformative operations on data values.
- [Organization](./organization.md)
  Modify the visual flow of data within your graph without changing any values.
- [Procedural](./procedural.md)
  Add a constant number, vector, matrix, color, string, or other value to your graph.
- [Surface](./surface.md)
  Generate a MaterialX preview surface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/realitykit)*