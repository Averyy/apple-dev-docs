# NSHyphenationFactorDocumentAttribute

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

The hyphenation factor of the document.

**Availability**:
- macOS 10.0+

## Declaration

```c
extern NSAttributedStringDocumentAttributeKey NSHyphenationFactorDocumentAttribute;
```

## Discussion

The value of this attribute is an [`NSNumber`](../Foundation/nsnumber.md) object containing a float. A value of `0` indicates that hyphenation is off, and a value of `1` indicates full hyphenation.

The string constant in macOS 10.3 and earlier is `@"HyphenationFactor"`.

## See Also

### Getting document appearance keys
- [NSAppearanceDocumentAttribute](./nsappearancedocumentattribute.md)
  The appearance of the document.
- [NSBackgroundColorDocumentAttribute](./nsbackgroundcolordocumentattribute.md)
  The background color of the document.
- [NSBottomMarginDocumentAttribute](./nsbottommargindocumentattribute.md)
  The bottom margin of the document.
- [NSDefaultFontExcludedDocumentAttribute](./nsdefaultfontexcludeddocumentattribute.md)
- [NSDefaultTabIntervalDocumentAttribute](./nsdefaulttabintervaldocumentattribute.md)
  The default tab stop interval for the document.
- [NSExcludedElementsDocumentAttribute](./nsexcludedelementsdocumentattribute.md)
  The HTML elements to exclude in generated HTML.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nshyphenationfactordocumentattribute)*