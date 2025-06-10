# collectionView(_:layout:minimumInteritemSpacingForSectionAt:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for the spacing between successive items in the rows or columns of a section.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, minimumInteritemSpacingForSectionAt section: Int) -> CGFloat
```

#### Return Value

The minimum space (measured in points) to apply between successive items in the lines of a section.

#### Discussion

If you do not implement this method, the flow layout uses the value in its [`minimumInteritemSpacing`](uicollectionviewflowlayout/minimuminteritemspacing.md) property to set the space between items instead. Your implementation of this method can return a fixed value or return different spacing values for each section.

For a vertically scrolling grid, this value represents the minimum spacing between items in the same row. For a horizontally scrolling grid, this value represents the minimum spacing between items in the same column. This spacing is used to compute how many items can fit in a single line, but after the number of items is determined, the actual spacing may possibly be adjusted upward.

## Parameters

- `collectionView`: The collection view object displaying the flow layout.
- `collectionViewLayout`: The layout object requesting the information.
- `section`: The index number of the section whose inter-item spacing is needed.

## See Also

- [func collectionView(UICollectionView, layout: UICollectionViewLayout, insetForSectionAt: Int) -> UIEdgeInsets](uicollectionviewdelegateflowlayout/collectionview(_:layout:insetforsectionat:).md)
  Asks the delegate for the margins to apply to content in the specified section.
- [func collectionView(UICollectionView, layout: UICollectionViewLayout, minimumLineSpacingForSectionAt: Int) -> CGFloat](uicollectionviewdelegateflowlayout/collectionview(_:layout:minimumlinespacingforsectionat:).md)
  Asks the delegate for the spacing between successive rows or columns of a section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout/collectionview(_:layout:minimuminteritemspacingforsectionat:))*