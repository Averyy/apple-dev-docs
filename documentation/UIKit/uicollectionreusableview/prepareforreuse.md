# prepareForReuse()

**Framework**: UIKit  
**Kind**: method

Performs any clean up necessary to prepare the view for use again.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func prepareForReuse()
```

#### Discussion

The default implementation of this method does nothing. Subclasses such as [`UICollectionViewCell`](uicollectionviewcell.md) override this method and use it to perform relevant actions. So, if your subclass descends from [`UICollectionViewCell`](uicollectionviewcell.md) or another intermediate class, call `super` to ensure that your class gets the parent’s behavior.

When the collection view dequeues your view for use, it calls this method before the corresponding dequeue method returns the view to your code. Override this method in your subclass to reset properties to their default values and make the view ready to use again. Don’t use this method to assign any new data to the view; that’s the responsibility of your data source object.

The collection view doesn’t call this method when you use [`reconfigureItems(at:)`](uicollectionview/reconfigureitems(at:).md) on `UICollectionView`, or [`reconfigureItems(_:)`](nsdiffabledatasourcesnapshot-swift.struct/reconfigureitems(_:).md) (Swift) or [`reconfigureItems(withIdentifiers:)`](nsdiffabledatasourcesnapshotreference/reconfigureitems(withidentifiers:).md) (Objective-C) on `NSDiffableDataSourceSnapshot` to update the contents of an existing cell.

## See Also

- [var reuseIdentifier: String?](uicollectionreusableview/reuseidentifier.md)
  A string that identifies the purpose of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionreusableview/prepareforreuse())*