# postScript

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Encapsulated PostScript (EPS) code.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

## Declaration

```swift
static let postScript: NSPasteboard.PasteboardType
```

```c
extern NSPasteboardType NSPostScriptPboardType;
```

#### Discussion

In macOS 10.6 and later, use `@"com.adobe.encapsulated-postscript"` instead.

## See Also

### Deprecated constants
- [static let filePromise: NSPasteboard.PasteboardType](./filepromise.md)
  Promised files.
- [static let inkText: NSPasteboard.PasteboardType](./inktext.md)
  Ink text data.
- [static let vCard: NSPasteboard.PasteboardType](./vcard.md)
  VCard data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/pasteboardtype/postscript)*