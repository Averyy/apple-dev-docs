# NSPrintOperation.RenderingQuality

**Framework**: AppKit  
**Kind**: enum

Constants that specify the print quality in use.

**Availability**:
- macOS 10.7+

## Declaration

```swift
enum RenderingQuality
```

## Topics

### Constants
- [NSPrintOperation.RenderingQuality.best](nsprintoperation/renderingquality/best.md)
  Renders the printing at the best possible quality, regardless of speed.
- [NSPrintOperation.RenderingQuality.responsive](nsprintoperation/renderingquality/responsive.md)
  Sacrifices the least possible amount of rendering quality for speed to maintain a responsive user interface. This option should be used only after establishing that best quality rendering does indeed make the user interface unresponsive.
### Initializers
- [init?(rawValue: Int)](nsprintoperation/renderingquality/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var preferredRenderingQuality: NSPrintOperation.RenderingQuality](nsprintoperation/preferredrenderingquality.md)
  The printing quality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/renderingquality)*