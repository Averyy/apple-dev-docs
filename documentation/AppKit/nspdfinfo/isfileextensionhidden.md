# isFileExtensionHidden

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the file extension should appear after the filename.

**Availability**:
- macOS 10.9+

## Declaration

```swift
var isFileExtensionHidden: Bool { get set }
```

```objc
@property (getter=isFileExtensionHidden) BOOL fileExtensionHidden;
```

## See Also

### Specifying PDF Information
- [var url: URL?](./url.md)
  The URL identifying the location at which the PDF file will be created.
- [var tagNames: [String]](./tagnames.md)
  An array of tag names that should be applied to the PDF file after it’s created.
- [var orientation: NSPrintInfo.PaperOrientation](./orientation.md)
  The paper orientation to use when exporting content as a PDF file.
- [var paperSize: NSSize](./papersize.md)
  The paper size to use when exporting content as a PDF file.
- [var attributes: NSMutableDictionary](./attributes.md)
  A dictionary of additional attributes that describe how to export content as a PDF file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspdfinfo/isfileextensionhidden)*