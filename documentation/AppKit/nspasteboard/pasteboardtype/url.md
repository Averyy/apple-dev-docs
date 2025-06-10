# URL

**Framework**: AppKit  
**Kind**: property

URL data for one file or resource.

**Availability**:
- macOS 10.13+

## Declaration

```swift
static let URL: NSPasteboard.PasteboardType
```

#### Discussion

In macOS 10.6 and later, use [`writeObjects(_:)`](nspasteboard/writeobjects(_:).md) to write URLs directly to the pasteboard instead.

In macOS 10.5 and earlier, write an URL to a pasteboard using the [`write(to:)`](https://developer.apple.com/documentation/Foundation/NSURL/write(to:)) method of [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL). To get an URL from a pasteboard, use the [`init(fromPasteboard:)`](https://developer.apple.com/documentation/Foundation/NSURL/init(fromPasteboard:)) method of [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL).

## See Also

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
- [static let string: NSPasteboard.PasteboardType](nspasteboard/pasteboardtype/string.md)
  String data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/pasteboardtype/url)*