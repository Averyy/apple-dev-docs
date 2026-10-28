# NSTIFFPboardType

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

`NSString` data.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: In apps that adopt App Sandbox, use an [`NSURL`](../Foundation/nsurl.md) object, a bookmark, or a filename pasteboard type instead. In a nonsandboxed app, you can also use the [`string`](./nspasteboard/pasteboardtype/string.md) pasteboard type.

## Declaration

```c
extern NSPasteboardType NSTIFFPboardType;
```

## Discussion

In macOS 10.6 and later, use [`tiff`](./nspasteboard/pasteboardtype/tiff.md) instead.

## See Also

### Deprecated constants
- [static let filePromise: NSPasteboard.PasteboardType](./nspasteboard/pasteboardtype/filepromise.md)
  Promised files.
- [static let inkText: NSPasteboard.PasteboardType](./nspasteboard/pasteboardtype/inktext.md)
  Ink text data.
- [static let postScript: NSPasteboard.PasteboardType](./nspasteboard/pasteboardtype/postscript.md)
  Encapsulated PostScript (EPS) code.
- [static let vCard: NSPasteboard.PasteboardType](./nspasteboard/pasteboardtype/vcard.md)
  VCard data.
- [NSColorPboardType](./nscolorpboardtype.md)
  `NSColor` data.
- [NSFilenamesPboardType](./nsfilenamespboardtype.md)
  An array of `NSString` objects designating one or more filenames.
- [NSFontPboardType](./nsfontpboardtype.md)
  Font and character information.
- [NSHTMLPboardType](./nshtmlpboardtype.md)
  HTML (which an `NSTextView` object can read from, but not write to).
- [NSMultipleTextSelectionPboardType](./nsmultipletextselectionpboardtype.md)
  Multiple text selection.
- [NSPDFPboardType](./nspdfpboardtype.md)
  PDF data.
- [NSPICTPboardType](./nspictpboardtype.md)
  QuickDraw picture data.
- [NSRTFDPboardType](./nsrtfdpboardtype.md)
  RTFD formatted file contents.
- [NSRTFPboardType](./nsrtfpboardtype.md)
  Rich Text Format (RTF) data.
- [NSRulerPboardType](./nsrulerpboardtype.md)
  Paragraph formatting information.
- [NSStringPboardType](./nsstringpboardtype.md)
  `NSString` data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstiffpboardtype)*