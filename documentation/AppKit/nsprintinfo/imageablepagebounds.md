# imageablePageBounds

**Framework**: AppKit  
**Kind**: property

The imageable area of a sheet of paper specified by the print info.

**Availability**:
- macOS ?+

## Declaration

```swift
var imageablePageBounds: NSRect { get }
```

#### Discussion

This property takes into account the current printer, paper size, and orientation settings, but not scaling factors. “Imageable area” is the maximum area that can possibly be marked on by the printer hardware, not the area defined by the current margin settings.

The origin (0, 0) of the rectangle is in the lower-left corner of the oriented sheet. The imageable bounds may extend past the edges of the sheet when, for example, a printer driver specifies it so that borderless printing can be done reliably.

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintinfo/imageablepagebounds)*