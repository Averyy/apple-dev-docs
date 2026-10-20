# filePromise

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Promised files.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

## Declaration

```swift
static let filePromise: NSPasteboard.PasteboardType
```

```c
extern NSPasteboardType NSFilesPromisePboardType;
```

#### Discussion

In macOS 10.6 and later, use `(NSString *)kPasteboardTypeFileURLPromise` instead.

For more information, see [Supporting Drag and Drop Through File Promises](../../supporting-drag-and-drop-through-file-promises.md).

## See Also

### Deprecated constants
- [static let inkText: NSPasteboard.PasteboardType](./inktext.md)
  Ink text data.
- [static let postScript: NSPasteboard.PasteboardType](./postscript.md)
  Encapsulated PostScript (EPS) code.
- [static let vCard: NSPasteboard.PasteboardType](./vcard.md)
  VCard data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/pasteboardtype/filepromise)*