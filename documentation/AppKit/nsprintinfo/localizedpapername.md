# localizedPaperName

**Framework**: AppKit  
**Kind**: property

The human-readable name of the currently selected paper size, suitable for presentation in user interfaces.

**Availability**:
- macOS ?+

## Declaration

```swift
var localizedPaperName: String? { get }
```

#### Discussion

This is typically different from the value of [`paperName`](nsprintinfo/papername.md), which is almost never suitable for presentation to the user.

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
- [NSPrinter.PaperName](nsprinter/papername.md)
  The type you use to specify the name of a type of paper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintinfo/localizedpapername)*