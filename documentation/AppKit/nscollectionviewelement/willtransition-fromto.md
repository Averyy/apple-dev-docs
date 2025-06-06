# willTransition(from:to:)

**Framework**: AppKit  
**Kind**: method

Tells the element that the layout object of the collection view is about to change.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
optional func willTransition(from oldLayout: NSCollectionViewLayout, to newLayout: NSCollectionViewLayout)
```

#### Discussion

The default implementation of this method does nothing. Subclasses can override it and use it to prepare for the change in layouts.

##### Special Considerations

In OS X 10.11, this method is never called.

## Parameters

- `oldLayout`: The current layout object used by the collection view.
- `newLayout`: The new layout object that is about to be used by the collection view.

## See Also

- [func preferredLayoutAttributesFitting(NSCollectionViewLayoutAttributes) -> NSCollectionViewLayoutAttributes](nscollectionviewelement/preferredlayoutattributesfitting(_:).md)
  Asks your element if it wants to modify any layout attributes before they are applied.
- [func apply(NSCollectionViewLayoutAttributes)](nscollectionviewelement/apply(_:).md)
  Applies the specified layout attributes to the element.
- [func didTransition(from: NSCollectionViewLayout, to: NSCollectionViewLayout)](nscollectionviewelement/didtransition(from:to:).md)
  Tells the element that the layout object of the collection view changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewelement/willtransition(from:to:))*