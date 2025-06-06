# UICollectionViewCell.ConfigurationUpdateHandler

**Framework**: UIKit  
**Kind**: typealias

The type of block for handling updates to the cell’s configuration using the current state.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+

## Declaration

```swift
typealias ConfigurationUpdateHandler = (UICollectionViewCell, UICellConfigurationState) -> Void
```

## Parameters

- `cell`: The collection view cell to configure.
- `state`: The new state to use for updating the cell’s configuration.

## See Also

- [var configurationState: UICellConfigurationState](uicollectionviewcell/configurationstate-4u37h.md)
  The current configuration state of the cell.
- [func setNeedsUpdateConfiguration()](uicollectionviewcell/setneedsupdateconfiguration.md)
  Informs the cell to update its configuration for its current state.
- [func updateConfiguration(using: UICellConfigurationState)](uicollectionviewcell/updateconfiguration(using:).md)
  Updates the cell’s configuration using the current state.
- [var configurationUpdateHandler: UICollectionViewCell.ConfigurationUpdateHandler?](uicollectionviewcell/configurationupdatehandler-7rqbu.md)
  A block for handling updates to the cell’s configuration using the current state.
- [var isSelected: Bool](uicollectionviewcell/isselected.md)
  The selection state of the cell.
- [var isHighlighted: Bool](uicollectionviewcell/ishighlighted.md)
  The highlight state of the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewcell/configurationupdatehandler-swift.typealias)*