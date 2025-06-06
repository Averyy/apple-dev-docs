# NSCompositingOperation.destinationOver

**Framework**: AppKit  
**Kind**: case

The destination image wherever it is opaque, and the source image elsewhere.

**Availability**:
- macOS ?+

## Declaration

```swift
case destinationOver
```

#### Discussion

The source image is applied using the formula `R = S*(1 - Da) + D`.

## See Also

- [NSCompositingOperation.clear](nscompositingoperation/clear.md)
  Transparency everywhere.
- [NSCompositingOperation.copy](nscompositingoperation/copy.md)
  The source image.
- [NSCompositingOperation.sourceOver](nscompositingoperation/sourceover.md)
  The source image wherever it is opaque, and the destination image elsewhere.
- [NSCompositingOperation.sourceIn](nscompositingoperation/sourcein.md)
  The source image wherever both images are opaque, and transparent elsewhere.
- [NSCompositingOperation.sourceOut](nscompositingoperation/sourceout.md)
  The source image wherever it is opaque and the destination image is transparent, and transparent elsewhere.
- [NSCompositingOperation.sourceAtop](nscompositingoperation/sourceatop.md)
  The source image wherever both images are opaque, the destination image wherever it is opaque but the source image is transparent, and transparent elsewhere
- [NSCompositingOperation.destinationIn](nscompositingoperation/destinationin.md)
  The destination image wherever both images are opaque, and transparent elsewhere.
- [NSCompositingOperation.destinationOut](nscompositingoperation/destinationout.md)
  The destination image wherever it is opaque and the source image is transparent, and transparent elsewhere.
- [NSCompositingOperation.destinationAtop](nscompositingoperation/destinationatop.md)
  The destination image wherever both images are opaque, the source image wherever it is opaque and the destination image is transparent, and transparent elsehwere.
- [NSCompositingOperation.xor](nscompositingoperation/xor.md)
  Exclusive OR of the source and destination images.
- [NSCompositingOperation.plusDarker](nscompositingoperation/plusdarker.md)
  The sum of the source and destination images, with color values approach 0 as a limit.
- [NSCompositingOperation.plusLighter](nscompositingoperation/pluslighter.md)
  The sum of the source and destination images, with color values approach 1 as a limit.
- [NSCompositingOperation.multiply](nscompositingoperation/multiply.md)
  The source color is multiplied by the destination color.
- [NSCompositingOperation.screen](nscompositingoperation/screen.md)
  Multiplies the complement of the destination and source color values, and then complements the result.
- [NSCompositingOperation.overlay](nscompositingoperation/overlay.md)
  Source colors overlay the destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscompositingoperation/destinationover)*