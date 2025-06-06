# Rendering with a Rasterization Rate Map

**Framework**: Metal

Create offscreen textures to hold intermediate rasterized data.

#### Overview

You don’t render data directly to the final render destination using variable rasterization rates. Instead, you allocate textures to use as intermediate targets. You get the sizes for these textures from the rate map. For example, if you specified a rate of `0.5` everywhere, the intermediate texture is half the height and width of the final render target.

The [`MTLRasterizationRateMap`](mtlrasterizationratemap.md) protocol [`screenSize`](mtlrasterizationratemap/screensize.md) property gives the dimensions of the final render target. Call the [`physicalSize(layer:)`](mtlrasterizationratemap/physicalsize(layer:).md): method on the rate map object to get the size for each layer. Then allocate the textures you need. For example, the following code gets the physical size and allocates a color texture and a depth texture of that size:

To use variable rasterization rates, create a render pass, specifying the intermediate textures as the render targets. Set the [`rasterizationRateMap`](mtlrenderpassdescriptor/rasterizationratemap.md) property to the rate map you created, as shown below:

## See Also

- [Rendering at Different Rasterization Rates](rendering-at-different-rasterization-rates.md)
  Configure a rasterization rate map to vary rasterization rates depending on the amount of detail needed.
- [Creating a Rasterization Rate Map](creating-a-rasterization-rate-map.md)
  Define the rasterization rates for each part of your render target.
- [Scaling Variable Rasterization Rate Content](scaling-variable-rasterization-rate-content.md)
  Use the rate map data to scale the content to fill your destination texture.
- [class MTLRasterizationRateMapDescriptor](mtlrasterizationratemapdescriptor.md)
  An object that you use to configure new rasterization rate maps.
- [protocol MTLRasterizationRateMap](mtlrasterizationratemap.md)
  A compiled read-only object that determines how to apply variable rasterization rates when rendering.
- [typealias MTLCoordinate2D](mtlcoordinate2d.md)
  A coordinate in the viewport.
- [func MTLCoordinate2DMake(Float, Float) -> MTLCoordinate2D](mtlcoordinate2dmake(_:_:).md)
  Returns a new 2D point with the specified coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/rendering-with-a-rasterization-rate-map)*