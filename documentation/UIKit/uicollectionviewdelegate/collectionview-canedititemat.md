# collectionView(_:canEditItemAt:)

**Framework**: UIKit  
**Kind**: method

Determines whether the specified item is editable.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: UICollectionView, canEditItemAt indexPath: IndexPath) -> Bool
```

#### Return Value

Returns [`true`](https://developer.apple.com/documentation/Swift/true) if the item is editable, [`false`](https://developer.apple.com/documentation/Swift/false) if it’s not. The default value is [`true`](https://developer.apple.com/documentation/Swift/true).

## Parameters

- `collectionView`: The collection view object requesting this information.
- `indexPath`: An index path locating an item in the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:canedititemat:))*