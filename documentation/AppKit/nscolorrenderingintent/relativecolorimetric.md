# NSColorRenderingIntent.relativeColorimetric

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

Map colors outside of the gamut of the output device to the closest possible match inside the gamut of the output device.

**Availability**:
- macOS 10.5+

## Declaration

```swift
case relativeColorimetric
```

```c
NSColorRenderingIntentRelativeColorimetric
```

## Discussion

This operation can produce a clipping effect, where two different color values in the gamut of the graphics context are mapped to the same color value in the output device’s gamut. The relative colorimetric shifts all colors (including those within the gamut) to account for the difference between the white point of the graphics context and the white point of the output device.

## See Also

### Constants
- [NSColorRenderingIntent.default](./default.md)
  Use the default rendering intent for the graphics context.
- [NSColorRenderingIntent.absoluteColorimetric](./absolutecolorimetric.md)
  Map colors outside of the gamut of the output device to the closest possible match inside the gamut of the output device.
- [NSColorRenderingIntent.perceptual](./perceptual.md)
  Preserve the visual relationship between colors by compressing the gamut of the graphics context to fit inside the gamut of the output device.
- [NSColorRenderingIntent.saturation](./saturation.md)
  Preserve the relative saturation value of the colors when converting into the gamut of the output device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorrenderingintent/relativecolorimetric)*