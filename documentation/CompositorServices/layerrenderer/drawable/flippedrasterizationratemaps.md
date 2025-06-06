# flippedRasterizationRateMaps

**Framework**: Compositor Services  
**Kind**: property

The rasterization rate maps that are flipped around the y-axis.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var flippedRasterizationRateMaps: [any MTLRasterizationRateMap] { get }
```

#### Discussion

Apply a flipped rasterization rate map to your render descriptor when you set up your drawing environment. Rasterization rate maps define how the GPU scales different parts of the texture to fill the display. You use them to save time and render less important parts of your scene at lower resolutions. For example, the drawable includes a rasterization rate map to render the portions of the texture in someone’s peripheral vision at a lower resolution. Flipped rasterization rate maps are available only when foveation is enabled and the [`generateFlippedRasterizationRateMaps`](layerrenderer/configuration-swift.struct/generateflippedrasterizationratemaps.md) property of your layer configuration is `true`.

## See Also

- [var rasterizationRateMaps: [any MTLRasterizationRateMap]](layerrenderer/drawable/rasterizationratemaps.md)
  The rasterization rate maps to use when rendering the frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/flippedrasterizationratemaps)*