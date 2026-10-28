# preferredLayoutAttributesFitting(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Asks your element if it wants to modify any layout attributes before they are applied.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
optional func preferredLayoutAttributesFitting(_ layoutAttributes: NSCollectionViewLayoutAttributes) -> NSCollectionViewLayoutAttributes
```

```objc
- (NSCollectionViewLayoutAttributes *) preferredLayoutAttributesFittingAttributes:(NSCollectionViewLayoutAttributes *) layoutAttributes;
```

## Return Value

The final attributes to apply to the element.

## Discussion

The default implementation of this method returns the same attributes that are in the `layoutAttributes` parameter. You can override this method in subclasses and use it to return a different set of attributes. If you override this method, call `super` first to give the system the opportunity to make changes, then modify the returned attributes.

### Special Considerations

In OS X 10.11, this method is never called.

## Parameters

- `layoutAttributes`: The attributes provided by the layout object. These attributes represent the values that the layout object intends to apply to the element.

## See Also

### Managing Layout Changes
- [func apply(NSCollectionViewLayoutAttributes)](./apply%28_%29.md)
  Applies the specified layout attributes to the element.
- [func willTransition(from: NSCollectionViewLayout, to: NSCollectionViewLayout)](./willtransition%28from,to%29.md)
  Tells the element that the layout object of the collection view is about to change.
- [func didTransition(from: NSCollectionViewLayout, to: NSCollectionViewLayout)](./didtransition%28from,to%29.md)
  Tells the element that the layout object of the collection view changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewelement/preferredlayoutattributesfitting(_:))*