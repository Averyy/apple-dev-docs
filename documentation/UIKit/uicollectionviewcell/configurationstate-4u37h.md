# configurationState

**Framework**: UIKit  
**Kind**: property

The current configuration state of the cell.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@objc(_bridgedConfigurationState) @preconcurrency dynamic var configurationState: UICellConfigurationState { get }
```

#### Discussion

To add your own custom state, see [`UIConfigurationStateCustomKey`](uiconfigurationstatecustomkey.md).

## See Also

- [func setNeedsUpdateConfiguration()](uicollectionviewcell/setneedsupdateconfiguration.md)
  Informs the cell to update its configuration for its current state.
- [func updateConfiguration(using: UICellConfigurationState)](uicollectionviewcell/updateconfiguration(using:).md)
  Updates the cell’s configuration using the current state.
- [var configurationUpdateHandler: UICollectionViewCell.ConfigurationUpdateHandler?](uicollectionviewcell/configurationupdatehandler-7rqbu.md)
  A block for handling updates to the cell’s configuration using the current state.
- [UICollectionViewCell.ConfigurationUpdateHandler](uicollectionviewcell/configurationupdatehandler-swift.typealias.md)
  The type of block for handling updates to the cell’s configuration using the current state.
- [var isSelected: Bool](uicollectionviewcell/isselected.md)
  The selection state of the cell.
- [var isHighlighted: Bool](uicollectionviewcell/ishighlighted.md)
  The highlight state of the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewcell/configurationstate-4u37h)*