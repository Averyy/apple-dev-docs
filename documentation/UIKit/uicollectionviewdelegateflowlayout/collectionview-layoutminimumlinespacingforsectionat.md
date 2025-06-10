# collectionView(_:layout:minimumLineSpacingForSectionAt:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for the spacing between successive rows or columns of a section.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, minimumLineSpacingForSectionAt section: Int) -> CGFloat
```

#### Return Value

The minimum space (measured in points) to apply between successive lines in a section.

#### Discussion

If you do not implement this method, the flow layout uses the value in its [`minimumLineSpacing`](uicollectionviewflowlayout/minimumlinespacing.md) property to set the space between lines instead. Your implementation of this method can return a fixed value or return different spacing values for each section.

For a vertically scrolling grid, this value represents the minimum spacing between successive rows. For a horizontally scrolling grid, this value represents the minimum spacing between successive columns. This spacing is not applied to the space between the header and the first line or between the last line and the footer.

## Parameters

- `collectionView`: The collection view object displaying the flow layout.
- `collectionViewLayout`: The layout object requesting the information.
- `section`: The index number of the section whose line spacing is needed.

## See Also

- [func collectionView(UICollectionView, layout: UICollectionViewLayout, insetForSectionAt: Int) -> UIEdgeInsets](uicollectionviewdelegateflowlayout/collectionview(_:layout:insetforsectionat:).md)
  Asks the delegate for the margins to apply to content in the specified section.
- [func collectionView(UICollectionView, layout: UICollectionViewLayout, minimumInteritemSpacingForSectionAt: Int) -> CGFloat](uicollectionviewdelegateflowlayout/collectionview(_:layout:minimuminteritemspacingforsectionat:).md)
  Asks the delegate for the spacing between successive items in the rows or columns of a section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout/collectionview(_:layout:minimumlinespacingforsectionat:))*