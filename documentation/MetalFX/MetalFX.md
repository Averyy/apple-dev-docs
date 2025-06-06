# MetalFX

**Framework**: MetalFX  
**Kind**: module

Boost your Metal app’s performance by upscaling lower-resolution content to save GPU time.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

#### Overview

The `MetalFX` framework integrates with [`Metal`](https://developer.apple.com/documentation/Metal) to upscale a relatively low-resolution image to a higher output resolution in less time than it takes to render directly to the output resolution.

![A timeline diagram that compares a traditional rendering timespan and compares it to a MetalFX upscaling timespan. The MetalFX upscaling method, which renders at a lower resolution and then upscales to the final resolution with MetalFX, takes about half the time traditional rendering, which renders directly to the higher, final resolution.](https://docs-assets.developer.apple.com/published/d0d41d9865689f453bc27b90af756121/media-4085441%402x.png)

Use the GPU time savings to further enhance your app or game’s experience. For example, add more effects or scene details.

`MetalFX` gives you two different ways to upscale your input renderings:

- Temporal antialiased upscaling
- Spatial upscaling

If you can provide pixel color, depth, and motion information, add an [`MTLFXTemporalScaler`](mtlfxtemporalscaler.md) instance to your render pipeline. Otherwise, add an [`MTLFXSpatialScaler`](mtlfxspatialscaler.md) instance, which only requires a pixel color input texture.

Because the scaling effects take time to initialize, make an instance of either effect at launch or when a display changes resolutions. Once you’ve created an effect instance, you can use it repeatedly, typically once per frame.

## Topics

### Temporal scaling
- [Applying temporal antialiasing and upscaling using MetalFX](applying-temporal-antialiasing-and-upscaling-using-metalfx.md)
  Reduce render workloads while increasing image detail with MetalFX.
- [protocol MTLFXTemporalScaler](mtlfxtemporalscaler.md)
  An upscaling effect that generates a higher resolution texture in a render pass by analyzing multiple input textures over time.
- [class MTLFXTemporalScalerDescriptor](mtlfxtemporalscalerdescriptor.md)
  A set of properties that configure a temporal scaling effect, and a factory method that creates the effect.
### Spatial scaling
- [protocol MTLFXSpatialScaler](mtlfxspatialscaler.md)
  An upscaling effect that generates a higher resolution texture in a render pass by spatially analyzing an input texture.
- [class MTLFXSpatialScalerDescriptor](mtlfxspatialscalerdescriptor.md)
  A set of properties that configure a spatial scaling effect, and a factory method that creates the effect.
- [enum MTLFXSpatialScalerColorProcessingMode](mtlfxspatialscalercolorprocessingmode.md)
  The color space modes for the input and output textures you use with a spatial scaling effect instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/MetalFX)*