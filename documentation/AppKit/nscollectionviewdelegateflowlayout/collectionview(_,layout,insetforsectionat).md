# collectionView(_:layout:insetForSectionAt:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate for the margins to apply to content in the specified section.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: NSCollectionView, layout collectionViewLayout: NSCollectionViewLayout, insetForSectionAt section: Int) -> NSEdgeInsets
```

```objc
- (NSEdgeInsets) collectionView:(NSCollectionView *) collectionView layout:(NSCollectionViewLayout *) collectionViewLayout insetForSectionAtIndex:(NSInteger) section;
```

## Return Value

The margins to apply to items in the specified section.

## Discussion

Implement this method when you want to provide margins for sections in the flow layout. Your implementation can return the same margins for all sections or it can return different margins for different sections. You can also adjust the margins of each section dynamically each time you update the layout. If you do not implement this method, the margins are obtained from the properties of the flow layout object.

The insets you return reflect the spacing between the items and the header and footer views of the section. They also reflect the spacing at the edges of a single row or column. For more information about how insets are applied, see the description of the [`sectionInset`](../nscollectionviewflowlayout/sectioninset.md) property.

## Parameters

- `collectionView`: The collection view object displaying the flow layout.
- `collectionViewLayout`: The layout object requesting the information.
- `section`: The index of the section whose margins are needed.

## See Also

### Related Documentation
- [var sectionInset: NSEdgeInsets](../nscollectionviewflowlayout/sectioninset.md)
  The margins used to lay out content in a section.
### Getting the Section Spacing
- [func collectionView(NSCollectionView, layout: NSCollectionViewLayout, minimumLineSpacingForSectionAt: Int) -> CGFloat](./collectionview%28_,layout,minimumlinespacingforsectionat%29.md)
  Asks the delegate for the spacing between successive rows or columns of a section.
- [func collectionView(NSCollectionView, layout: NSCollectionViewLayout, minimumInteritemSpacingForSectionAt: Int) -> CGFloat](./collectionview%28_,layout,minimuminteritemspacingforsectionat%29.md)
  Asks the delegate for the spacing between successive items of a single row or column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdelegateflowlayout/collectionview(_:layout:insetforsectionat:))*