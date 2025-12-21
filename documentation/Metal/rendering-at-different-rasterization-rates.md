# Rendering at different rasterization rates

**Framework**: Metal

Configure a rasterization rate map to vary rasterization rates depending on the amount of detail needed.

#### Overview

In complex 3D applications, you perform many calculations to render each pixel in the output image, generating a high-quality result. However, as your render targets get larger and screen resolutions increase, the cost to render so many pixels at high quality becomes too great.

One common solution is to render intermediate images at a lower resolution and then stretch them to generate the final result. Although this solution incurs an additional cost to scale the image, it can greatly reduce the memory and performance costs to render it. This solution is most useful when lower image quality is acceptable or not noticeable, and the render savings are larger than the scaling cost.

Another way to reduce rendering cost is to avoid complex calculations in parts of the rendered image when you don’t need the detail in those parts or the app discards them later in the rendering process. For example, if you plan to apply a blur effect to part of your image as a postprocessing step, you don’t need to incur the cost of rendering those pixels with great detail, because the blur effect removes the details.

##### Implement Variable Rasterization Rates

In Metal, you can combine these two solutions by using variable rasterization rates (VRR). You specify different rasterization rates for different parts of the render target. When you need detail, you render those areas of the target at full resolution. In areas that don’t need detail, you specify a lower resolution rate, which means that you need fewer pixels in those areas and fewer invocations of your fragment shader.

Use VRR when:

- You want to render different parts of your render target at different quality levels.
- The cost to render each pixel is high enough that reducing rasterization rates produces substantial savings in rendering time, and the savings are greater than the additional cost of scaling the image to a full-rate image.

To use VRR, you create a rasterization map to divide the render target into zones and specify a horizontal and vertical rasterization rate for each zone. After you create the rate map, you allocate textures to hold intermediate images. These textures are smaller than the final render target image, because you allocate only the memory you need to hold the rendered pixels.

After you’ve finished rendering intermediate data using the rate map, you execute additional draw commands to stretch the intermediate data and copy it to another texture at the higher resolution, such as a texture provided by a Metal drawable for display. This final target is called a , because it uses the normal rasterization uniformly across the image. After you generate the full-rate image, you can apply additional processing to it. For example, you usually want to render user interface elements on top of the full-rate image.

##### Check for Vrr Support

Not all GPUs support VRR. Before attempting to use it, check for support on the device object:

## See Also

- [Creating a rasterization rate map](creating-a-rasterization-rate-map.md)
  Define the rasterization rates for each part of your render target.
- [Rendering with a rasterization rate map](rendering-with-a-rasterization-rate-map.md)
  Create offscreen textures to hold intermediate rasterized data.
- [Scaling variable rasterization rate content](scaling-variable-rasterization-rate-content.md)
  Use the rate map data to scale the content to fill your destination texture.
- [class MTLRasterizationRateMapDescriptor](mtlrasterizationratemapdescriptor.md)
  An object that you use to configure new rasterization rate maps.
- [protocol MTLRasterizationRateMap](mtlrasterizationratemap.md)
  A compiled read-only instance that determines how to apply variable rasterization rates when rendering.
- [typealias MTLCoordinate2D](mtlcoordinate2d.md)
  A coordinate in the viewport.
- [func MTLCoordinate2DMake(Float, Float) -> MTLCoordinate2D](mtlcoordinate2dmake(_:_:).md)
  Returns a new 2D point with the specified coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/rendering-at-different-rasterization-rates)*