# vCard

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

VCard data.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14 (renamed: kUTTypeVCard)

## Declaration

```swift
static let vCard: NSPasteboard.PasteboardType
```

```c
extern NSPasteboardType NSVCardPboardType;
```

#### Discussion

In macOS 10.6 and later, use `(NSString *)kUTTypeVCard` instead.

## See Also

### Deprecated constants
- [static let filePromise: NSPasteboard.PasteboardType](./filepromise.md)
  Promised files.
- [static let inkText: NSPasteboard.PasteboardType](./inktext.md)
  Ink text data.
- [static let postScript: NSPasteboard.PasteboardType](./postscript.md)
  Encapsulated PostScript (EPS) code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/pasteboardtype/vcard)*