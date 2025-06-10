# UICollectionView.CellRegistration.Handler

**Framework**: UIKit  
**Kind**: typealias

A closure that handles the cell registration and configuration.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
typealias Handler = (Cell, IndexPath, Item) -> Void
```

## See Also

- [init(handler: UICollectionView.CellRegistration<Cell, Item>.Handler)](uicollectionview/cellregistration/init(handler:).md)
  Creates a cell registration with the specified registration handler.
- [init(cellNib: UINib, handler: UICollectionView.CellRegistration<Cell, Item>.Handler)](uicollectionview/cellregistration/init(cellnib:handler:).md)
  Creates a cell registration with the specified registration handler and nib file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/cellregistration/handler)*