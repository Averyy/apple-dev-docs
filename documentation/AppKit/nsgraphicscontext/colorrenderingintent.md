# colorRenderingIntent

**Framework**: AppKit  
**Kind**: property

The color rendering intent in the graphics context’s graphics state.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var colorRenderingIntent: NSColorRenderingIntent { get set }
```

#### Discussion

A value that specifies the rendering intent currently used by the graphics context. For possible values, see [`NSColorRenderingIntent`](nscolorrenderingintent.md). The rendering intent specifies how Cocoa should handle colors that are not located within the gamut of the destination color space of a graphics context. If you do not explicitly set the rendering intent, and sampled images are being drawn, [`NSGraphicsContext`](nsgraphicscontext.md) uses perceptual rendering intent. Otherwise, [`NSGraphicsContext`](nsgraphicscontext.md) uses relative colorimetric rendering intent.

## See Also

- [enum NSColorRenderingIntent](nscolorrenderingintent.md)
  Constants that specify how Cocoa should handle colors that are not located within the destination color space of a graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/colorrenderingintent)*