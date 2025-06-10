# collectionView(_:layout:referenceSizeForHeaderInSection:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for the size of the header view in the specified section.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, referenceSizeForHeaderInSection section: Int) -> CGSize
```

#### Return Value

The size of the header. If you return a value of size (0, 0), no header is added.

#### Discussion

If you do not implement this method, the flow layout uses the value in its [`headerReferenceSize`](uicollectionviewflowlayout/headerreferencesize.md) property to set the size of the header.

During layout, only the size that corresponds to the appropriate scrolling direction is used. For example, for the vertical scrolling direction, the layout object uses the height value returned by your method. (In that instance, the width of the header would be set to the width of the collection view.) If the size in the appropriate scrolling dimension is 0, no header is added.

## Parameters

- `collectionView`: The collection view object displaying the flow layout.
- `collectionViewLayout`: The layout object requesting the information.
- `section`: The index of the section whose header size is being requested.

## See Also

- [func collectionView(UICollectionView, layout: UICollectionViewLayout, referenceSizeForFooterInSection: Int) -> CGSize](uicollectionviewdelegateflowlayout/collectionview(_:layout:referencesizeforfooterinsection:).md)
  Asks the delegate for the size of the footer view in the specified section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout/collectionview(_:layout:referencesizeforheaderinsection:))*