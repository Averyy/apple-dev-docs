# willTransition(from:to:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the element that the layout object of the collection view is about to change.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
optional func willTransition(from oldLayout: NSCollectionViewLayout, to newLayout: NSCollectionViewLayout)
```

```objc
- (void) willTransitionFromLayout:(NSCollectionViewLayout *) oldLayout toLayout:(NSCollectionViewLayout *) newLayout;
```

#### Discussion

The default implementation of this method does nothing. Subclasses can override it and use it to prepare for the change in layouts.

##### Special Considerations

In OS X 10.11, this method is never called.

## Parameters

- `oldLayout`: The current layout object used by the collection view.
- `newLayout`: The new layout object that is about to be used by the collection view.

## See Also

### Managing Layout Changes
- [func preferredLayoutAttributesFitting(NSCollectionViewLayoutAttributes) -> NSCollectionViewLayoutAttributes](./preferredlayoutattributesfitting%28_%29.md)
  Asks your element if it wants to modify any layout attributes before they are applied.
- [func apply(NSCollectionViewLayoutAttributes)](./apply%28_%29.md)
  Applies the specified layout attributes to the element.
- [func didTransition(from: NSCollectionViewLayout, to: NSCollectionViewLayout)](./didtransition%28from,to%29.md)
  Tells the element that the layout object of the collection view changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewelement/willtransition(from:to:))*