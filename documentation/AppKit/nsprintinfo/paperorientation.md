# NSPrintInfo.PaperOrientation

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the orientation of printing on a page.

**Availability**:
- macOS 10.9+

## Declaration

```swift
enum PaperOrientation
```

```c
enum NSPaperOrientation : NSInteger;
```

## Topics

### Orientations
- [NSPrintInfo.PaperOrientation.portrait](./paperorientation/portrait.md)
  Pages are printed in portrait orientation.
- [NSPrintInfo.PaperOrientation.landscape](./paperorientation/landscape.md)
  Pages are printed in landscape orientation.
### Initializers
- [init?(rawValue: Int)](./paperorientation/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing the Printing Rectangle
- [var paperSize: NSSize](./papersize.md)
  The size of the paper.
- [var topMargin: CGFloat](./topmargin.md)
  The top margin to the specified size.
- [var bottomMargin: CGFloat](./bottommargin.md)
  The height of the bottom margin.
- [var leftMargin: CGFloat](./leftmargin.md)
  The width of the left margin.
- [var rightMargin: CGFloat](./rightmargin.md)
  The width of the right margin.
- [var imageablePageBounds: NSRect](./imageablepagebounds.md)
  The imageable area of a sheet of paper specified by the print info.
- [var orientation: NSPrintInfo.PaperOrientation](./orientation-swift.property.md)
  The orientation attribute.
- [var paperName: NSPrinter.PaperName?](./papername.md)
  The name of the currently selected paper size.
- [NSPrinter.PaperName](../nsprinter/papername.md)
  The type you use to specify the name of a type of paper.
- [var localizedPaperName: String?](./localizedpapername.md)
  The human-readable name of the currently selected paper size, suitable for presentation in user interfaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintinfo/paperorientation)*