# NSImage.ResizingMode

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the resizing mode for the image.

**Availability**:
- macOS 10.10+

## Declaration

```swift
enum ResizingMode
```

```c
enum NSImageResizingMode : NSInteger;
```

## Topics

### Constants
- [NSImage.ResizingMode.tile](./resizingmode-swift.enum/tile.md)
  The image tiles when it resizes.
- [NSImage.ResizingMode.stretch](./resizingmode-swift.enum/stretch.md)
  The image stretches when it resizes.
### Initializers
- [init?(rawValue: Int)](./resizingmode-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing Drawing Options
- [var isValid: Bool](./isvalid.md)
  A Boolean value that indicates whether it is possible to draw an image representation.
- [var backgroundColor: NSColor](./backgroundcolor.md)
  The background color for the image.
- [var capInsets: NSEdgeInsets](./capinsets.md)
  The cap insets for the image.
- [var resizingMode: NSImage.ResizingMode](./resizingmode-swift.property.md)
  The resizing mode for the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/resizingmode-swift.enum)*