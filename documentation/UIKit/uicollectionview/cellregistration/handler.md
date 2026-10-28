# UICollectionView.CellRegistration.Handler

**Framework**: UIKit  
**Kind**: typealias  
**Role**: Type Alias

A closure that handles the cell registration and configuration.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
typealias Handler = (Cell, IndexPath, Item) -> Void
```

## Discussion

The closure takes the following parameters:

- **`cell`**: The [`UICollectionViewCell`](../../uicollectionviewcell.md) or subclass instance to configure.
- **`indexPath`**: The [`IndexPath`](../../../Foundation/indexpath.md) of the cell to configure.
- **`item`**: The data item you provide in [`dequeueConfiguredReusableCell(using:for:item:)`](../dequeueconfiguredreusablecell%28using,for,item%29.md).

## See Also

### Creating a cell registration
- [init(handler: UICollectionView.CellRegistration<Cell, Item>.Handler)](./init%28handler%29.md)
  Creates a cell registration with the specified registration handler.
- [init(cellNib: UINib, handler: UICollectionView.CellRegistration<Cell, Item>.Handler)](./init%28cellnib,handler%29.md)
  Creates a cell registration with the specified registration handler and nib file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/cellregistration/handler)*