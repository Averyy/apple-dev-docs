# RealityKit

**Framework**: ShaderGraph  
**Kind**: dictionary

Add RealityKit surfaces or textures to your material and access and manipulate scene geometry.

#### Overview

Incorporate RealityKit-specific content into your graph and modify that content visually. You can use geometry modifiers to change the vertices of your models. You can also create and configure RealityKit surfaces and textures and use them in your graph.

## Topics

### Nodes
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
- [Surface World To View (RealityKit)](realitykit/surface-world-to-view-(realitykit).md)
  The world-to-view transformation Matrix4x4 (Float).
- [Surface View To Projection (RealityKit)](realitykit/surface-view-to-projection-(realitykit).md)
  The view-to-projection transformation Matrix4x4 (Float).
- [Surface Projection To View (RealityKit)](realitykit/surface-projection-to-view-(realitykit).md)
  The projection-to-view transformation Matrix4x4 (Float).
- [Surface Screen Position (RealityKit)](realitykit/surface-screen-position-(realitykit).md)
  The coordinates of the currently-processed data in screen space.
- [Surface View Direction (RealityKit)](realitykit/surface-view-direction-(realitykit).md)
  A vector from a position in the scene to the view reference point.
- [Environment Radiance (RealityKit)](realitykit/environment-radiance-(realitykit).md)
  Returns an environment’s diffuse and specular radiance value based on real-world environment, and an IBL map that is either a developer-provided map or a default map.
- [Hover State (RealityKit)](realitykit/hover-state-(realitykit).md)
  Hover State to define custom hover effects.
- [Blurred Background (RealityKit)](realitykit/blurred-background-(realitykit).md)
  Returns a sample of the blurred background.
- [Geometry Modifier (RealityKit)](realitykit/geometry-modifier-(realitykit).md)
  A function that manipulates the location of a model’s vertices, run once per vertex.
- [Camera Index Switch (RealityKit)](realitykit/camera-index-switch-(realitykit).md)
  Render different results for each eye in a stereoscopic render.
- [Image 2D (RealityKit)](realitykit/image-2d-(realitykit).md)
  A texture with RealityKit properties.
- [Image 2D LOD (RealityKit)](realitykit/image-2d-lod-(realitykit).md)
  A texture with RealityKit properties and a explicit level of detail.
- [Image 2D Gradient (RealityKit)](realitykit/image-2d-gradient-(realitykit).md)
  A texture with RealityKit properties and a specified LOD gradient.
- [Image 2D Pixel (RealityKit)](realitykit/image-2d-pixel-(realitykit).md)
  A texture with RealityKit properties and pixel texture coordinates.
- [Image 2D LOD Pixel (RealityKit)](realitykit/image-2d-lod-pixel-(realitykit).md)
  A texture with RealityKit properties, a explicit level of detail, and pixel texture coordinates.
- [Image 2D Gradient Pixel (RealityKit)](realitykit/image-2d-gradient-pixel-(realitykit).md)
  A texture with RealityKit properties, a specified LOD gradient, and pixel texture coordinates.
- [Cube Image (RealityKit)](realitykit/cube-image-(realitykit).md)
  A texturecube with RealityKit properties.
- [Cube Image LOD (RealityKit)](realitykit/cube-image-lod-(realitykit).md)
  A texturecube with RealityKit properties and a explicit level of detail.
- [Cube Image Gradient (RealityKit)](realitykit/cube-image-gradient-(realitykit).md)
  A texturecube with RealityKit properties and a specified LOD gradient.
- [Image 2D Read (RealityKit)](realitykit/image-2d-read-(realitykit).md)
  Direct texture read.
- [Image 3D (RealityKit)](realitykit/image-3d-(realitykit).md)
  A texture with RealityKit properties.
- [Image 3D LOD (RealityKit)](realitykit/image-3d-lod-(realitykit).md)
  A texture with RealityKit properties.
- [Image 3D Gradient (RealityKit)](realitykit/image-3d-gradient-(realitykit).md)
  A texture with RealityKit properties.
- [Image 3D Pixel (RealityKit)](realitykit/image-3d-pixel-(realitykit).md)
  A texture with RealityKit properties.
- [Image 3D LOD Pixel (RealityKit)](realitykit/image-3d-lod-pixel-(realitykit).md)
  A texture with RealityKit properties.
- [Image 3D Gradient Pixel (RealityKit)](realitykit/image-3d-gradient-pixel-(realitykit).md)
  A texture with RealityKit properties.
- [Image 2D Array (RealityKit)](realitykit/image-2d-array-(realitykit).md)
  A texture with RealityKit properties.
- [Image 2D Array LOD (RealityKit)](realitykit/image-2d-array-lod-(realitykit).md)
  A texture with RealityKit properties.
- [Image 2D Array Gradient (RealityKit)](realitykit/image-2d-array-gradient-(realitykit).md)
  A texture with RealityKit properties.
- [Image 2D Array Pixel (RealityKit)](realitykit/image-2d-array-pixel-(realitykit).md)
  A texture with RealityKit properties.
- [Image 2D Array LOD Pixel (RealityKit)](realitykit/image-2d-array-lod-pixel-(realitykit).md)
  A texture with RealityKit properties.
- [Image 2D Array Gradient Pixel (RealityKit)](realitykit/image-2d-array-gradient-pixel-(realitykit).md)
  A texture with RealityKit properties.
- [Image 2D Array Read (RealityKit)](realitykit/image-2d-array-read-(realitykit).md)
  Direct texture read.
- [Image 3D Read (RealityKit)](realitykit/image-3d-read-(realitykit).md)
  Direct texture read.
- [Screen-Space X Partial Derivative (RealityKit)](realitykit/screen-space-x-partial-derivative-(realitykit).md)
  Returns a high-precision partial derivative of the specified value with respect to the screen space X coordinate.
- [Screen-Space Y Partial Derivative (RealityKit)](realitykit/screen-space-y-partial-derivative-(realitykit).md)
  Returns a high-precision partial derivative of the specified value with respect to the screen space Y coordinate.
- [Absolute Derivatives Sum (RealityKit)](realitykit/absolute-derivatives-sum-(realitykit).md)
  Returns the sum of the absolute derivatives in X and Y using local differencing for p; that is, fabs(dfdx(p)) + fabs(dfdy(p)).
- [Power Positive (RealityKit)](realitykit/power-positive-(realitykit).md)
  Computes X to the power of Y, where X is >= 0.
- [Round Integral (RealityKit)](realitykit/round-integral-(realitykit).md)
  Rounds X to integral value using round ties to even rounding mode in floating-point format.
- [Reflection Diffuse (RealityKit)](realitykit/reflection-diffuse-(realitykit).md)
  Diffuse component of reflection.
- [Reflection Specular (RealityKit)](realitykit/reflection-specular-(realitykit).md)
  Specular component of reflection.
- [Fortran Difference and Minimum (RealityKit)](realitykit/fortran-difference-and-minimum-(realitykit).md)
  Returns X – Y if X > Y, or +0 if X <= Y.
- [Is Finite (RealityKit)](realitykit/is-finite-(realitykit).md)
  Returns true if the incoming value is finite.
- [Is Infinite (RealityKit)](realitykit/is-infinite-(realitykit).md)
  Returns true if the incoming value is infinite.
- [Is Not a Number (RealityKit)](realitykit/is-not-a-number-(realitykit).md)
  Returns true if the incoming value is a not a number (NaN).
- [Is Normal (RealityKit)](realitykit/is-normal-(realitykit).md)
  Test if the incoming value is a normalized floating-point value.
- [Is Ordered (RealityKit)](realitykit/is-ordered-(realitykit).md)
  Test if arguments are ordered.
- [Is Unordered (RealityKit)](realitykit/is-unordered-(realitykit).md)
  Test if arguments are unordered.
- [Sign Bit (RealityKit)](realitykit/sign-bit-(realitykit).md)
  Tests for sign bit.
### Subscripts
- [Multiply 24 (RealityKit)](realitykit/multiply-24-(realitykit).md)
  Multiplies two 24-bit integer values X and Y and returns the 32-bit integer result.
- [Multiply Add 24 (RealityKit)](realitykit/multiply-add-24-(realitykit).md)
  Multiplies two 24-bit integer values X and Y and returns the 32-bit integer result with 32-bit Z value added.

## See Also

- [2D-Procedural](2d-procedural.md)
  Generate 2D gradients, noise, and other patterns programmatically for your material.
- [2D-Texture](2d-texture.md)
  Load and configure 2D texture files.
- [3D-Procedural](3d-procedural.md)
  Generate 3D noise patterns programmatically for your material.
- [3D-Texture](3d-texture.md)
  Project multiple 2D images onto a surface to create a 3D texture.
- [Adjustment](adjustment.md)
  Modify or convert values, or ranges of values, from one form to another.
- [Application](application.md)
  Get system values such as the current time or the direction of the up vector.
- [Compositing](compositing.md)
  Generate a single output from the combination of multiple data values.
- [Data](data.md)
  Convert data values to different formats, or manipulate individual elements within a data structure.
- [Geometric](geometric.md)
  Access scene geometry while your graph runs.
- [Logic](logic.md)
  Perform Boolean operations and other logical comparisons on data values.
- [Material](material.md)
  Encapsulate a set of shader graph nodes into a single module.
- [Math](math.md)
  Perform a wide variety of mathematical and transformative operations on data values.
- [Organization](organization.md)
  Modify the visual flow of data within your graph without changing any values.
- [Procedural](procedural.md)
  Add a constant number, vector, matrix, color, string, or other value to your graph.
- [Surface](surface.md)
  Generate a MaterialX preview surface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/realitykit)*