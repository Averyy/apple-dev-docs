# CGColorRenderingIntent.absoluteColorimetric

**Framework**: Core Graphics  
**Kind**: case

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
case absoluteColorimetric
```

#### Discussion

Map colors outside of the gamut of the output device to the closest possible match inside the gamut of the output device. This can produce a clipping effect, where two different color values in the gamut of the graphics context are mapped to the same color value in the output device’s gamut. Unlike the relative colorimetric, absolute colorimetric does not modify colors inside the gamut of the output device.

## See Also

- [CGColorRenderingIntent.defaultIntent](cgcolorrenderingintent/defaultintent.md)
  The default rendering intent for the graphics context.
- [CGColorRenderingIntent.relativeColorimetric](cgcolorrenderingintent/relativecolorimetric.md)
- [CGColorRenderingIntent.perceptual](cgcolorrenderingintent/perceptual.md)
  Preserve the visual relationship between colors by compressing the gamut of the graphics context to fit inside the gamut of the output device. Perceptual intent is good for photographs and other complex, detailed images.
- [CGColorRenderingIntent.saturation](cgcolorrenderingintent/saturation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolorrenderingintent/absolutecolorimetric)*