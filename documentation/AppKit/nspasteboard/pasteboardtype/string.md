# string

**Framework**: AppKit  
**Kind**: property

String data.

**Availability**:
- macOS 10.6+

## Declaration

```swift
static let string: NSPasteboard.PasteboardType
```

## Mentions

- [Supporting Writing Tools via the pasteboard](supporting-writing-tools-via-the-pasteboard.md)

#### Discussion

Apps that adopt App Sandbox cannot access files identified using the [`string`](nspasteboard/pasteboardtype/string.md) pasteboard type. Instead, use an [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL) object, a bookmark, or a filename pasteboard type.

## See Also

- [static let URL: NSPasteboard.PasteboardType](nspasteboard/pasteboardtype/url.md)
  URL data for one file or resource.
- [static let collaborationMetadata: NSPasteboard.PasteboardType](nspasteboard/pasteboardtype/collaborationmetadata.md)
  An object you use for conveying data during a collaboration.
- [static let color: NSPasteboard.PasteboardType](nspasteboard/pasteboardtype/color.md)
  Color data.
- [static let fileContents: NSPasteboard.PasteboardType](nspasteboard/pasteboardtype/filecontents.md)
  A representation of a file’s contents.
- [static let fileURL: NSPasteboard.PasteboardType](nspasteboard/pasteboardtype/fileurl.md)
  A file URL.
- [static let findPanelSearchOptions: NSPasteboard.PasteboardType](nspasteboard/pasteboardtype/findpanelsearchoptions.md)
  Type for the find panel metadata property list.
- [static let font: NSPasteboard.PasteboardType](nspasteboard/pasteboardtype/font.md)
  Font and character information.
- [static let html: NSPasteboard.PasteboardType](nspasteboard/pasteboardtype/html.md)
  Type for HTML content.
- [static let multipleTextSelection: NSPasteboard.PasteboardType](nspasteboard/pasteboardtype/multipletextselection.md)
  Multiple text selection.
- [static let pdf: NSPasteboard.PasteboardType](nspasteboard/pasteboardtype/pdf.md)
  PDF data.
- [static let png: NSPasteboard.PasteboardType](nspasteboard/pasteboardtype/png.md)
  PNG image data.
- [static let rtf: NSPasteboard.PasteboardType](nspasteboard/pasteboardtype/rtf.md)
  Rich Text Format (RTF) data.
- [static let rtfd: NSPasteboard.PasteboardType](nspasteboard/pasteboardtype/rtfd.md)
  RTFD formatted file contents.
- [static let ruler: NSPasteboard.PasteboardType](nspasteboard/pasteboardtype/ruler.md)
  Paragraph formatting information.
- [static let sound: NSPasteboard.PasteboardType](nspasteboard/pasteboardtype/sound.md)
  Sound data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/pasteboardtype/string)*