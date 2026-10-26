# UICollectionViewCellConfigurationUpdateHandler

**Framework**: UIKit  
**Kind**: typealias  
**Role**: Type Alias

The type of block for handling updates to the cell’s configuration using the current state.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```c
typedef void (^)(__kindof UICollectionViewCell *, UICellConfigurationState *) UICollectionViewCellConfigurationUpdateHandler;
```

## Parameters

- `cell`: The collection view cell to configure.
- `state`: The new state to use for updating the cell’s configuration.

## See Also

### Managing the state
- [configurationState](./uicollectionviewcell/configurationstate-4269k.md)
  The current configuration state of the cell.
- [func setNeedsUpdateConfiguration()](./uicollectionviewcell/setneedsupdateconfiguration%28%29.md)
  Informs the cell to update its configuration for its current state.
- [- updateConfigurationUsingState:](./uicollectionviewcell/updateconfigurationusingstate_.md)
  Updates the cell’s configuration using the current state.
- [configurationUpdateHandler](./uicollectionviewcell/configurationupdatehandler-ajhn.md)
  A block for handling updates to the cell’s configuration using the current state.
- [var isSelected: Bool](./uicollectionviewcell/isselected.md)
  The selection state of the cell.
- [var isHighlighted: Bool](./uicollectionviewcell/ishighlighted.md)
  The highlight state of the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewcellconfigurationupdatehandler)*