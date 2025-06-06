# attributes

**Framework**: AppKit  
**Kind**: property

A dictionary of additional attributes that describe how to export content as a PDF file.

**Availability**:
- macOS 10.9+

## Declaration

```swift
var attributes: NSMutableDictionary { get }
```

#### Discussion

Although `attributes` is a read-only property, you can modify the mutable dictionary associated with it. Typically, this dictionary contains custom attributes or parameters that are set by a custom accessory view in the PDF panel.

## See Also

- [var url: URL?](nspdfinfo/url.md)
  The URL identifying the location at which the PDF file will be created.
- [var isFileExtensionHidden: Bool](nspdfinfo/isfileextensionhidden.md)
  A Boolean value that indicates whether the file extension should appear after the filename.
- [var tagNames: [String]](nspdfinfo/tagnames.md)
  An array of tag names that should be applied to the PDF file after it’s created.
- [var orientation: NSPrintInfo.PaperOrientation](nspdfinfo/orientation.md)
  The paper orientation to use when exporting content as a PDF file.
- [var paperSize: NSSize](nspdfinfo/papersize.md)
  The paper size to use when exporting content as a PDF file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspdfinfo/attributes)*