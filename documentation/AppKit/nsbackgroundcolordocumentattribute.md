# NSBackgroundColorDocumentAttribute

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

The background color of the document.

**Availability**:
- macOS 10.0+

## Declaration

```c
extern NSAttributedStringDocumentAttributeKey NSBackgroundColorDocumentAttribute;
```

## Discussion

The value of this attribute is an [`NSColor`](./nscolor.md) object representing the document-wide page background color.

The string constant in macOS 10.3 and earlier is `@"BackgroundColor"`.

For applications linked on versions prior to macOS 10.5, HTML import sets the `NSBackgroundColorDocumentAttribute` to `[NSColor whiteColor]` in cases in which the HTML does not specify a background color. For applications linked on macOS 10.5 and later, no `NSBackgroundColorDocumentAttribute` is set in these cases.

## See Also

### Getting document appearance keys
- [NSAppearanceDocumentAttribute](./nsappearancedocumentattribute.md)
  The appearance of the document.
- [NSBottomMarginDocumentAttribute](./nsbottommargindocumentattribute.md)
  The bottom margin of the document.
- [NSDefaultFontExcludedDocumentAttribute](./nsdefaultfontexcludeddocumentattribute.md)
- [NSDefaultTabIntervalDocumentAttribute](./nsdefaulttabintervaldocumentattribute.md)
  The default tab stop interval for the document.
- [NSExcludedElementsDocumentAttribute](./nsexcludedelementsdocumentattribute.md)
  The HTML elements to exclude in generated HTML.
- [NSHyphenationFactorDocumentAttribute](./nshyphenationfactordocumentattribute.md)
  The hyphenation factor of the document.
- [NSLeftMarginDocumentAttribute](./nsleftmargindocumentattribute.md)
  The left margin of the document.
- [NSPaperMarginDocumentAttribute](./nspapermargindocumentattribute.md)
- [NSPaperSizeDocumentAttribute](./nspapersizedocumentattribute.md)
  The paper size for the document.
- [NSPrefixSpacesDocumentAttribute](./nsprefixspacesdocumentattribute.md)
  The number of spaces for indenting nested HTML elements.
- [NSRightMarginDocumentAttribute](./nsrightmargindocumentattribute.md)
  The right margin of the document.
- [NSTextLayoutSectionsAttribute](./nstextlayoutsectionsattribute.md)
  The layout orientations for each section.
- [NSTopMarginDocumentAttribute](./nstopmargindocumentattribute.md)
  The top margin of the document.
- [NSViewModeDocumentAttribute](./nsviewmodedocumentattribute.md)
  The view mode.
- [NSViewSizeDocumentAttribute](./nsviewsizedocumentattribute.md)
  The view size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbackgroundcolordocumentattribute)*