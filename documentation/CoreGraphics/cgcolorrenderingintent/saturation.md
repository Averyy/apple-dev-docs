# CGColorRenderingIntent.saturation

**Framework**: Core Graphics  
**Kind**: case  
**Role**: Case

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
case saturation
```

```c
kCGRenderingIntentSaturation
```

#### Discussion

Preserve the relative saturation value of the colors when converting into the gamut of the output device. The result is an image with bright, saturated colors. Saturation intent is good for reproducing images with low detail, such as presentation charts and graphs.

## See Also

### Constants
- [CGColorRenderingIntent.defaultIntent](./defaultintent.md)
  The default rendering intent for the graphics context.
- [CGColorRenderingIntent.absoluteColorimetric](./absolutecolorimetric.md)
- [CGColorRenderingIntent.relativeColorimetric](./relativecolorimetric.md)
- [CGColorRenderingIntent.perceptual](./perceptual.md)
  Preserve the visual relationship between colors by compressing the gamut of the graphics context to fit inside the gamut of the output device. Perceptual intent is good for photographs and other complex, detailed images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolorrenderingintent/saturation)*