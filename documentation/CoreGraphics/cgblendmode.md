# CGBlendMode

**Framework**: Core Graphics  
**Kind**: enum

Compositing operations for images.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum CGBlendMode
```

#### Overview

These blend mode constants represent the Porter-Duff blend modes. The symbols in the equations for these blend modes are:

- R is the premultiplied result
- S is the source color, and includes alpha
- D is the destination color, and includes alpha
- Ra, Sa, and Da are the alpha components of R, S, and D

You can find more information on blend modes, including examples of images produced using them, and many mathematical descriptions of the modes, in , Version 1.5, Adobe Systems, Inc. If you are a former QuickDraw developer, it may be helpful for you to think of blend modes as an alternative to transfer modes

For examples of using blend modes see “Setting Blend Modes” and “Using Blend Modes With Images” in [`Quartz 2D Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066).

## Topics

### Constants
- [CGBlendMode.normal](cgblendmode/normal.md)
  Paints the source image samples over the background image samples.
- [CGBlendMode.multiply](cgblendmode/multiply.md)
  Multiplies the source image samples with the background image samples. This results in colors that are at least as dark as either of the two contributing sample colors.
- [CGBlendMode.screen](cgblendmode/screen.md)
  Multiplies the inverse of the source image samples with the inverse of the background image samples, resulting in colors that are at least as light as either of the two contributing sample colors.
- [CGBlendMode.overlay](cgblendmode/overlay.md)
- [CGBlendMode.darken](cgblendmode/darken.md)
- [CGBlendMode.lighten](cgblendmode/lighten.md)
- [CGBlendMode.colorDodge](cgblendmode/colordodge.md)
  Brightens the background image samples to reflect the source image samples. Source image sample values that specify black do not produce a change.
- [CGBlendMode.colorBurn](cgblendmode/colorburn.md)
  Darkens the background image samples to reflect the source image samples. Source image sample values that specify white do not produce a change.
- [CGBlendMode.softLight](cgblendmode/softlight.md)
- [CGBlendMode.hardLight](cgblendmode/hardlight.md)
- [CGBlendMode.difference](cgblendmode/difference.md)
- [CGBlendMode.exclusion](cgblendmode/exclusion.md)
  Produces an effect similar to that produced by [`CGBlendMode.difference`](cgblendmode/difference.md), but with lower contrast. Source image sample values that are black don’t produce a change; white inverts the background color values.
- [CGBlendMode.hue](cgblendmode/hue.md)
  Uses the luminance and saturation values of the background with the hue of the source image.
- [CGBlendMode.saturation](cgblendmode/saturation.md)
  Uses the luminance and hue values of the background with the saturation of the source image. Areas of the background that have no saturation (that is, pure gray areas) don’t produce a change.
- [CGBlendMode.color](cgblendmode/color.md)
  Uses the luminance values of the background with the hue and saturation values of the source image. This mode preserves the gray levels in the image. You can use this mode to color monochrome images or to tint color images.
- [CGBlendMode.luminosity](cgblendmode/luminosity.md)
  Uses the hue and saturation of the background with the luminance of the source image. This mode creates an effect that is inverse to the effect created by [`CGBlendMode.color`](cgblendmode/color.md).
- [CGBlendMode.clear](cgblendmode/clear.md)
  `R = 0`
- [CGBlendMode.copy](cgblendmode/copy.md)
  `R = S`
- [CGBlendMode.sourceIn](cgblendmode/sourcein.md)
  `R = S*Da`
- [CGBlendMode.sourceOut](cgblendmode/sourceout.md)
  `R = S*(1 - Da)`
- [CGBlendMode.sourceAtop](cgblendmode/sourceatop.md)
  `R = S*Da + D*(1 - Sa)`
- [CGBlendMode.destinationOver](cgblendmode/destinationover.md)
  `R = S*(1 - Da) + D`
- [CGBlendMode.destinationIn](cgblendmode/destinationin.md)
  `R = D*Sa`
- [CGBlendMode.destinationOut](cgblendmode/destinationout.md)
  `R = D*(1 - Sa)`
- [CGBlendMode.destinationAtop](cgblendmode/destinationatop.md)
  `R = S*(1 - Da) + D*Sa`
- [CGBlendMode.xor](cgblendmode/xor.md)
  `R = S*(1 - Da) + D*(1 - Sa)`. This XOR mode is only nominally related to the classical bitmap XOR operation, which is not supported by Core Graphics
- [CGBlendMode.plusDarker](cgblendmode/plusdarker.md)
  `R = MAX(0, 1 - ((1 - D) + (1 - S)))`
- [CGBlendMode.plusLighter](cgblendmode/pluslighter.md)
  `R = MIN(1, S + D)`
### Initializers
- [init?(rawValue: Int32)](cgblendmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func flush()](cgcontext/flush.md)
  Forces all pending drawing operations in a window context to be rendered immediately to the destination device.
- [func synchronize()](cgcontext/synchronize.md)
  Marks a window context for update.
- [func setBlendMode(CGBlendMode)](cgcontext/setblendmode(_:).md)
  Sets how sample values are composited by a graphics context.
- [func setRenderingIntent(CGColorRenderingIntent)](cgcontext/setrenderingintent(_:).md)
  Sets the rendering intent in the current graphics state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgblendmode)*