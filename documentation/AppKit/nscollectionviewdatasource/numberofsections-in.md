# numberOfSections(in:)

**Framework**: AppKit  
**Kind**: method

Asks your data source object to provide the total number of sections.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
optional func numberOfSections(in collectionView: NSCollectionView) -> Int
```

#### Return Value

The number of sections in the specified collection view.

#### Discussion

Implement this method when the organization of your data requires more than one section. If you do not implement this method, the collection view creates only one section.

## Parameters

- `collectionView`: The collection view requesting the information.

## See Also

- [func collectionView(NSCollectionView, numberOfItemsInSection: Int) -> Int](nscollectionviewdatasource/collectionview(_:numberofitemsinsection:).md)
  Asks your data source object to provide the number of items in the specified section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdatasource/numberofsections(in:))*