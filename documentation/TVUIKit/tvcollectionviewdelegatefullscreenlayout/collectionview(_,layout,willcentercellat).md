# collectionView(_:layout:willCenterCellAt:)

**Framework**: TVUIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when a cell is to be the center cell.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
optional func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, willCenterCellAt indexPath: IndexPath)
```

```objc
- (void) collectionView:(UICollectionView *) collectionView layout:(UICollectionViewLayout *) collectionViewLayout willCenterCellAtIndexPath:(NSIndexPath *) indexPath;
```

## See Also

### Managing Cell Transitions
- [func collectionView(UICollectionView, layout: UICollectionViewLayout, didCenterCellAt: IndexPath)](./collectionview%28_,layout,didcentercellat%29.md)
  Tells the delegate when a cell has completed the transition and has become the center cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvcollectionviewdelegatefullscreenlayout/collectionview(_:layout:willcentercellat:))*