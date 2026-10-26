# dequeueConfiguredReusableSupplementaryViewWithRegistration:forIndexPath:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Dequeues a configured reusable supplementary view object.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
- (UICollectionReusableView *) dequeueConfiguredReusableSupplementaryViewWithRegistration:(UICollectionViewSupplementaryRegistration *) registration forIndexPath:(NSIndexPath *) indexPath;
```

#### Return Value

A configured reusable supplementary view object.

## Parameters

- `registration`: The supplementary registration for configuring the supplementary view object. See [`UICollectionViewSupplementaryRegistration`](../uicollectionviewsupplementaryregistration.md).
- `indexPath`: The index path that specifies the location of the supplementary view in the collection view.

## See Also

### Creating headers and footers
- [UICollectionViewSupplementaryRegistration](../uicollectionviewsupplementaryregistration.md)
  A registration for the collection view’s supplementary views.
- [func register(AnyClass?, forSupplementaryViewOfKind: String, withReuseIdentifier: String)](./register%28_,forsupplementaryviewofkind,withreuseidentifier%29-661io.md)
  Registers a class for use in creating supplementary views for the collection view.
- [func register(UINib?, forSupplementaryViewOfKind: String, withReuseIdentifier: String)](./register%28_,forsupplementaryviewofkind,withreuseidentifier%29-9hn73.md)
  Registers a nib file for use in creating supplementary views for the collection view.
- [func dequeueReusableSupplementaryView(ofKind: String, withReuseIdentifier: String, for: IndexPath) -> UICollectionReusableView](./dequeuereusablesupplementaryview%28ofkind,withreuseidentifier,for%29.md)
  Dequeues a reusable supplementary view located by its identifier and kind.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/dequeueconfiguredreusablesupplementaryviewwithregistration:forindexpath:)*