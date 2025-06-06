# NSColorRenderingIntent

**Framework**: AppKit  
**Kind**: enum

Constants that specify how Cocoa should handle colors that are not located within the destination color space of a graphics context.

**Availability**:
- macOS 10.5+

## Declaration

```swift
enum NSColorRenderingIntent
```

#### Overview

These constants are used by the property [`colorRenderingIntent`](nsgraphicscontext/colorrenderingintent.md).

## Topics

### Constants
- [NSColorRenderingIntent.default](nscolorrenderingintent/default.md)
  Use the default rendering intent for the graphics context.
- [NSColorRenderingIntent.absoluteColorimetric](nscolorrenderingintent/absolutecolorimetric.md)
  Map colors outside of the gamut of the output device to the closest possible match inside the gamut of the output device.
- [NSColorRenderingIntent.relativeColorimetric](nscolorrenderingintent/relativecolorimetric.md)
  Map colors outside of the gamut of the output device to the closest possible match inside the gamut of the output device.
- [NSColorRenderingIntent.perceptual](nscolorrenderingintent/perceptual.md)
  Preserve the visual relationship between colors by compressing the gamut of the graphics context to fit inside the gamut of the output device.
- [NSColorRenderingIntent.saturation](nscolorrenderingintent/saturation.md)
  Preserve the relative saturation value of the colors when converting into the gamut of the output device.
### Initializers
- [init?(rawValue: Int)](nscolorrenderingintent/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var colorRenderingIntent: NSColorRenderingIntent](nsgraphicscontext/colorrenderingintent.md)
  The color rendering intent in the graphics context’s graphics state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorrenderingintent)*