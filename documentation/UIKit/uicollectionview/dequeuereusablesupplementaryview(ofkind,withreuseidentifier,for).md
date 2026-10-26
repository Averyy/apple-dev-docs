# dequeueReusableSupplementaryView(ofKind:withReuseIdentifier:for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Dequeues a reusable supplementary view located by its identifier and kind.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func dequeueReusableSupplementaryView(ofKind elementKind: String, withReuseIdentifier identifier: String, for indexPath: IndexPath) -> UICollectionReusableView
```

```objc
- (UICollectionReusableView *) dequeueReusableSupplementaryViewOfKind:(NSString *) elementKind withReuseIdentifier:(NSString *) identifier forIndexPath:(NSIndexPath *) indexPath;
```

#### Return Value

A valid [`UICollectionReusableView`](../uicollectionreusableview.md) object.

#### Discussion

Call this method from your data source object when asked to provide a new supplementary view for the collection view. This method dequeues an existing view if one is available or creates a new one based on the class or nib file you previously registered.

> ❗ **Important**:  You must register a class or nib file using the [`register(_:forSupplementaryViewOfKind:withReuseIdentifier:)`](./register%28_,forsupplementaryviewofkind,withreuseidentifier%29-661io.md) or [`register(_:forSupplementaryViewOfKind:withReuseIdentifier:)`](./register%28_,forsupplementaryviewofkind,withreuseidentifier%29-9hn73.md) method before calling this method. You can also register a set of default supplementary views with the layout object using the [`register(_:forDecorationViewOfKind:)`](../uicollectionviewlayout/register%28_,fordecorationviewofkind%29-361k6.md) or [`register(_:forDecorationViewOfKind:)`](../uicollectionviewlayout/register%28_,fordecorationviewofkind%29-35jf9.md) method.

If you registered a class for the specified `identifier` and a new cell must be created, this method initializes the cell by calling its [`init(frame:)`](../uiview/init%28frame%29.md) method. For nib-based cells, this method loads the cell object from the provided nib file. If an existing cell was available for reuse, this method calls the cell’s [`prepareForReuse()`](../uicollectionreusableview/prepareforreuse%28%29.md) method instead.

## Parameters

- `elementKind`: The kind of supplementary view to retrieve. This value is defined by the layout object. This parameter must not be `nil`.
- `identifier`: The reuse identifier for the specified view. This parameter must not be `nil`.
- `indexPath`: The index path specifying the location of the supplementary view in the collection view. The data source receives this information when it’s asked for the view and should just pass it along. This method uses the information to perform additional configuration based on the view’s position in the collection view.

## See Also

### Creating headers and footers
- [UICollectionView.SupplementaryRegistration](./supplementaryregistration.md)
  A registration for the collection view’s supplementary views.
- [func dequeueConfiguredReusableSupplementary<Supplementary>(using: UICollectionView.SupplementaryRegistration<Supplementary>, for: IndexPath) -> Supplementary](./dequeueconfiguredreusablesupplementary%28using,for%29.md)
  Dequeues a configured reusable supplementary view object.
- [func register(AnyClass?, forSupplementaryViewOfKind: String, withReuseIdentifier: String)](./register%28_,forsupplementaryviewofkind,withreuseidentifier%29-661io.md)
  Registers a class for use in creating supplementary views for the collection view.
- [func register(UINib?, forSupplementaryViewOfKind: String, withReuseIdentifier: String)](./register%28_,forsupplementaryviewofkind,withreuseidentifier%29-9hn73.md)
  Registers a nib file for use in creating supplementary views for the collection view.
- [UICollectionViewSupplementaryRegistration](../uicollectionviewsupplementaryregistration.md)
  A registration for the collection view’s supplementary views.
- [- dequeueConfiguredReusableSupplementaryViewWithRegistration:forIndexPath:](./dequeueconfiguredreusablesupplementaryviewwithregistration_forindexpath_.md)
  Dequeues a configured reusable supplementary view object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/dequeuereusablesupplementaryview(ofkind:withreuseidentifier:for:))*