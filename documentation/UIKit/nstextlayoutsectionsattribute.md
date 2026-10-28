# NSTextLayoutSectionsAttribute

**Framework**: UIKit  
**Kind**: var  
**Role**: Global Variable

The layout orientations for each section.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern NSAttributedStringDocumentAttributeKey const NSTextLayoutSectionsAttribute;
```

## Discussion

An [NSArray](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/OldStylePlists/OldStylePLists.html#//apple_ref/doc/uid/20001012-47205) containing [`NSDictionary`](../Foundation/nsdictionary.md) objects, each dictionary describing a layout orientation section. The dictionary can have two attributes: [`NSTextLayoutSectionOrientation`](./nstextlayoutsectionorientation.md) and [`NSTextLayoutSectionRange`](./nstextlayoutsectionrange.md). When there is a gap between sections, it’s assumed to have [`NSLayoutManager.TextLayoutOrientation.horizontal`](./nslayoutmanager/textlayoutorientation/horizontal.md).

## See Also

### Getting document appearance keys
- [NSAppearanceDocumentAttribute](../AppKit/nsappearancedocumentattribute.md)
  The appearance of the document.
- [NSBackgroundColorDocumentAttribute](./nsbackgroundcolordocumentattribute.md)
  The background color of the document.
- [NSBottomMarginDocumentAttribute](../AppKit/nsbottommargindocumentattribute.md)
  The bottom margin of the document.
- [NSDefaultFontExcludedDocumentAttribute](./nsdefaultfontexcludeddocumentattribute.md)
- [NSDefaultTabIntervalDocumentAttribute](./nsdefaulttabintervaldocumentattribute.md)
  The default tab stop interval for the document.
- [NSExcludedElementsDocumentAttribute](../AppKit/nsexcludedelementsdocumentattribute.md)
  The HTML elements to exclude in generated HTML.
- [NSHyphenationFactorDocumentAttribute](./nshyphenationfactordocumentattribute.md)
  The hyphenation factor of the document.
- [NSLeftMarginDocumentAttribute](../AppKit/nsleftmargindocumentattribute.md)
  The left margin of the document.
- [NSPaperMarginDocumentAttribute](./nspapermargindocumentattribute.md)
  The paper margin of the document.
- [NSPaperSizeDocumentAttribute](./nspapersizedocumentattribute.md)
  The paper size for the document.
- [NSPrefixSpacesDocumentAttribute](../AppKit/nsprefixspacesdocumentattribute.md)
  The number of spaces for indenting nested HTML elements.
- [NSRightMarginDocumentAttribute](../AppKit/nsrightmargindocumentattribute.md)
  The right margin of the document.
- [NSTopMarginDocumentAttribute](../AppKit/nstopmargindocumentattribute.md)
  The top margin of the document.
- [NSViewModeDocumentAttribute](./nsviewmodedocumentattribute.md)
  The view mode.
- [NSViewSizeDocumentAttribute](./nsviewsizedocumentattribute.md)
  The view size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutsectionsattribute)*