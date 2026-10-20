# NSCompositingOperation.sourceOver

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

The source image wherever it is opaque, and the destination image elsewhere.

**Availability**:
- macOS

## Declaration

```swift
case sourceOver
```

```c
NSCompositingOperationSourceOver
```

#### Discussion

The source image is applied using the formula `R = S + D*(1-Sa)`.

## See Also

### Operations for Compositing
- [NSCompositingOperation.clear](./clear.md)
  Transparency everywhere.
- [NSCompositingOperation.copy](./copy.md)
  The source image.
- [NSCompositingOperation.sourceIn](./sourcein.md)
  The source image wherever both images are opaque, and transparent elsewhere.
- [NSCompositingOperation.sourceOut](./sourceout.md)
  The source image wherever it is opaque and the destination image is transparent, and transparent elsewhere.
- [NSCompositingOperation.sourceAtop](./sourceatop.md)
  The source image wherever both images are opaque, the destination image wherever it is opaque but the source image is transparent, and transparent elsewhere
- [NSCompositingOperation.destinationOver](./destinationover.md)
  The destination image wherever it is opaque, and the source image elsewhere.
- [NSCompositingOperation.destinationIn](./destinationin.md)
  The destination image wherever both images are opaque, and transparent elsewhere.
- [NSCompositingOperation.destinationOut](./destinationout.md)
  The destination image wherever it is opaque and the source image is transparent, and transparent elsewhere.
- [NSCompositingOperation.destinationAtop](./destinationatop.md)
  The destination image wherever both images are opaque, the source image wherever it is opaque and the destination image is transparent, and transparent elsehwere.
- [NSCompositingOperation.xor](./xor.md)
  Exclusive OR of the source and destination images.
- [NSCompositingOperation.plusDarker](./plusdarker.md)
  The sum of the source and destination images, with color values approach 0 as a limit.
- [NSCompositingOperation.plusLighter](./pluslighter.md)
  The sum of the source and destination images, with color values approach 1 as a limit.
- [NSCompositingOperation.multiply](./multiply.md)
  The source color is multiplied by the destination color.
- [NSCompositingOperation.screen](./screen.md)
  Multiplies the complement of the destination and source color values, and then complements the result.
- [NSCompositingOperation.overlay](./overlay.md)
  Source colors overlay the destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscompositingoperation/sourceover)*