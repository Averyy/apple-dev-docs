# NSPrintOperation.RenderingQuality

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the print quality in use.

**Availability**:
- macOS 10.7+

## Declaration

```swift
enum RenderingQuality
```

```c
enum NSPrintRenderingQuality : NSInteger;
```

## Topics

### Constants
- [NSPrintOperation.RenderingQuality.best](./renderingquality/best.md)
  Renders the printing at the best possible quality, regardless of speed.
- [NSPrintOperation.RenderingQuality.responsive](./renderingquality/responsive.md)
  Sacrifices the least possible amount of rendering quality for speed to maintain a responsive user interface. This option should be used only after establishing that best quality rendering does indeed make the user interface unresponsive.
### Initializers
- [init?(rawValue: Int)](./renderingquality/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the Printing Quality
- [var preferredRenderingQuality: NSPrintOperation.RenderingQuality](./preferredrenderingquality.md)
  The printing quality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/renderingquality)*