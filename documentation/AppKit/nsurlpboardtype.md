# NSURLPboardType

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

`NSURL` data for one file or resource.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

## Declaration

```c
extern NSPasteboardType NSURLPboardType;
```

#### Discussion

In macOS 10.6 and later, use [`writeObjects(_:)`](./nspasteboard/writeobjects%28_%29.md) to write URLs directly to the pasteboard instead.

In OS X v10.5 and earlier: to write an URL to a pasteboard you use [`write(to:)`](../Foundation/nsurl/write%28to%29.md) ([`NSURL`](../Foundation/nsurl.md)); to get an URL from a pasteboard you use [`init(fromPasteboard:)`](../Foundation/nsurl/init%28frompasteboard%29.md) ([`NSURL`](../Foundation/nsurl.md)).

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsurlpboardtype)*