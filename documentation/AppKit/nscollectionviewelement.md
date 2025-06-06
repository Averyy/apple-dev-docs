# NSCollectionViewElement

**Framework**: AppKit  
**Kind**: protocol

A set of methods that you use to manage the content in a collection view.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSCollectionViewElement : NSUserInterfaceItemIdentification, NSObjectProtocol
```

#### Overview

Adopt this protocol in the classes that you use to display content for items, supplementary views, and decoration views in a collection view. The methods of this protocol are optional and provide support for applying layout attributes and for cleaning up elements when they move offscreen and are recycled.

Collection view items—that is, instances of the [`NSCollectionViewItem`](nscollectionviewitem.md) class—already adopt this protocol. For supplementary and decoration views, adopt this protocol in the custom view classes you use to represent that content.

## Topics

### Reusing Elements
- [func prepareForReuse()](nscollectionviewelement/prepareforreuse.md)
  Performs any necessary cleanup to prepare the element for use again.
### Managing Layout Changes
- [func preferredLayoutAttributesFitting(NSCollectionViewLayoutAttributes) -> NSCollectionViewLayoutAttributes](nscollectionviewelement/preferredlayoutattributesfitting(_:).md)
  Asks your element if it wants to modify any layout attributes before they are applied.
- [func apply(NSCollectionViewLayoutAttributes)](nscollectionviewelement/apply(_:).md)
  Applies the specified layout attributes to the element.
- [func willTransition(from: NSCollectionViewLayout, to: NSCollectionViewLayout)](nscollectionviewelement/willtransition(from:to:).md)
  Tells the element that the layout object of the collection view is about to change.
- [func didTransition(from: NSCollectionViewLayout, to: NSCollectionViewLayout)](nscollectionviewelement/didtransition(from:to:).md)
  Tells the element that the layout object of the collection view changed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
### Inherited By
- [NSCollectionViewSectionHeaderView](nscollectionviewsectionheaderview.md)
### Conforming Types
- [NSCollectionViewItem](nscollectionviewitem.md)

## See Also

- [class NSCollectionViewItem](nscollectionviewitem.md)
  The visual representation for a single data element in a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewelement)*