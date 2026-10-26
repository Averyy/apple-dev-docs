# NSPICTPboardType

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

QuickDraw picture data.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
extern NSPasteboardType NSPICTPboardType;
```

#### Discussion

The PICT format was formally deprecated in OS X v10.4 along with QuickDraw. You should not be explicitly providing or looking for PICT data on the pasteboard.

To aid in this deprecation, if PICT is the only image type on the pasteboard, as is sometimes the case when copying images from 32-bit Carbon applications, a translated image type will be automatically reported and provided by `NSPasteboard`. The translated type is added to the types array ahead of PICT so that the deprecated PICT format is not the preferred format. In addition, when an application provides image data to `NSPasteboard`, the Carbon Pasteboard Manager will automatically make a PICT translation available to 32-bit Carbon applications.

Although `NSPICTPboardType`, and its UTI equivalent `kUTTypePICT`, will appear in a pasteboard’s type array retrieved from the existing `NSPasteboard` API, it may cease to be reported in future releases.

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
- [NSRTFDPboardType](./nsrtfdpboardtype.md)
  RTFD formatted file contents.
- [NSRTFPboardType](./nsrtfpboardtype.md)
  Rich Text Format (RTF) data.
- [NSRulerPboardType](./nsrulerpboardtype.md)
  Paragraph formatting information.
- [NSStringPboardType](./nsstringpboardtype.md)
  `NSString` data.
- [NSTIFFPboardType](./nstiffpboardtype.md)
  `NSString` data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspictpboardtype)*