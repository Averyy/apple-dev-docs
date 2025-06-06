# showsOrientation

**Framework**: AppKit  
**Kind**: property

The PDF panel shows the current orientation of the PDF contents, such as landscape or portrait.

**Availability**:
- macOS 10.9+

## Declaration

```swift
static var showsOrientation: NSPDFPanel.Options { get }
```

## See Also

- [static var showsPaperSize: NSPDFPanel.Options](nspdfpanel/options-swift.struct/showspapersize.md)
  The PDF panel shows a menu of paper sizes.
- [static var requestsParentDirectory: NSPDFPanel.Options](nspdfpanel/options-swift.struct/requestsparentdirectory.md)
  The PDF panel doesn’t show a name field; instead, it allows the user to identify a directory in which to save multiple PDF files. If you set this flag, you’re responsible for appending a filename and the “pdf” extension to the resulting  URL value in the [`NSPDFInfo`](nspdfinfo.md) object before proceeding with the creation of the PDF file (or calling the `takeSettingsFromPDFInfo` method of [`NSPrintInfo`](nsprintinfo.md)).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspdfpanel/options-swift.struct/showsorientation)*