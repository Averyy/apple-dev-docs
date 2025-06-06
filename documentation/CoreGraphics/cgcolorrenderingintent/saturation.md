# CGColorRenderingIntent.saturation

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
case saturation
```

#### Discussion

Preserve the relative saturation value of the colors when converting into the gamut of the output device. The result is an image with bright, saturated colors. Saturation intent is good for reproducing images with low detail, such as presentation charts and graphs.

## See Also

- [CGColorRenderingIntent.defaultIntent](cgcolorrenderingintent/defaultintent.md)
  The default rendering intent for the graphics context.
- [CGColorRenderingIntent.absoluteColorimetric](cgcolorrenderingintent/absolutecolorimetric.md)
- [CGColorRenderingIntent.relativeColorimetric](cgcolorrenderingintent/relativecolorimetric.md)
- [CGColorRenderingIntent.perceptual](cgcolorrenderingintent/perceptual.md)
  Preserve the visual relationship between colors by compressing the gamut of the graphics context to fit inside the gamut of the output device. Perceptual intent is good for photographs and other complex, detailed images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolorrenderingintent/saturation)*