# NSPrinter.PaperName

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

The type you use to specify the name of a type of paper.

**Availability**:
- macOS

## Declaration

```swift
struct PaperName
```

```c
typedef NSString * NSPrinterPaperName;
```

## Topics

### Initializers
- [init(String)](./papername/init%28_%29.md)
  Creates a paper name.
- [init(rawValue: String)](./papername/init%28rawvalue%29.md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing the Printing Rectangle
- [var paperSize: NSSize](../nsprintinfo/papersize.md)
  The size of the paper.
- [var topMargin: CGFloat](../nsprintinfo/topmargin.md)
  The top margin to the specified size.
- [var bottomMargin: CGFloat](../nsprintinfo/bottommargin.md)
  The height of the bottom margin.
- [var leftMargin: CGFloat](../nsprintinfo/leftmargin.md)
  The width of the left margin.
- [var rightMargin: CGFloat](../nsprintinfo/rightmargin.md)
  The width of the right margin.
- [var imageablePageBounds: NSRect](../nsprintinfo/imageablepagebounds.md)
  The imageable area of a sheet of paper specified by the print info.
- [var orientation: NSPrintInfo.PaperOrientation](../nsprintinfo/orientation-swift.property.md)
  The orientation attribute.
- [NSPrintInfo.PaperOrientation](../nsprintinfo/paperorientation.md)
  Constants that describe the orientation of printing on a page.
- [var paperName: NSPrinter.PaperName?](../nsprintinfo/papername.md)
  The name of the currently selected paper size.
- [var localizedPaperName: String?](../nsprintinfo/localizedpapername.md)
  The human-readable name of the currently selected paper size, suitable for presentation in user interfaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprinter/papername)*