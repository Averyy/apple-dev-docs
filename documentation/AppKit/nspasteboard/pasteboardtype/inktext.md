# inkText

**Framework**: AppKit  
**Kind**: property

Ink text data.

**Availability**:
- macOS 10.0+

## Declaration

```swift
static let inkText: NSPasteboard.PasteboardType
```

#### Discussion

In macOS 10.6 and later, use `(NSString *)kUTTypeInkText` instead.

For information on ink text objects, see Using Ink Services in Your Application.

## See Also

- [static let filePromise: NSPasteboard.PasteboardType](nspasteboard/pasteboardtype/filepromise.md)
  Promised files.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/pasteboardtype/inktext)*