# Deprecated symbols

**Framework**: AppKit  
**Role**: API Collection

Review symbols that are no longer in active development, and their recommended replacements.

#### Overview

Although these symbols are available for use, Apple is no longer actively developing them, and may remove them in a future release. Apple recommends moving away from these symbols and using their indicated replacements instead. Check the individual symbol pages for the recommended replacements.

## Topics

### Deprecated constants
- [NSCompositeClear](./nscompositeclear.md)
  Transparent. (`R = 0`)
- [NSCompositeCopy](./nscompositecopy.md)
  Source image. (`R = S`)
- [NSCompositeSourceOver](./nscompositesourceover.md)
  Source image wherever source image is opaque, and destination image elsewhere. (`R = S + D*(1 - Sa)`)
- [NSCompositeSourceIn](./nscompositesourcein.md)
  Source image wherever both images are opaque, and transparent elsewhere. (`R = S*Da`)
- [NSCompositeSourceOut](./nscompositesourceout.md)
  Source image wherever source image is opaque but destination image is transparent, and transparent elsewhere. (`R = S*(1 - Da)`)
- [NSCompositeSourceAtop](./nscompositesourceatop.md)
  Source image wherever both images are opaque, destination image wherever destination image is opaque but source image is transparent, and transparent elsewhere. (`R = S*Da + D*(1 - Sa)`)
- [NSCompositeDestinationOver](./nscompositedestinationover.md)
  Destination image wherever destination image is opaque, and source image elsewhere. (`R = S*(1 - Da) + D`)
- [NSCompositeDestinationIn](./nscompositedestinationin.md)
  Destination image wherever both images are opaque, and transparent elsewhere. (`R = D*Sa`)
- [NSCompositeDestinationOut](./nscompositedestinationout.md)
  Destination image wherever destination image is opaque but source image is transparent, and transparent elsewhere. (`R = D*(1 - Sa)`)
- [NSCompositeDestinationAtop](./nscompositedestinationatop.md)
  Destination image wherever both images are opaque, source image wherever source image is opaque but destination image is transparent, and transparent elsewhere. (`R = S*(1 - Da) + D*Sa`)
- [NSCompositeXOR](./nscompositexor.md)
  Exclusive OR of source and destination images. (`R = S*(1 - Da) + D*(1 - Sa)`)
- [NSCompositePlusDarker](./nscompositeplusdarker.md)
  Sum of source and destination images, with color values approaching 0 as a limit. (`R = MAX(0, (1 - D) + (1 - S))`)
- [NSCompositePlusLighter](./nscompositepluslighter.md)
  Sum of source and destination images, with color values approaching 1 as a limit. (`R = MIN(1, S + D)`)
- [NSCompositeMultiply](./nscompositemultiply.md)
  The source color is multiplied by the destination color.
- [NSCompositeScreen](./nscompositescreen.md)
  Multiplies the complement of the destination and source color values, and then complements the result.
- [NSCompositeOverlay](./nscompositeoverlay.md)
  Source colors overlay the destination.
- [NSCompositeDarken](./nscompositedarken.md)
  Use the darker of the source and destination colors.
- [NSCompositeLighten](./nscompositelighten.md)
  Use the lighter of the source and destination colors.
- [NSCompositeColorDodge](./nscompositecolordodge.md)
  Brightens the destination to reflect the source.
- [NSCompositeColorBurn](./nscompositecolorburn.md)
  Darkens the destination color to reflect the source.
- [NSCompositeSoftLight](./nscompositesoftlight.md)
  Darkens or lightens colors, with the effect of shining a diffused spotlight on the destination.
- [NSCompositeHardLight](./nscompositehardlight.md)
  Multiplies or screens colors, with the effect of shining a spotlight on the destination.
- [NSCompositeDifference](./nscompositedifference.md)
  Subtracts the darker value from the lighter value.
- [NSCompositeExclusion](./nscompositeexclusion.md)
  Subtracts the darker value from the lighter value, except lower in contrast.
- [NSCompositeHue](./nscompositehue.md)
  Uses the hue of the source and the saturation and luminosity of the destination.
- [NSCompositeSaturation](./nscompositesaturation.md)
  Uses the saturation value of the source and the hue and luminosity of the destination.
- [NSCompositeColor](./nscompositecolor.md)
  Uses the hue and saturation of the source and the luminosity of the destination.
- [NSCompositeLuminosity](./nscompositeluminosity.md)
  Uses the luminosity of the source and the hue and saturation of the destination.
- [NSCompositeHighlight](./nscompositehighlight.md)
  Source image wherever source image is opaque, and destination image elsewhere.
### Deprecated symbols
- [NSCompositingOperationHighlight](./nscompositingoperation/nscompositingoperationhighlight.md)
  The source image wherever it is opaque, and the destination image elsewhere.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscompositingoperation-deprecated-symbols)*