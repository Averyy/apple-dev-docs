# NSPrinter.PaperName

**Framework**: AppKit  
**Kind**: struct

The type you use to specify the name of a type of paper.

**Availability**:
- macOS ?+

## Declaration

```swift
struct PaperName
```

## Topics

### Initializers
- [init(String)](nsprinter/papername/init(_:).md)
  Creates a paper name.
- [init(rawValue: String)](nsprinter/papername/init(rawvalue:).md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
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
- [NSPrintInfo.PaperOrientation](nsprintinfo/paperorientation.md)
  Constants that describe the orientation of printing on a page.
- [var paperName: NSPrinter.PaperName?](nsprintinfo/papername.md)
  The name of the currently selected paper size.
- [var localizedPaperName: String?](nsprintinfo/localizedpapername.md)
  The human-readable name of the currently selected paper size, suitable for presentation in user interfaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprinter/papername)*