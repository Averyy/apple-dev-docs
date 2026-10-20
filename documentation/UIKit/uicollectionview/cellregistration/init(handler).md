# init(handler:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a cell registration with the specified registration handler.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
init(handler: @escaping UICollectionView.CellRegistration<Cell, Item>.Handler)
```

## See Also

### Creating a cell registration
- [init(cellNib: UINib, handler: UICollectionView.CellRegistration<Cell, Item>.Handler)](./init%28cellnib,handler%29.md)
  Creates a cell registration with the specified registration handler and nib file.
- [UICollectionView.CellRegistration.Handler](./handler.md)
  A closure that handles the cell registration and configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/cellregistration/init(handler:))*