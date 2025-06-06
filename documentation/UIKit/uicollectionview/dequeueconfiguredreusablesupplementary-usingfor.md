# dequeueConfiguredReusableSupplementary(using:for:)

**Framework**: UIKit  
**Kind**: method

Dequeues a configured reusable supplementary view object.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func dequeueConfiguredReusableSupplementary<Supplementary>(using registration: UICollectionView.SupplementaryRegistration<Supplementary>, for indexPath: IndexPath) -> Supplementary where Supplementary : UICollectionReusableView
```

#### Return Value

A configured reusable supplementary view object.

## Parameters

- `registration`: The supplementary registration for configuring the supplementary view object. See  .
- `indexPath`: The index path that specifies the location of the supplementary view in the collection view.

## See Also

- [UICollectionView.SupplementaryRegistration](uicollectionview/supplementaryregistration.md)
  A registration for the collection view’s supplementary views.
- [func register(AnyClass?, forSupplementaryViewOfKind: String, withReuseIdentifier: String)](uicollectionview/register(_:forsupplementaryviewofkind:withreuseidentifier:)-661io.md)
  Registers a class for use in creating supplementary views for the collection view.
- [func register(UINib?, forSupplementaryViewOfKind: String, withReuseIdentifier: String)](uicollectionview/register(_:forsupplementaryviewofkind:withreuseidentifier:)-9hn73.md)
  Registers a nib file for use in creating supplementary views for the collection view.
- [func dequeueReusableSupplementaryView(ofKind: String, withReuseIdentifier: String, for: IndexPath) -> UICollectionReusableView](uicollectionview/dequeuereusablesupplementaryview(ofkind:withreuseidentifier:for:).md)
  Dequeues a reusable supplementary view located by its identifier and kind.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/dequeueconfiguredreusablesupplementary(using:for:))*