# isSelected

**Framework**: UIKit  
**Kind**: property

The selection state of the cell.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isSelected: Bool { get set }
```

#### Discussion

This property manages the selection state of the cell only. The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false), which indicates an unselected state.

You typically don’t set the value of this property directly. Changing the value of this property programmatically doesn’t change the appearance of the cell. The preferred way to select the cell and highlight it’s to use the selection methods of the collection view object.

## See Also

- [var configurationState: UICellConfigurationState](uicollectionviewcell/configurationstate-4u37h.md)
  The current configuration state of the cell.
- [func setNeedsUpdateConfiguration()](uicollectionviewcell/setneedsupdateconfiguration.md)
  Informs the cell to update its configuration for its current state.
- [func updateConfiguration(using: UICellConfigurationState)](uicollectionviewcell/updateconfiguration(using:).md)
  Updates the cell’s configuration using the current state.
- [var configurationUpdateHandler: UICollectionViewCell.ConfigurationUpdateHandler?](uicollectionviewcell/configurationupdatehandler-7rqbu.md)
  A block for handling updates to the cell’s configuration using the current state.
- [UICollectionViewCell.ConfigurationUpdateHandler](uicollectionviewcell/configurationupdatehandler-swift.typealias.md)
  The type of block for handling updates to the cell’s configuration using the current state.
- [var isHighlighted: Bool](uicollectionviewcell/ishighlighted.md)
  The highlight state of the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewcell/isselected)*