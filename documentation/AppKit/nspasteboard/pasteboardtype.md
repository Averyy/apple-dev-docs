# NSPasteboard.PasteboardType

**Framework**: AppKit  
**Kind**: struct

The supported pasteboard types.

**Availability**:
- macOS ?+

## Declaration

```swift
struct PasteboardType
```

## Topics

### Pasteboard Types
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
- [static let string: NSPasteboard.PasteboardType](nspasteboard/pasteboardtype/string.md)
  String data.
- [static let tabularText: NSPasteboard.PasteboardType](nspasteboard/pasteboardtype/tabulartext.md)
  Tab-separated fields of text.
- [static let textFinderOptions: NSPasteboard.PasteboardType](nspasteboard/pasteboardtype/textfinderoptions.md)
  Type for the Find panel metadata property list.
- [static let tiff: NSPasteboard.PasteboardType](nspasteboard/pasteboardtype/tiff.md)
  Tag Image File Format (TIFF) data.
### Option Keys
- [NSPasteboard.PasteboardType.FindPanelSearchOptionKey](nspasteboard/pasteboardtype/findpanelsearchoptionkey.md)
  Search options for the find panel.
- [NSPasteboard.PasteboardType.TextFinderOptionKey](nspasteboard/pasteboardtype/textfinderoptionkey.md)
  Search options for text in Finder.
### Initializers
- [init(String)](nspasteboard/pasteboardtype/init(_:).md)
- [init(rawValue: String)](nspasteboard/pasteboardtype/init(rawvalue:).md)
### Deprecated
- [static let filePromise: NSPasteboard.PasteboardType](nspasteboard/pasteboardtype/filepromise.md)
  Promised files.
- [static let inkText: NSPasteboard.PasteboardType](nspasteboard/pasteboardtype/inktext.md)
  Ink text data.
- [static let postScript: NSPasteboard.PasteboardType](nspasteboard/pasteboardtype/postscript.md)
  Encapsulated PostScript (EPS) code.
- [static let vCard: NSPasteboard.PasteboardType](nspasteboard/pasteboardtype/vcard.md)
  VCard data.
- [var representedPathExtension: String?](nspasteboard/pasteboardtype/representedpathextension.md)
  A file type based on the passed pasteboard type.
- [static func fileContentsType(forPathExtension: String) -> NSPasteboard.PasteboardType!](nspasteboard/pasteboardtype/filecontentstype(forpathextension:).md)
  Returns a pasteboard type based on the passed file type.
- [static func fileNameType(forPathExtension: String) -> NSPasteboard.PasteboardType!](nspasteboard/pasteboardtype/filenametype(forpathextension:).md)
  Returns a pasteboard type based on the passed file type.
- [static func representedPathExtensions(from: [NSPasteboard.PasteboardType]) -> [String]?](nspasteboard/pasteboardtype/representedpathextensions(from:).md)
  Returns an array of file types based on the passed pasteboard types.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func clearContents() -> Int](nspasteboard/clearcontents.md)
  Clears the existing contents of the pasteboard.
- [func writeObjects([any NSPasteboardWriting]) -> Bool](nspasteboard/writeobjects(_:).md)
  Writes an array of objects to the receiver.
- [func setData(Data?, forType: NSPasteboard.PasteboardType) -> Bool](nspasteboard/setdata(_:fortype:).md)
  Sets the data as the representation for the specified type for the first item on the receiver.
- [func setPropertyList(Any, forType: NSPasteboard.PasteboardType) -> Bool](nspasteboard/setpropertylist(_:fortype:).md)
  Sets the given property list as the representation for the specified type for the first item on the receiver.
- [func setString(String, forType: NSPasteboard.PasteboardType) -> Bool](nspasteboard/setstring(_:fortype:).md)
  Sets the given string as the representation for the specified type for the first item on the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/pasteboardtype)*