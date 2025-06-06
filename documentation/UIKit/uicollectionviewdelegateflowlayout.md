# UICollectionViewDelegateFlowLayout

**Framework**: UIKit  
**Kind**: protocol

The methods that let you coordinate with a flow layout object to implement a grid-based layout.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UICollectionViewDelegateFlowLayout : UICollectionViewDelegate
```

#### Overview

The methods of this protocol define the size of items and the spacing between items in the grid. All of the methods in this protocol are optional. If you don’t implement a particular method, the flow layout delegate uses values in its own properties for the appropriate spacing information.

The [`UICollectionViewFlowLayout`](uicollectionviewflowlayout.md) object expects the collection view’s delegate object to adopt this protocol. Therefore, implement this protocol on the object assigned to your collection view’s [`delegate`](uicollectionview/delegate.md) property.

## Topics

### Getting the size of items
- [func collectionView(UICollectionView, layout: UICollectionViewLayout, sizeForItemAt: IndexPath) -> CGSize](uicollectionviewdelegateflowlayout/collectionview(_:layout:sizeforitemat:).md)
  Asks the delegate for the size of the specified item’s cell.
### Getting the section spacing
- [func collectionView(UICollectionView, layout: UICollectionViewLayout, insetForSectionAt: Int) -> UIEdgeInsets](uicollectionviewdelegateflowlayout/collectionview(_:layout:insetforsectionat:).md)
  Asks the delegate for the margins to apply to content in the specified section.
- [func collectionView(UICollectionView, layout: UICollectionViewLayout, minimumLineSpacingForSectionAt: Int) -> CGFloat](uicollectionviewdelegateflowlayout/collectionview(_:layout:minimumlinespacingforsectionat:).md)
  Asks the delegate for the spacing between successive rows or columns of a section.
- [func collectionView(UICollectionView, layout: UICollectionViewLayout, minimumInteritemSpacingForSectionAt: Int) -> CGFloat](uicollectionviewdelegateflowlayout/collectionview(_:layout:minimuminteritemspacingforsectionat:).md)
  Asks the delegate for the spacing between successive items in the rows or columns of a section.
### Getting the header and footer sizes
- [func collectionView(UICollectionView, layout: UICollectionViewLayout, referenceSizeForHeaderInSection: Int) -> CGSize](uicollectionviewdelegateflowlayout/collectionview(_:layout:referencesizeforheaderinsection:).md)
  Asks the delegate for the size of the header view in the specified section.
- [func collectionView(UICollectionView, layout: UICollectionViewLayout, referenceSizeForFooterInSection: Int) -> CGSize](uicollectionviewdelegateflowlayout/collectionview(_:layout:referencesizeforfooterinsection:).md)
  Asks the delegate for the size of the footer view in the specified section.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UICollectionViewDelegate](uicollectionviewdelegate.md)
- [UIScrollViewDelegate](uiscrollviewdelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout)*