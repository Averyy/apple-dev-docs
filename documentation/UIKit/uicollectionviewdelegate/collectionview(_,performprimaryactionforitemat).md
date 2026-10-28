# collectionView(_:performPrimaryActionForItemAt:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate to perform the primary action for the cell at the specified index path.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
optional func collectionView(_ collectionView: UICollectionView, performPrimaryActionForItemAt indexPath: IndexPath)
```

```objc
- (void) collectionView:(UICollectionView *) collectionView performPrimaryActionForItemAtIndexPath:(NSIndexPath *) indexPath;
```

## Mentions

- [Building a desktop-class iPad app](../building-a-desktop-class-ipad-app.md)

## Discussion

Primary actions allow you to distinguish between a distinct user action and a change in selection (like a focus change or other indirect selection change). A primary action occurs when a person selects a single cell without extending an existing selection.

UIKit calls this method after [`collectionView(_:shouldSelectItemAt:)`](./collectionview%28_,shouldselectitemat%29.md) and [`collectionView(_:didSelectItemAt:)`](./collectionview%28_,didselectitemat%29.md), regardless of whether the cell selection state changes. Use [`collectionView(_:didSelectItemAt:)`](./collectionview%28_,didselectitemat%29.md) to update the state of the current view controller (like its buttons, title, and so on), and use [`collectionView(_:performPrimaryActionForItemAt:)`](./collectionview%28_,performprimaryactionforitemat%29.md) for actions like navigation or showing another split view column.

If [`collectionView(_:shouldSelectItemAt:)`](./collectionview%28_,shouldselectitemat%29.md) returns [`true`](../../Swift/true.md) to allow selection for the cell at `indexPath`, only that cell has selection when the system calls this method. If [`collectionView(_:shouldSelectItemAt:)`](./collectionview%28_,shouldselectitemat%29.md) returns [`false`](../../Swift/false.md), the system preserves the existing cell selection in the collection view. You can use this behavior to perform primary actions on nonselectable, button-style cells without changing the selection.

## Parameters

- `collectionView`: The collection view object on which to perform the primary action.
- `indexPath`: The index path of the cell.

## See Also

### Managing actions for cells
- [func collectionView(UICollectionView, canPerformPrimaryActionForItemAt: IndexPath) -> Bool](./collectionview%28_,canperformprimaryactionforitemat%29.md)
  Asks the delegate whether to perform a primary action for the cell at the specified index path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:performprimaryactionforitemat:))*