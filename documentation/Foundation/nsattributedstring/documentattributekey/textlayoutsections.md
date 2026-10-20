# textLayoutSections

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

The layout orientations for each section.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let textLayoutSections: NSAttributedString.DocumentAttributeKey
```

#### Discussion

An [NSArray](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/OldStylePlists/OldStylePLists.html#//apple_ref/doc/uid/20001012-47205) containing [`NSDictionary`](../../nsdictionary.md) objects, each dictionary describing a layout orientation section. The dictionary can have two attributes: [`orientation`](../textlayoutsectionkey/orientation.md) and [`range`](../textlayoutsectionkey/range.md). When there is a gap between sections, it’s assumed to have [`NSLayoutManager.TextLayoutOrientation.horizontal`](../../../AppKit/nslayoutmanager/textlayoutorientation/horizontal.md).

## See Also

### Getting document appearance keys
- [static let appearance: NSAttributedString.DocumentAttributeKey](./appearance.md)
  The appearance of the document.
- [static let backgroundColor: NSAttributedString.DocumentAttributeKey](./backgroundcolor.md)
  The background color of the document.
- [static let bottomMargin: NSAttributedString.DocumentAttributeKey](./bottommargin.md)
  The bottom margin of the document.
- [static let defaultFontExcluded: NSAttributedString.DocumentAttributeKey](./defaultfontexcluded.md)
- [static let defaultTabInterval: NSAttributedString.DocumentAttributeKey](./defaulttabinterval.md)
  The default tab stop interval for the document.
- [static let excludedElements: NSAttributedString.DocumentAttributeKey](./excludedelements.md)
  The HTML elements to exclude in generated HTML.
- [static let hyphenationFactor: NSAttributedString.DocumentAttributeKey](./hyphenationfactor.md)
  The hyphenation factor of the document.
- [static let leftMargin: NSAttributedString.DocumentAttributeKey](./leftmargin.md)
  The left margin of the document.
- [static let paperMargin: NSAttributedString.DocumentAttributeKey](./papermargin.md)
  The paper margin of the document.
- [static let paperSize: NSAttributedString.DocumentAttributeKey](./papersize.md)
  The paper size for the document.
- [static let prefixSpaces: NSAttributedString.DocumentAttributeKey](./prefixspaces.md)
  The number of spaces for indenting nested HTML elements.
- [static let rightMargin: NSAttributedString.DocumentAttributeKey](./rightmargin.md)
  The right margin of the document.
- [static let topMargin: NSAttributedString.DocumentAttributeKey](./topmargin.md)
  The top margin of the document.
- [static let viewMode: NSAttributedString.DocumentAttributeKey](./viewmode.md)
  The view mode.
- [static let viewSize: NSAttributedString.DocumentAttributeKey](./viewsize.md)
  The view size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/documentattributekey/textlayoutsections)*