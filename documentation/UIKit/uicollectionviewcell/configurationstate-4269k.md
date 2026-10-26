# configurationState

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The current configuration state of the cell.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, readonly) UICellConfigurationState * configurationState;
```

#### Discussion

To add your own custom state, see [`UIConfigurationStateCustomKey`](../uiconfigurationstatecustomkey.md).

## See Also

### Managing the state
- [func setNeedsUpdateConfiguration()](./setneedsupdateconfiguration%28%29.md)
  Informs the cell to update its configuration for its current state.
- [- updateConfigurationUsingState:](./updateconfigurationusingstate_.md)
  Updates the cell’s configuration using the current state.
- [configurationUpdateHandler](./configurationupdatehandler-ajhn.md)
  A block for handling updates to the cell’s configuration using the current state.
- [UICollectionViewCellConfigurationUpdateHandler](../uicollectionviewcellconfigurationupdatehandler.md)
  The type of block for handling updates to the cell’s configuration using the current state.
- [var isSelected: Bool](./isselected.md)
  The selection state of the cell.
- [var isHighlighted: Bool](./ishighlighted.md)
  The highlight state of the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewcell/configurationstate-4269k)*