# NSColorRenderingIntent.default

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

Use the default rendering intent for the graphics context.

**Availability**:
- macOS 10.5+

## Declaration

```swift
case `default`
```

```c
NSColorRenderingIntentDefault
```

## See Also

### Constants
- [NSColorRenderingIntent.absoluteColorimetric](./absolutecolorimetric.md)
  Map colors outside of the gamut of the output device to the closest possible match inside the gamut of the output device.
- [NSColorRenderingIntent.relativeColorimetric](./relativecolorimetric.md)
  Map colors outside of the gamut of the output device to the closest possible match inside the gamut of the output device.
- [NSColorRenderingIntent.perceptual](./perceptual.md)
  Preserve the visual relationship between colors by compressing the gamut of the graphics context to fit inside the gamut of the output device.
- [NSColorRenderingIntent.saturation](./saturation.md)
  Preserve the relative saturation value of the colors when converting into the gamut of the output device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorrenderingintent/default)*