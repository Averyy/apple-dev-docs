# orientation

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The paper orientation to use when exporting content as a PDF file.

**Availability**:
- macOS 10.9+

## Declaration

```swift
var orientation: NSPrintInfo.PaperOrientation { get set }
```

```objc
@property NSPaperOrientation orientation;
```

## See Also

### Specifying PDF Information
- [var url: URL?](./url.md)
  The URL identifying the location at which the PDF file will be created.
- [var isFileExtensionHidden: Bool](./isfileextensionhidden.md)
  A Boolean value that indicates whether the file extension should appear after the filename.
- [var tagNames: [String]](./tagnames.md)
  An array of tag names that should be applied to the PDF file after it’s created.
- [var paperSize: NSSize](./papersize.md)
  The paper size to use when exporting content as a PDF file.
- [var attributes: NSMutableDictionary](./attributes.md)
  A dictionary of additional attributes that describe how to export content as a PDF file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspdfinfo/orientation)*