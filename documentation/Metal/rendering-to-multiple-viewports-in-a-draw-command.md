# Rendering to Multiple Viewports in a Draw Command

**Framework**: Metal

Select viewports and their corresponding scissor rectangles in your vertex shader.

#### Overview

A viewport defines a subsection of the render targets that you want a drawing command to render into. Using viewport selection, you provide multiple viewports for a drawing command, and dynamically choose one of these viewports for each primitive rendered by the drawing command. Viewport selection makes it easier to consolidate rendering to multiple viewports into fewer drawing commands. For example, you might use viewport selection when rendering stereo imagery or other images whose content is rendered to multiple parts of the render target.

![A block diagram that shows a render pipeline whose final destination is a single target with multiple viewports.](https://docs-assets.developer.apple.com/published/c028ba3b6b343c64f8f0ff8c12debc4c/media-3372066%402x.png)

##### Check the Device Object for Support for Multiple Viewports

All GPUs in the macOS family support multiple viewports. Multiple viewports are available in the Apple GPU family starting with family 5. Test for support using the code below:

For the maximum number of viewports you can use with each GPU family, see:

- [`Metal feature set tables (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf)
- [`Metal feature set tables (Numbers)`](https://developer.apple.comhttps://developer.apple.com/metal/metal-feature-set-tables.zip)

##### Add Viewport Selection to Your Vertex Shader

To specify which viewport a primitive should be rendered into, add a vertex output with the `[[viewport_array_index]]` attribute. Your vertex shader must set this value so that Metal knows which viewport to render into.

The example below uses instanced rendering to primitives to multiple viewports. It adds a `viewPort` field to the vertex output to specify the target slice. The target viewport is passed in as part of the per-instance properties, and copied to the vertex output.

```metal
typedef struct
{
    ...
    uint   viewport [[viewport_array_index]];
} ColorInOut;

vertex ColorInOut vertexTransform (
    const Vertex in [[ stage_in ]],
    const uint   instanceId                       [[ instance_id ]],
    const device InstanceParams* instanceParams   [[ buffer ]],
{
    ColorInOut out;
    out.viewport = instanceParams[instanceId].viewport;
    ...
}
```

Your vertex function must return the same index for all vertices that make up any given primitive.

The rasterization stage uses the selected viewport and associated scissor rectangle to transform the vertex outputs and then passes the data over to the fragment stage. If you need to know which viewport is being rendered to inside your fragment shader, you can reference the same field that you set in the vertex output.

##### Specify Viewports and Scissor Rectangles in Your Draw Command

Call [`setViewports(_:)`](mtlrendercommandencoder/setviewports(_:).md) to specify multiple viewports and [`setScissorRects(_:)`](mtlrendercommandencoder/setscissorrects(_:).md) to specify scissor rectangles:

Specify the same number of scissor rectangles and viewports. Coordinate your code that encodes render commands with the code in your shaders such that the indices that your shader generates are within the range of provided values.

## See Also

- [Specifying Drawing and Dispatch Arguments Indirectly](specifying-drawing-and-dispatch-arguments-indirectly.md)
  Use indirect commands if you don’t know your draw or dispatch call arguments when you encode the command.
- [Rendering to Multiple Texture Slices in a Draw Command](rendering-to-multiple-texture-slices-in-a-draw-command.md)
  Select a destination texture slice in your vertex shader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/rendering-to-multiple-viewports-in-a-draw-command)*