# NSPrintInfo.PaperOrientation

**Framework**: AppKit  
**Kind**: enum

Constants that describe the orientation of printing on a page.

**Availability**:
- macOS 10.9+

## Declaration

```swift
enum PaperOrientation
```

## Topics

### Orientations
- [NSPrintInfo.PaperOrientation.portrait](nsprintinfo/paperorientation/portrait.md)
  Pages are printed in portrait orientation.
- [NSPrintInfo.PaperOrientation.landscape](nsprintinfo/paperorientation/landscape.md)
  Pages are printed in landscape orientation.
### Initializers
- [init?(rawValue: Int)](nsprintinfo/paperorientation/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var paperSize: NSSize](nsprintinfo/papersize.md)
  The size of the paper.
- [var topMargin: CGFloat](nsprintinfo/topmargin.md)
  The top margin to the specified size.
- [var bottomMargin: CGFloat](nsprintinfo/bottommargin.md)
  The height of the bottom margin.
- [var leftMargin: CGFloat](nsprintinfo/leftmargin.md)
  The width of the left margin.
- [var rightMargin: CGFloat](nsprintinfo/rightmargin.md)
  The width of the right margin.
- [var imageablePageBounds: NSRect](nsprintinfo/imageablepagebounds.md)
  The imageable area of a sheet of paper specified by the print info.
- [var orientation: NSPrintInfo.PaperOrientation](nsprintinfo/orientation-swift.property.md)
  The orientation attribute.
- [var paperName: NSPrinter.PaperName?](nsprintinfo/papername.md)
  The name of the currently selected paper size.
- [NSPrinter.PaperName](nsprinter/papername.md)
  The type you use to specify the name of a type of paper.
- [var localizedPaperName: String?](nsprintinfo/localizedpapername.md)
  The human-readable name of the currently selected paper size, suitable for presentation in user interfaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintinfo/paperorientation)*