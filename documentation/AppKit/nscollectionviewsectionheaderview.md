# NSCollectionViewSectionHeaderView

**Framework**: AppKit  
**Kind**: protocol

A protocol that defines a button to control the collapse of a collection view’s section.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSCollectionViewSectionHeaderView : NSCollectionViewElement
```

#### Overview

A collection view can support a section that can collapse into a single horizontally scrollable row, similar to the groupings in the icon view in Finder. To ensure that the collection view can communicate with the button that controls the collapsing of a section, the section header view object should conform to this protocol and connect the button’s outlet to [`sectionCollapseButton`](nscollectionviewsectionheaderview/sectioncollapsebutton.md).

## Topics

### Providing a Collapse Button
- [var sectionCollapseButton: NSButton?](nscollectionviewsectionheaderview/sectioncollapsebutton.md)
  A control that lets users collapse and open a collection view section.

## Relationships

### Inherits From
- [NSCollectionViewElement](nscollectionviewelement.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)

## See Also

- [class NSCollectionView](nscollectionview.md)
  An ordered collection of data items displayed in a customizable layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewsectionheaderview)*