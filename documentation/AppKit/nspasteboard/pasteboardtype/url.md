# URL

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

URL data for one file or resource.

**Availability**:
- macOS 10.13+

## Declaration

```swift
static let URL: NSPasteboard.PasteboardType
```

```c
extern NSPasteboardType const NSPasteboardTypeURL;
```

#### Discussion

In macOS 10.6 and later, use [`writeObjects(_:)`](../writeobjects%28_%29.md) to write URLs directly to the pasteboard instead.

In macOS 10.5 and earlier, write an URL to a pasteboard using the [`write(to:)`](../../../Foundation/nsurl/write%28to%29.md) method of [`NSURL`](../../../Foundation/nsurl.md). To get an URL from a pasteboard, use the [`init(fromPasteboard:)`](../../../Foundation/nsurl/init%28frompasteboard%29.md) method of [`NSURL`](../../../Foundation/nsurl.md).

## See Also

### Pasteboard Types
- [static let collaborationMetadata: NSPasteboard.PasteboardType](./collaborationmetadata.md)
  An object you use for conveying data during a collaboration.
- [static let color: NSPasteboard.PasteboardType](./color.md)
  Color data.
- [static let fileContents: NSPasteboard.PasteboardType](./filecontents.md)
  A representation of a file’s contents.
- [static let fileURL: NSPasteboard.PasteboardType](./fileurl.md)
  A file URL.
- [static let findPanelSearchOptions: NSPasteboard.PasteboardType](./findpanelsearchoptions.md)
  Type for the find panel metadata property list.
- [static let font: NSPasteboard.PasteboardType](./font.md)
  Font and character information.
- [static let html: NSPasteboard.PasteboardType](./html.md)
  Type for HTML content.
- [static let multipleTextSelection: NSPasteboard.PasteboardType](./multipletextselection.md)
  Multiple text selection.
- [static let pdf: NSPasteboard.PasteboardType](./pdf.md)
  PDF data.
- [static let png: NSPasteboard.PasteboardType](./png.md)
  PNG image data.
- [static let rtf: NSPasteboard.PasteboardType](./rtf.md)
  Rich Text Format (RTF) data.
- [static let rtfd: NSPasteboard.PasteboardType](./rtfd.md)
  RTFD formatted file contents.
- [static let ruler: NSPasteboard.PasteboardType](./ruler.md)
  Paragraph formatting information.
- [static let sound: NSPasteboard.PasteboardType](./sound.md)
  Sound data.
- [static let string: NSPasteboard.PasteboardType](./string.md)
  String data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/pasteboardtype/url)*