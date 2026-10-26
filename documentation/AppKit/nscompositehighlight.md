# NSCompositeHighlight

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

Source image wherever source image is opaque, and destination image elsewhere.

**Availability**:
- macOS 10.0+ - Deprecated in 10.0

> **Deprecated**: Use [`NSCompositingOperation.sourceOver`](./nscompositingoperation/sourceover.md) instead.

## Declaration

```c
static const NSCompositingOperation NSCompositeHighlight;
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscompositehighlight)*