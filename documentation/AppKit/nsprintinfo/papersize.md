# paperSize

**Framework**: AppKit  
**Kind**: property

The size of the paper.

**Availability**:
- macOS ?+

## Declaration

```swift
var paperSize: NSSize { get set }
```

#### Discussion

The size is measured in points in the user coordinate space.

## See Also

- [func dictionary() -> NSMutableDictionary](nsprintinfo/dictionary.md)
  Returns the print info’s dictionary that contains the printing attributes.
- [init(dictionary: [NSPrintInfo.AttributeKey : Any])](nsprintinfo/init(dictionary:).md)
  Returns a printing information object initialized with the parameters in the specified dictionary.
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
- [NSPrinter.PaperName](nsprinter/papername.md)
  The type you use to specify the name of a type of paper.
- [var localizedPaperName: String?](nsprintinfo/localizedpapername.md)
  The human-readable name of the currently selected paper size, suitable for presentation in user interfaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintinfo/papersize)*