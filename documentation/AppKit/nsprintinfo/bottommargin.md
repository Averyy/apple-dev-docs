# bottomMargin

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The height of the bottom margin.

**Availability**:
- macOS

## Declaration

```swift
var bottomMargin: CGFloat { get set }
```

```objc
@property CGFloat bottomMargin;
```

## Discussion

bottomMargin is measured in points in the user coordinate space.

## See Also

### Managing the Printing Rectangle
- [var paperSize: NSSize](./papersize.md)
  The size of the paper.
- [var topMargin: CGFloat](./topmargin.md)
  The top margin to the specified size.
- [var leftMargin: CGFloat](./leftmargin.md)
  The width of the left margin.
- [var rightMargin: CGFloat](./rightmargin.md)
  The width of the right margin.
- [var imageablePageBounds: NSRect](./imageablepagebounds.md)
  The imageable area of a sheet of paper specified by the print info.
- [var orientation: NSPrintInfo.PaperOrientation](./orientation-swift.property.md)
  The orientation attribute.
- [NSPrintInfo.PaperOrientation](./paperorientation.md)
  Constants that describe the orientation of printing on a page.
- [var paperName: NSPrinter.PaperName?](./papername.md)
  The name of the currently selected paper size.
- [NSPrinter.PaperName](../nsprinter/papername.md)
  The type you use to specify the name of a type of paper.
- [var localizedPaperName: String?](./localizedpapername.md)
  The human-readable name of the currently selected paper size, suitable for presentation in user interfaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintinfo/bottommargin)*