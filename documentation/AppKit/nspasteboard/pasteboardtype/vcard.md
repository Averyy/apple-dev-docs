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
- [NSColorPboardType](../../nscolorpboardtype.md)
  `NSColor` data.
- [NSFilenamesPboardType](../../nsfilenamespboardtype.md)
  An array of `NSString` objects designating one or more filenames.
- [NSFontPboardType](../../nsfontpboardtype.md)
  Font and character information.
- [NSHTMLPboardType](../../nshtmlpboardtype.md)
  HTML (which an `NSTextView` object can read from, but not write to).
- [NSMultipleTextSelectionPboardType](../../nsmultipletextselectionpboardtype.md)
  Multiple text selection.
- [NSPDFPboardType](../../nspdfpboardtype.md)
  PDF data.
- [NSPICTPboardType](../../nspictpboardtype.md)
  QuickDraw picture data.
- [NSRTFDPboardType](../../nsrtfdpboardtype.md)
  RTFD formatted file contents.
- [NSRTFPboardType](../../nsrtfpboardtype.md)
  Rich Text Format (RTF) data.
- [NSRulerPboardType](../../nsrulerpboardtype.md)
  Paragraph formatting information.
- [NSStringPboardType](../../nsstringpboardtype.md)
  `NSString` data.
- [NSTIFFPboardType](../../nstiffpboardtype.md)
  `NSString` data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/pasteboardtype/vcard)*