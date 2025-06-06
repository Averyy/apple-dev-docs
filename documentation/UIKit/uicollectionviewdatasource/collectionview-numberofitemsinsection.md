# collectionView(_:numberOfItemsInSection:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Asks your data source object for the number of items in the specified section.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int
```

#### Return Value

The number of items in `section`.

## Parameters

- `collectionView`: The collection view requesting this information.
- `section`: An index number identifying a section in  . This index value is 0-based.

## See Also

- [func numberOfSections(in: UICollectionView) -> Int](uicollectionviewdatasource/numberofsections(in:).md)
  Asks your data source object for the number of sections in the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdatasource/collectionview(_:numberofitemsinsection:))*