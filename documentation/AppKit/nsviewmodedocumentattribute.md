# NSViewModeDocumentAttribute

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

The view mode.

**Availability**:
- macOS 10.0+

## Declaration

```c
extern NSAttributedStringDocumentAttributeKey NSViewModeDocumentAttribute;
```

#### Discussion

The value of this attribute is an [`NSValue`](../Foundation/nsvalue.md) object containing an integer. A value of `0` indicates normal, and a value of `1` indicates page layout (use the value `@"PaperSize"`).

The string constant in macOS 10.3 and earlier is `@"ViewMode"`.

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
- [NSViewSizeDocumentAttribute](./nsviewsizedocumentattribute.md)
  The view size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewmodedocumentattribute)*