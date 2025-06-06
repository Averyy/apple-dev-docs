# CGBlendMode.destinationAtop

**Framework**: Core Graphics  
**Kind**: case

`R = S*(1 - Da) + D*Sa`

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
case destinationAtop
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgblendmode/destinationatop)*