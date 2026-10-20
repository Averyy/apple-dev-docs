# numberOfItems(inSection:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Fetches the count of items in the specified section.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func numberOfItems(inSection section: Int) -> Int
```

```objc
- (NSInteger) numberOfItemsInSection:(NSInteger) section;
```

#### Return Value

The number of items in the specified section.

## Parameters

- `section`: The index of the section for which you want a count of the items.

## See Also

### Getting the state of the collection view
- [var numberOfSections: Int](./numberofsections.md)
  The number of sections displayed by the collection view.
- [var visibleCells: [UICollectionViewCell]](./visiblecells.md)
  An array of visible cells currently displayed by the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/numberofitems(insection:))*