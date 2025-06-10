# NSCompositingOperation

**Framework**: AppKit  
**Kind**: enum

Constants that describe compositing operators in terms of source and destination images, each having an opaque and transparent region.

**Availability**:
- macOS ?+

## Declaration

```swift
enum NSCompositingOperation
```

#### Overview

The type of operation, the source image, and the destination image determine the final output.

These compositing operators are defined in and used by [`compositeToPoint:fromRect:operation:`](nsimage/compositetopoint:fromrect:operation:.md), [`compositeToPoint:operation:`](nsimage/compositetopoint:operation:.md), [`compositeToPoint:fromRect:operation:fraction:`](nsimage/compositetopoint:fromrect:operation:fraction:.md), [`compositeToPoint:operation:fraction:`](nsimage/compositetopoint:operation:fraction:.md), [`draw(at:from:operation:fraction:)`](nsimage/draw(at:from:operation:fraction:).md), and [`draw(in:from:operation:fraction:)`](nsimage/draw(in:from:operation:fraction:).md). They are also used by drawing methods in other classes that take a compositing operator.

The equations after each constant represent the mathematical formulas for calculating the color value of the resulting pixel. The table below lists the meaning of each placeholder value in the equations.

| Placeholder | Meaning |
| --- | --- |
| `R` | The premultiplied result color. |
| `S` | The source color. |
| `D` | The destination color. |
| `Sa` | The alpha value of the source color. |
| `Da` | The alpha value of the destination color. |

## Topics

### Operations for Compositing
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
- [NSCompositingOperation.destinationOver](nscompositingoperation/destinationover.md)
  The destination image wherever it is opaque, and the source image elsewhere.
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
- [NSCompositingOperation.darken](nscompositingoperation/darken.md)
  Use the darker of the source and destination colors.
- [NSCompositingOperation.lighten](nscompositingoperation/lighten.md)
  Use the lighter of the source and destination colors.
- [NSCompositingOperation.colorDodge](nscompositingoperation/colordodge.md)
  Brightens the destination to reflect the source.
- [NSCompositingOperation.colorBurn](nscompositingoperation/colorburn.md)
  Darkens the destination color to reflect the source.
- [NSCompositingOperation.softLight](nscompositingoperation/softlight.md)
  Darkens or lightens colors, with the effect of shining a diffused spotlight on the destination.
- [NSCompositingOperation.hardLight](nscompositingoperation/hardlight.md)
  Multiplies or screens colors, with the effect of shining a spotlight on the destination.
- [NSCompositingOperation.difference](nscompositingoperation/difference.md)
  Subtracts the darker value from the lighter value.
- [NSCompositingOperation.exclusion](nscompositingoperation/exclusion.md)
  Subtracts the darker value from the lighter value, except lower in contrast.
- [NSCompositingOperation.hue](nscompositingoperation/hue.md)
  Uses the hue of the source and the saturation and luminosity of the destination.
- [NSCompositingOperation.saturation](nscompositingoperation/saturation.md)
  Uses the saturation value of the source and the hue and luminosity of the destination.
- [NSCompositingOperation.color](nscompositingoperation/color.md)
  Uses the hue and saturation of the source and the luminosity of the destination.
- [NSCompositingOperation.luminosity](nscompositingoperation/luminosity.md)
  Uses the luminosity of the source and the hue and saturation of the destination.
### Initializers
- [init?(rawValue: UInt)](nscompositingoperation/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var compositingOperation: NSCompositingOperation](nsgraphicscontext/compositingoperation.md)
  The graphics context’s global compositing operation setting.
- [var imageInterpolation: NSImageInterpolation](nsgraphicscontext/imageinterpolation.md)
  A constant that specifies the graphics context’s interpolation, or image smoothing, behavior.
- [enum NSImageInterpolation](nsimageinterpolation.md)
  Constants that specify the interpolation, or image smoothing, behavior used by the image interpolation property.
- [var shouldAntialias: Bool](nsgraphicscontext/shouldantialias.md)
  A Boolean value that indicates whether the graphics context uses antialiasing.
- [var patternPhase: NSPoint](nsgraphicscontext/patternphase.md)
  The amount to offset the pattern color when filling the graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscompositingoperation)*