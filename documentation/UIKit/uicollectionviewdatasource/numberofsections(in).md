# numberOfSections(in:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks your data source object for the number of sections in the collection view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func numberOfSections(in collectionView: UICollectionView) -> Int
```

```objc
- (NSInteger) numberOfSectionsInCollectionView:(UICollectionView *) collectionView;
```

## Return Value

The number of sections in `collectionView`.

## Discussion

If you don’t implement this method, the collection view uses a default value of 1.

## Parameters

- `collectionView`: The collection view requesting this information.

## See Also

### Getting item and section metrics
- [func collectionView(UICollectionView, numberOfItemsInSection: Int) -> Int](./collectionview%28_,numberofitemsinsection%29.md)
  Asks your data source object for the number of items in the specified section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdatasource/numberofsections(in:))*