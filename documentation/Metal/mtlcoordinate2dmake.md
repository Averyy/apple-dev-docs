# MTLCoordinate2DMake(_:_:)

**Framework**: Metal  
**Kind**: func

Returns a new 2D point with the specified coordinates.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
func MTLCoordinate2DMake(_ x: Float, _ y: Float) -> MTLCoordinate2D
```

## Parameters

- `x`: The x coordinate of the new point.
- `y`: The y coordinate of the new point.

## See Also

- [Rendering at Different Rasterization Rates](rendering-at-different-rasterization-rates.md)
  Configure a rasterization rate map to vary rasterization rates depending on the amount of detail needed.
- [Creating a Rasterization Rate Map](creating-a-rasterization-rate-map.md)
  Define the rasterization rates for each part of your render target.
- [Rendering with a Rasterization Rate Map](rendering-with-a-rasterization-rate-map.md)
  Create offscreen textures to hold intermediate rasterized data.
- [Scaling Variable Rasterization Rate Content](scaling-variable-rasterization-rate-content.md)
  Use the rate map data to scale the content to fill your destination texture.
- [class MTLRasterizationRateMapDescriptor](mtlrasterizationratemapdescriptor.md)
  An object that you use to configure new rasterization rate maps.
- [protocol MTLRasterizationRateMap](mtlrasterizationratemap.md)
  A compiled read-only object that determines how to apply variable rasterization rates when rendering.
- [typealias MTLCoordinate2D](mtlcoordinate2d.md)
  A coordinate in the viewport.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcoordinate2dmake(_:_:))*