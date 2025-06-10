# CGColorRenderingIntent

**Framework**: Core Graphics  
**Kind**: enum

Handling options for colors that are not located within the destination color space of a graphics context.

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
enum CGColorRenderingIntent
```

#### Overview

The rendering intent specifies how Quartz should handle colors that are not located within the gamut of the destination color space of a graphics context. It determines the exact method used to map colors from one color space to another. If you do not explicitly set the rendering intent by calling the function [`setRenderingIntent(_:)`](cgcontext/setrenderingintent(_:).md), the graphics context uses the relative colorimetric rendering intent, except when drawing sampled images.

## Topics

### Constants
- [CGColorRenderingIntent.defaultIntent](cgcolorrenderingintent/defaultintent.md)
  The default rendering intent for the graphics context.
- [CGColorRenderingIntent.absoluteColorimetric](cgcolorrenderingintent/absolutecolorimetric.md)
- [CGColorRenderingIntent.relativeColorimetric](cgcolorrenderingintent/relativecolorimetric.md)
- [CGColorRenderingIntent.perceptual](cgcolorrenderingintent/perceptual.md)
  Preserve the visual relationship between colors by compressing the gamut of the graphics context to fit inside the gamut of the output device. Perceptual intent is good for photographs and other complex, detailed images.
- [CGColorRenderingIntent.saturation](cgcolorrenderingintent/saturation.md)
### Initializers
- [init?(rawValue: Int32)](cgcolorrenderingintent/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolorrenderingintent)*