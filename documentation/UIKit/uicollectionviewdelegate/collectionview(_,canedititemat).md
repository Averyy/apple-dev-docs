# collectionView(_:canEditItemAt:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Determines whether the specified item is editable.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
optional func collectionView(_ collectionView: UICollectionView, canEditItemAt indexPath: IndexPath) -> Bool
```

```objc
- (BOOL) collectionView:(UICollectionView *) collectionView canEditItemAtIndexPath:(NSIndexPath *) indexPath;
```

## Return Value

Returns [`true`](../../Swift/true.md) if the item is editable, [`false`](../../Swift/false.md) if it’s not. The default value is [`true`](../../Swift/true.md).

## Parameters

- `collectionView`: The collection view object requesting this information.
- `indexPath`: An index path locating an item in the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:canedititemat:))*