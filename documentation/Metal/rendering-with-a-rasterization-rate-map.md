# Rendering with a rasterization rate map

**Framework**: Metal

Create offscreen textures to hold intermediate rasterized data.

#### Overview

You don’t render data directly to the final render destination using variable rasterization rates. Instead, you allocate textures to use as intermediate targets. You get the sizes for these textures from the rate map. For example, if you specified a rate of `0.5` everywhere, the intermediate texture is half the height and width of the final render target.

The [`MTLRasterizationRateMap`](mtlrasterizationratemap.md) protocol [`screenSize`](mtlrasterizationratemap/screensize.md) property gives the dimensions of the final render target. Call the [`physicalSize(layer:)`](mtlrasterizationratemap/physicalsize(layer:).md): method on the rate map object to get the size for each layer. Then allocate the textures you need. For example, the following code gets the physical size and allocates a color texture and a depth texture of that size:

To use variable rasterization rates, create a render pass, specifying the intermediate textures as the render targets. Set the [`rasterizationRateMap`](mtlrenderpassdescriptor/rasterizationratemap.md) property to the rate map you created, as shown below:

After rendering with a rasterization rate map, you need to scale the intermediate textures to fill your destination texture. To convert between screen space and physical fragment space in your shader, bind the rate map data buffer to the shader with type `rasterization_rate_map_data`, then construct `rasterization_rate_map_decoder` with the buffer data. For more details, see the “Variable Rasterization Rate” section of the [`Metal Shading Language Specification`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf) and [`Scaling variable rasterization rate content`](scaling-variable-rasterization-rate-content.md).

## See Also

- [Rendering at different rasterization rates](rendering-at-different-rasterization-rates.md)
  Configure a rasterization rate map to vary rasterization rates depending on the amount of detail needed.
- [Creating a rasterization rate map](creating-a-rasterization-rate-map.md)
  Define the rasterization rates for each part of your render target.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metal/rendering-with-a-rasterization-rate-map)*