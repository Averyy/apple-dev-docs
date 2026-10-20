# UICollectionViewCell.ConfigurationUpdateHandler

**Framework**: UIKit  
**Kind**: typealias  
**Role**: Type Alias

The type of block for handling updates to the cell’s configuration using the current state.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS

## Declaration

```swift
typealias ConfigurationUpdateHandler = (UICollectionViewCell, UICellConfigurationState) -> Void
```

## Parameters

- `cell`: The collection view cell to configure.
- `state`: The new state to use for updating the cell’s configuration.

## See Also

### Managing the state
- [var configurationState: UICellConfigurationState](./configurationstate-4u37h.md)
  The current configuration state of the cell.
- [func setNeedsUpdateConfiguration()](./setneedsupdateconfiguration%28%29.md)
  Informs the cell to update its configuration for its current state.
- [func updateConfiguration(using: UICellConfigurationState)](./updateconfiguration%28using%29.md)
  Updates the cell’s configuration using the current state.
- [var configurationUpdateHandler: UICollectionViewCell.ConfigurationUpdateHandler?](./configurationupdatehandler-7rqbu.md)
  A block for handling updates to the cell’s configuration using the current state.
- [var isSelected: Bool](./isselected.md)
  The selection state of the cell.
- [var isHighlighted: Bool](./ishighlighted.md)
  The highlight state of the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewcell/configurationupdatehandler-swift.typealias)*