# apply(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Applies the specified layout attributes to the element.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
optional func apply(_ layoutAttributes: NSCollectionViewLayoutAttributes)
```

```objc
- (void) applyLayoutAttributes:(NSCollectionViewLayoutAttributes *) layoutAttributes;
```

## Discussion

In your custom elements, you can use this method to apply the specified attributes to your content. For example, if your element object is a view controller, you would override this method and use it to apply the attributes to the root view object. When using your element with a layout object that supports custom attributes, you would also use this method to apply those custom attributes.

## Parameters

- `layoutAttributes`: The layout attributes to apply.

## See Also

### Managing Layout Changes
- [func preferredLayoutAttributesFitting(NSCollectionViewLayoutAttributes) -> NSCollectionViewLayoutAttributes](./preferredlayoutattributesfitting%28_%29.md)
  Asks your element if it wants to modify any layout attributes before they are applied.
- [func willTransition(from: NSCollectionViewLayout, to: NSCollectionViewLayout)](./willtransition%28from,to%29.md)
  Tells the element that the layout object of the collection view is about to change.
- [func didTransition(from: NSCollectionViewLayout, to: NSCollectionViewLayout)](./didtransition%28from,to%29.md)
  Tells the element that the layout object of the collection view changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewelement/apply(_:))*