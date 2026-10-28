# indexTitles(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the data source to return the titles for the index items to display for the collection view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
optional func indexTitles(for collectionView: UICollectionView) -> [String]?
```

```objc
- (NSArray<NSString *> *) indexTitlesForCollectionView:(UICollectionView *) collectionView;
```

## Return Value

An array of strings to use for the title of each index entry. For example, you might return an array of strings containing the letters of the alphabet (`["A", "B", "C", ..., "Z"]`).

## Discussion

Use this method to support fast scrolling through your collection view’s content. The strings you return are displayed in an index view that can be used to jump to specific locations in the collection view’s content. If you implement this method, you must also implement the [`collectionView(_:indexPathForIndexTitle:at:)`](./collectionview%28_,indexpathforindextitle,at%29.md) method to specify the collection view item associated with each index title.

## Parameters

- `collectionView`: The collection view requesting this information.

## See Also

### Configuring an index
- [func collectionView(UICollectionView, indexPathForIndexTitle: String, at: Int) -> IndexPath](./collectionview%28_,indexpathforindextitle,at%29.md)
  Asks the data source to return the index path of a collection view item that corresponds to one of your index entries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdatasource/indextitles(for:))*