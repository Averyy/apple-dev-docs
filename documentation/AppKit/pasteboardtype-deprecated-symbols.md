# Deprecated symbols

**Framework**: AppKit  
**Role**: API Collection

Review symbols that are no longer in active development, and their recommended replacements.

#### Overview

Although these symbols are available for use, Apple is no longer actively developing them, and may remove them in a future release. Apple recommends moving away from these symbols and using their indicated replacements instead. Check the individual symbol pages for the recommended replacements.

## Topics

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
- [NSTIFFPboardType](./nstiffpboardtype.md)
  `NSString` data.
- [NSTabularTextPboardType](./nstabulartextpboardtype.md)
  An `NSString` object containing tab-separated fields of text.
- [NSURLPboardType](./nsurlpboardtype.md)
  `NSURL` data for one file or resource.
- [NSPasteboardTypeFindPanelSearchOptions](./nspasteboardtypefindpanelsearchoptions.md)
  Type for the Find panel metadata property list.

## See Also

### Deprecated
- [var representedPathExtension: String?](./nspasteboard/pasteboardtype/representedpathextension.md)
  A file type based on the passed pasteboard type.
- [static func fileContentsType(forPathExtension: String) -> NSPasteboard.PasteboardType!](./nspasteboard/pasteboardtype/filecontentstype%28forpathextension%29.md)
  Returns a pasteboard type based on the passed file type.
- [static func fileNameType(forPathExtension: String) -> NSPasteboard.PasteboardType!](./nspasteboard/pasteboardtype/filenametype%28forpathextension%29.md)
  Returns a pasteboard type based on the passed file type.
- [static func representedPathExtensions(from: [NSPasteboard.PasteboardType]) -> [String]?](./nspasteboard/pasteboardtype/representedpathextensions%28from%29.md)
  Returns an array of file types based on the passed pasteboard types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/pasteboardtype-deprecated-symbols)*