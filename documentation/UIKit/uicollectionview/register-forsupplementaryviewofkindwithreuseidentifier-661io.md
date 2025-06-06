# register(_:forSupplementaryViewOfKind:withReuseIdentifier:)

**Framework**: UIKit  
**Kind**: method

Registers a class for use in creating supplementary views for the collection view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func register(_ viewClass: AnyClass?, forSupplementaryViewOfKind elementKind: String, withReuseIdentifier identifier: String)
```

#### Discussion

Prior to calling the [`dequeueReusableSupplementaryView(ofKind:withReuseIdentifier:for:)`](uicollectionview/dequeuereusablesupplementaryview(ofkind:withreuseidentifier:for:).md) method of the collection view, you must use this method or the [`register(_:forSupplementaryViewOfKind:withReuseIdentifier:)`](uicollectionview/register(_:forsupplementaryviewofkind:withreuseidentifier:)-9hn73.md) method to tell the collection view how to create a supplementary view of the given type. If a view of the specified type isn’t currently in a reuse queue, the collection view uses the provided information to create a view object automatically.

If you previously registered a class or nib file with the same element kind and reuse identifier, the class you specify in the `viewClass` parameter replaces the old entry. You may specify `nil` for `viewClass` if you want to unregister the class from the specified element kind and reuse identifier.

## Parameters

- `viewClass`: The class to use for the supplementary view.
- `elementKind`: The kind of supplementary view to create. This value is defined by the layout object. This parameter must not be  .
- `identifier`: The reuse identifier to associate with the specified class. This parameter must not be   and must not be an empty string.

## See Also

- [UICollectionView.SupplementaryRegistration](uicollectionview/supplementaryregistration.md)
  A registration for the collection view’s supplementary views.
- [func dequeueConfiguredReusableSupplementary<Supplementary>(using: UICollectionView.SupplementaryRegistration<Supplementary>, for: IndexPath) -> Supplementary](uicollectionview/dequeueconfiguredreusablesupplementary(using:for:).md)
  Dequeues a configured reusable supplementary view object.
- [func register(UINib?, forSupplementaryViewOfKind: String, withReuseIdentifier: String)](uicollectionview/register(_:forsupplementaryviewofkind:withreuseidentifier:)-9hn73.md)
  Registers a nib file for use in creating supplementary views for the collection view.
- [func dequeueReusableSupplementaryView(ofKind: String, withReuseIdentifier: String, for: IndexPath) -> UICollectionReusableView](uicollectionview/dequeuereusablesupplementaryview(ofkind:withreuseidentifier:for:).md)
  Dequeues a reusable supplementary view located by its identifier and kind.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/register(_:forsupplementaryviewofkind:withreuseidentifier:)-661io)*