# paperName

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The name of the currently selected paper size.

**Availability**:
- macOS

## Declaration

```swift
var paperName: NSPrinter.PaperName? { get set }
```

```objc
@property (copy, nullable) NSPrinterPaperName paperName;
```

## Discussion

The string contains a value such as Letter or Legal. Paper names are implementation specific.

## See Also

### Related Documentation
- [func dictionary() -> NSMutableDictionary](./dictionary%28%29.md)
  Returns the print info’s dictionary that contains the printing attributes.
- [init(dictionary: [NSPrintInfo.AttributeKey : Any])](./init%28dictionary%29.md)
  Returns a printing information object initialized with the parameters in the specified dictionary.
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
- [NSPrintInfo.PaperOrientation](./paperorientation.md)
  Constants that describe the orientation of printing on a page.
- [NSPrinter.PaperName](../nsprinter/papername.md)
  The type you use to specify the name of a type of paper.
- [var localizedPaperName: String?](./localizedpapername.md)
  The human-readable name of the currently selected paper size, suitable for presentation in user interfaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintinfo/papername)*