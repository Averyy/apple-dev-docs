# NSPrintInfo.Orientation

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify page orientations.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14 (renamed: NSPaperOrientation)

## Declaration

```swift
enum Orientation
```

```c
enum NSPrintingOrientation : NSUInteger;
```

## Topics

### Constants
- [NSPrintInfo.Orientation.portraitOrientation](./orientation-swift.enum/portraitorientation.md)
  Orientation is portrait (page is taller than it is wide).
- [NSPrintInfo.Orientation.landscapeOrientation](./orientation-swift.enum/landscapeorientation.md)
  Orientation is landscape (page is wider than it is tall).
### Initializers
- [init?(rawValue: UInt)](./orientation-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Deprecated
- [class var defaultPrinter: NSPrinter?](./defaultprinter.md)
  Deprecated.
- [Deprecated Printing Keys](../deprecated-printing-keys.md)
  These keys refer to older printing properties that are no longer used.
- [+ setDefaultPrinter:](./setdefaultprinter_.md)
  Deprecated.
- [+ sizeForPaperName:](./sizeforpapername_.md)
  Deprecated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintinfo/orientation-swift.enum)*