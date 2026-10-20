# collectionView(_:layout:insetForSectionAt:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate for the margins to apply to content in the specified section.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, insetForSectionAt section: Int) -> UIEdgeInsets
```

```objc
- (UIEdgeInsets) collectionView:(UICollectionView *) collectionView layout:(UICollectionViewLayout *) collectionViewLayout insetForSectionAtIndex:(NSInteger) section;
```

#### Return Value

The margins to apply to items in the section.

#### Discussion

If you do not implement this method, the flow layout uses the value in its [`sectionInset`](../uicollectionviewflowlayout/sectioninset.md) property to set the margins instead. Your implementation of this method can return a fixed set of margin sizes or return different margin sizes for each section.

Section insets are margins applied only to the items in the section. They represent the distance between the header view and the first line of items and between the last line of items and the footer view. They also indicate the spacing on either side of a single line of items. They do not affect the size of the headers or footers themselves.

## Parameters

- `collectionView`: The collection view object displaying the flow layout.
- `collectionViewLayout`: The layout object requesting the information.
- `section`: The index number of the section whose insets are needed.

## See Also

### Getting the section spacing
- [func collectionView(UICollectionView, layout: UICollectionViewLayout, minimumLineSpacingForSectionAt: Int) -> CGFloat](./collectionview%28_,layout,minimumlinespacingforsectionat%29.md)
  Asks the delegate for the spacing between successive rows or columns of a section.
- [func collectionView(UICollectionView, layout: UICollectionViewLayout, minimumInteritemSpacingForSectionAt: Int) -> CGFloat](./collectionview%28_,layout,minimuminteritemspacingforsectionat%29.md)
  Asks the delegate for the spacing between successive items in the rows or columns of a section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout/collectionview(_:layout:insetforsectionat:))*