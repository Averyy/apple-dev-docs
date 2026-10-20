# collectionView(_:numberOfItemsInSection:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asks your data source object for the number of items in the specified section.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int
```

```objc
- (NSInteger) collectionView:(UICollectionView *) collectionView numberOfItemsInSection:(NSInteger) section;
```

#### Return Value

The number of items in `section`.

## Parameters

- `collectionView`: The collection view requesting this information.
- `section`: An index number identifying a section in `collectionView`. This index value is 0-based.

## See Also

### Getting item and section metrics
- [func numberOfSections(in: UICollectionView) -> Int](./numberofsections%28in%29.md)
  Asks your data source object for the number of sections in the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdatasource/collectionview(_:numberofitemsinsection:))*