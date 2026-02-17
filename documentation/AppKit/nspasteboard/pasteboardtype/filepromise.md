# filePromise

**Framework**: AppKit  
**Kind**: property

Promised files.

**Availability**:
- macOS 10.0+

## Declaration

```swift
static let filePromise: NSPasteboard.PasteboardType
```

#### Discussion

In macOS 10.6 and later, use `(NSString *)kPasteboardTypeFileURLPromise` instead.

For more information, see [`Supporting Drag and Drop Through File Promises`](supporting-drag-and-drop-through-file-promises.md).

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/pasteboardtype/filepromise)*