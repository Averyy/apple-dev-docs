# collectionView(_:didHighlightItemAt:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the item at the specified index path was highlighted.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func collectionView(_ collectionView: UICollectionView, didHighlightItemAt indexPath: IndexPath)
```

```objc
- (void) collectionView:(UICollectionView *) collectionView didHighlightItemAtIndexPath:(NSIndexPath *) indexPath;
```

#### Discussion

The collection view calls this method only in response to user interactions and does not call it if you programmatically set the highlighting on a cell.

## Parameters

- `collectionView`: The collection view object that is notifying you of the highlight change.
- `indexPath`: The index path of the cell that was highlighted.

## See Also

### Managing cell highlighting
- [func collectionView(UICollectionView, shouldHighlightItemAt: IndexPath) -> Bool](./collectionview%28_,shouldhighlightitemat%29.md)
  Asks the delegate if the item should be highlighted during tracking.
- [func collectionView(UICollectionView, didUnhighlightItemAt: IndexPath)](./collectionview%28_,didunhighlightitemat%29.md)
  Tells the delegate that the highlight was removed from the item at the specified index path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:didhighlightitemat:))*