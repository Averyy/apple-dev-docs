# MTLCoordinate2D

**Framework**: Metal  
**Kind**: typealias  
**Role**: Type Alias

A coordinate in the viewport.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
typealias MTLCoordinate2D = MTLSamplePosition
```

```c
typedef MTLSamplePosition MTLCoordinate2D;
```

## See Also

### Rasterization settings
- [Rendering at different rasterization rates](./rendering-at-different-rasterization-rates.md)
  Configure a rasterization rate map to vary rasterization rates depending on the amount of detail needed.
- [Creating a rasterization rate map](./creating-a-rasterization-rate-map.md)
  Define the rasterization rates for each part of your render target.
- [Rendering with a rasterization rate map](./rendering-with-a-rasterization-rate-map.md)
  Create offscreen textures to hold intermediate rasterized data.
- [Scaling variable rasterization rate content](./scaling-variable-rasterization-rate-content.md)
  Use the rate map data to scale the content to fill your destination texture.
- [class MTLRasterizationRateMapDescriptor](./mtlrasterizationratemapdescriptor.md)
  An object that you use to configure new rasterization rate maps.
- [protocol MTLRasterizationRateMap](./mtlrasterizationratemap.md)
  A compiled read-only instance that determines how to apply variable rasterization rates when rendering.
- [func MTLCoordinate2DMake(Float, Float) -> MTLCoordinate2D](./mtlcoordinate2dmake%28_,_%29.md)
  Returns a new 2D point with the specified coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcoordinate2d)*