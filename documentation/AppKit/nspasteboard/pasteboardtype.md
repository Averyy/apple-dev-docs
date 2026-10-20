# NSPasteboard.PasteboardType

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

The supported pasteboard types.

**Availability**:
- macOS

## Declaration

```swift
struct PasteboardType
```

```c
typedef NSString * NSPasteboardType;
```

## Topics

### Pasteboard Types
- [static let URL: NSPasteboard.PasteboardType](./pasteboardtype/url.md)
  URL data for one file or resource.
- [static let collaborationMetadata: NSPasteboard.PasteboardType](./pasteboardtype/collaborationmetadata.md)
  An object you use for conveying data during a collaboration.
- [static let color: NSPasteboard.PasteboardType](./pasteboardtype/color.md)
  Color data.
- [static let fileContents: NSPasteboard.PasteboardType](./pasteboardtype/filecontents.md)
  A representation of a file’s contents.
- [static let fileURL: NSPasteboard.PasteboardType](./pasteboardtype/fileurl.md)
  A file URL.
- [static let findPanelSearchOptions: NSPasteboard.PasteboardType](./pasteboardtype/findpanelsearchoptions.md)
  Type for the find panel metadata property list.
- [static let font: NSPasteboard.PasteboardType](./pasteboardtype/font.md)
  Font and character information.
- [static let html: NSPasteboard.PasteboardType](./pasteboardtype/html.md)
  Type for HTML content.
- [static let multipleTextSelection: NSPasteboard.PasteboardType](./pasteboardtype/multipletextselection.md)
  Multiple text selection.
- [static let pdf: NSPasteboard.PasteboardType](./pasteboardtype/pdf.md)
  PDF data.
- [static let png: NSPasteboard.PasteboardType](./pasteboardtype/png.md)
  PNG image data.
- [static let rtf: NSPasteboard.PasteboardType](./pasteboardtype/rtf.md)
  Rich Text Format (RTF) data.
- [static let rtfd: NSPasteboard.PasteboardType](./pasteboardtype/rtfd.md)
  RTFD formatted file contents.
- [static let ruler: NSPasteboard.PasteboardType](./pasteboardtype/ruler.md)
  Paragraph formatting information.
- [static let sound: NSPasteboard.PasteboardType](./pasteboardtype/sound.md)
  Sound data.
- [static let string: NSPasteboard.PasteboardType](./pasteboardtype/string.md)
  String data.
- [static let tabularText: NSPasteboard.PasteboardType](./pasteboardtype/tabulartext.md)
  Tab-separated fields of text.
- [static let textFinderOptions: NSPasteboard.PasteboardType](./pasteboardtype/textfinderoptions.md)
  Type for the Find panel metadata property list.
- [static let tiff: NSPasteboard.PasteboardType](./pasteboardtype/tiff.md)
  Tag Image File Format (TIFF) data.
### Option Keys
- [NSPasteboard.PasteboardType.FindPanelSearchOptionKey](./pasteboardtype/findpanelsearchoptionkey.md)
  Search options for the find panel.
- [NSPasteboard.PasteboardType.TextFinderOptionKey](./pasteboardtype/textfinderoptionkey.md)
  Search options for text in Finder.
### Initializers
- [init(String)](./pasteboardtype/init%28_%29.md)
- [init(rawValue: String)](./pasteboardtype/init%28rawvalue%29.md)
### Deprecated
- [var representedPathExtension: String?](./pasteboardtype/representedpathextension.md)
  A file type based on the passed pasteboard type.
- [static func fileContentsType(forPathExtension: String) -> NSPasteboard.PasteboardType!](./pasteboardtype/filecontentstype%28forpathextension%29.md)
  Returns a pasteboard type based on the passed file type.
- [static func fileNameType(forPathExtension: String) -> NSPasteboard.PasteboardType!](./pasteboardtype/filenametype%28forpathextension%29.md)
  Returns a pasteboard type based on the passed file type.
- [static func representedPathExtensions(from: [NSPasteboard.PasteboardType]) -> [String]?](./pasteboardtype/representedpathextensions%28from%29.md)
  Returns an array of file types based on the passed pasteboard types.
- [Deprecated symbols](../pasteboardtype-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Writing data
- [func clearContents() -> Int](./clearcontents%28%29.md)
  Clears the existing contents of the pasteboard.
- [func writeObjects([any NSPasteboardWriting]) -> Bool](./writeobjects%28_%29.md)
  Writes an array of objects to the receiver.
- [func setData(Data?, forType: NSPasteboard.PasteboardType) -> Bool](./setdata%28_,fortype%29.md)
  Sets the data as the representation for the specified type for the first item on the receiver.
- [func setPropertyList(Any, forType: NSPasteboard.PasteboardType) -> Bool](./setpropertylist%28_,fortype%29.md)
  Sets the given property list as the representation for the specified type for the first item on the receiver.
- [func setString(String, forType: NSPasteboard.PasteboardType) -> Bool](./setstring%28_,fortype%29.md)
  Sets the given string as the representation for the specified type for the first item on the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/pasteboardtype)*