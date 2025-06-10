# Applying temporal antialiasing and upscaling using MetalFX

**Framework**: MetalFX

Reduce render workloads while increasing image detail with MetalFX.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- Xcode 14.0+

#### Overview

> **Note**: This sample code project is associated with WWDC22 session [`10103: Boost performance with MetalFX upscaling`](https://developer.apple.comhttps://developer.apple.com/wwdc22/10103/).

##### Configure the Sample Code Project

This sample code project requires the following:

- macOS 13 or later, and a Mac with the M1 chip or an Intel-based Mac
- iOS 16 or later, and an iPad with the M1 chip
- Xcode 14 or later

## See Also

- [protocol MTLFXTemporalScaler](mtlfxtemporalscaler.md)
  An upscaling effect that generates a higher resolution texture in a render pass by analyzing multiple input textures over time.
- [class MTLFXTemporalScalerDescriptor](mtlfxtemporalscalerdescriptor.md)
  A set of properties that configure a temporal scaling effect, and a factory method that creates the effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/applying-temporal-antialiasing-and-upscaling-using-metalfx)*