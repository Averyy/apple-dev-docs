# isHighlighted

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The highlight state of the cell.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isHighlighted: Bool { get set }
```

```objc
@property (nonatomic, getter=isHighlighted) BOOL highlighted;
```

## Discussion

This property manages the highlight state of the cell only. The default value of this property is [`false`](../../Swift/false.md), which indicates that the cell isn’t in a highlighted state.

You typically don’t set the value of this property directly. Instead, the preferred way to select the cell and highlight it’s to use the selection methods of the collection view object.

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
- [UICollectionViewCell.ConfigurationUpdateHandler](./configurationupdatehandler-swift.typealias.md)
  The type of block for handling updates to the cell’s configuration using the current state.
- [var isSelected: Bool](./isselected.md)
  The selection state of the cell.
- [configurationState](./configurationstate-4269k.md)
  The current configuration state of the cell.
- [- updateConfigurationUsingState:](./updateconfigurationusingstate_.md)
  Updates the cell’s configuration using the current state.
- [configurationUpdateHandler](./configurationupdatehandler-ajhn.md)
  A block for handling updates to the cell’s configuration using the current state.
- [UICollectionViewCellConfigurationUpdateHandler](../uicollectionviewcellconfigurationupdatehandler.md)
  The type of block for handling updates to the cell’s configuration using the current state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewcell/ishighlighted)*