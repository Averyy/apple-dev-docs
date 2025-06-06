# collectionView(_:layout:minimumInteritemSpacingForSectionAt:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate for the spacing between successive items of a single row or column.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: NSCollectionView, layout collectionViewLayout: NSCollectionViewLayout, minimumInteritemSpacingForSectionAt section: Int) -> CGFloat
```

#### Return Value

The minimum space (in points) to apply between successive items in a single row or column.

#### Discussion

Implement this method when you want to provide custom inter-item spacing for sections in the flow layout. Your implementation can return the same spacing for all sections or it can return different spacing for different sections. You can also adjust the inter-item spacing of each section dynamically each time you update the layout. If you do not implement this method, the inter-item spacing is obtained from the properties of the flow layout object.

For a vertically scrolling layout, this value represents the minimum spacing between items in the same row. For a horizontally scrolling layout, this value represents the minimum spacing between items in the same column. The layout object uses this spacing only to compute how many items can fit in a single row or column. The actual spacing may be increased after the number of items has been determined. For more information about how inter-item spacing is applied, see the description of the [`minimumInteritemSpacing`](nscollectionviewflowlayout/minimuminteritemspacing.md) property.

## Parameters

- `collectionView`: The collection view object displaying the flow layout.
- `collectionViewLayout`: The layout object requesting the information.
- `section`: The index of the section whose inter-item spacing is needed.

## See Also

- [var minimumInteritemSpacing: CGFloat](nscollectionviewflowlayout/minimuminteritemspacing.md)
  The minimum spacing (in points) to use between items in the same row or column.
- [func collectionView(NSCollectionView, layout: NSCollectionViewLayout, insetForSectionAt: Int) -> NSEdgeInsets](nscollectionviewdelegateflowlayout/collectionview(_:layout:insetforsectionat:).md)
  Asks the delegate for the margins to apply to content in the specified section.
- [func collectionView(NSCollectionView, layout: NSCollectionViewLayout, minimumLineSpacingForSectionAt: Int) -> CGFloat](nscollectionviewdelegateflowlayout/collectionview(_:layout:minimumlinespacingforsectionat:).md)
  Asks the delegate for the spacing between successive rows or columns of a section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdelegateflowlayout/collectionview(_:layout:minimuminteritemspacingforsectionat:))*