# collectionView(_:numberOfItemsInSection:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asks your data source object to provide the number of items in the specified section.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func collectionView(_ collectionView: NSCollectionView, numberOfItemsInSection section: Int) -> Int
```

```objc
- (NSInteger) collectionView:(NSCollectionView *) collectionView numberOfItemsInSection:(NSInteger) section;
```

#### Return Value

The number of items in the specified section.

#### Discussion

All data source objects must implement this method. Your implementation should quickly return the number of items in the specified section.

Make sure the number of items you return is accurate. The [`collectionView(_:itemForRepresentedObjectAt:)`](./collectionview%28_,itemforrepresentedobjectat%29.md) method of your data source object must be able to provide a visual representation for each item in the section.

## Parameters

- `collectionView`: The collection view requesting the information.
- `section`: The index number of the section. Section indexes are zero based.

## See Also

### Getting the Number of Sections and Items
- [func numberOfSections(in: NSCollectionView) -> Int](./numberofsections%28in%29.md)
  Asks your data source object to provide the total number of sections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdatasource/collectionview(_:numberofitemsinsection:))*