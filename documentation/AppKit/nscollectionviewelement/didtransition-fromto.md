# didTransition(from:to:)

**Framework**: AppKit  
**Kind**: method

Tells the element that the layout object of the collection view changed.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
optional func didTransition(from oldLayout: NSCollectionViewLayout, to newLayout: NSCollectionViewLayout)
```

#### Discussion

The default implementation of this method does nothing. Subclasses can override it and use it to finalize any behaviors associated with the change in layouts.

##### Special Considerations

In OS X 10.11, this method is never called.

## Parameters

- `oldLayout`: The collection view’s previous layout object.
- `newLayout`: The current layout object associated with the collection view.

## See Also

- [func preferredLayoutAttributesFitting(NSCollectionViewLayoutAttributes) -> NSCollectionViewLayoutAttributes](nscollectionviewelement/preferredlayoutattributesfitting(_:).md)
  Asks your element if it wants to modify any layout attributes before they are applied.
- [func apply(NSCollectionViewLayoutAttributes)](nscollectionviewelement/apply(_:).md)
  Applies the specified layout attributes to the element.
- [func willTransition(from: NSCollectionViewLayout, to: NSCollectionViewLayout)](nscollectionviewelement/willtransition(from:to:).md)
  Tells the element that the layout object of the collection view is about to change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewelement/didtransition(from:to:))*