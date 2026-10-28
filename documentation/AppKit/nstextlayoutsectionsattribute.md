# NSTextLayoutSectionsAttribute

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

The layout orientations for each section.

**Availability**:
- macOS 10.7+

## Declaration

```c
extern NSAttributedStringDocumentAttributeKey NSTextLayoutSectionsAttribute;
```

## Discussion

An [`NSArray`](../Foundation/nsarray.md) containing [`NSDictionary`](../Foundation/nsdictionary.md) objects, each dictionary describing a layout orientation section. The dictionary can have two attributes: [`NSTextLayoutSectionOrientation`](./nstextlayoutsectionorientation.md) and [`NSTextLayoutSectionRange`](./nstextlayoutsectionrange.md). When there is a gap between sections, it’s assumed to have [`NSLayoutManager.TextLayoutOrientation.horizontal`](./nslayoutmanager/textlayoutorientation/horizontal.md).

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
- [NSTopMarginDocumentAttribute](./nstopmargindocumentattribute.md)
  The top margin of the document.
- [NSViewModeDocumentAttribute](./nsviewmodedocumentattribute.md)
  The view mode.
- [NSViewSizeDocumentAttribute](./nsviewsizedocumentattribute.md)
  The view size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutsectionsattribute)*