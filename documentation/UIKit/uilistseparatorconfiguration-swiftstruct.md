# UIListSeparatorConfiguration

**Framework**: UIKit  
**Kind**: struct

A configuration that controls the list separator appearance in a list section.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
struct UIListSeparatorConfiguration
```

#### Overview

To specify list separator appearance for a section, set a default sectionwide [`separatorConfiguration`](uicollectionlayoutlistconfiguration-swift.struct/separatorconfiguration.md) on your [`UICollectionLayoutListConfiguration`](uicollectionlayoutlistconfiguration-swift.struct.md) when you create your list.

```swift
var listConfig = UICollectionLayoutListConfiguration(appearance: .plain)
listConfig.separatorConfiguration.color = .tertiarySystemFill
let layout = UICollectionViewCompositionalLayout.list(using: listConfig)
```

To override list separator appearance on a per-item basis, use the [`itemSeparatorHandler`](uicollectionlayoutlistconfiguration-swift.struct/itemseparatorhandler-swift.property.md) property.

```swift
var listConfig = UICollectionLayoutListConfiguration(appearance: .plain)
listConfig.separatorConfiguration.color = .tertiarySystemFill

let indexPathToHide = IndexPath()
 
listConfig.itemSeparatorHandler = { (indexPath, sectionSeparatorConfiguration) in    
    var configuration = sectionSeparatorConfiguration
    if indexPath == indexPathToHide {
        configuration.bottomSeparatorVisibility = .hidden    
    }    
    return configuration
}

let layout = UICollectionViewCompositionalLayout.list(using: listConfig)
```

## Topics

### Creating a list separator configuration
- [init(listAppearance: UICollectionLayoutListConfiguration.Appearance)](uilistseparatorconfiguration-swift.struct/init(listappearance:).md)
  Creates a list separator configuration with default values according to the specified list appearance.
### Controlling separator visibility
- [var topSeparatorVisibility: UIListSeparatorConfiguration.Visibility](uilistseparatorconfiguration-swift.struct/topseparatorvisibility.md)
  The visibility of the top separator for the item the configuration applies to.
- [var bottomSeparatorVisibility: UIListSeparatorConfiguration.Visibility](uilistseparatorconfiguration-swift.struct/bottomseparatorvisibility.md)
  The visibility of the bottom separator for the item the configuration applies to.
- [UIListSeparatorConfiguration.Visibility](uilistseparatorconfiguration-swift.struct/visibility.md)
  Constants that define the visibility of list separators.
### Configuring separator insets
- [var topSeparatorInsets: NSDirectionalEdgeInsets](uilistseparatorconfiguration-swift.struct/topseparatorinsets.md)
  Insets to apply to the top separator of the item the configuration applies to.
- [var bottomSeparatorInsets: NSDirectionalEdgeInsets](uilistseparatorconfiguration-swift.struct/bottomseparatorinsets.md)
  Insets to apply to the bottom separator of the item the configuration applies to.
- [static let automaticInsets: NSDirectionalEdgeInsets](uilistseparatorconfiguration-swift.struct/automaticinsets.md)
  A constant that specifies a placeholder size for separator insets.
### Configuring separator appearance
- [var color: UIColor](uilistseparatorconfiguration-swift.struct/color.md)
  The color to use for the separators of the item the configuration applies to.
- [var multipleSelectionColor: UIColor](uilistseparatorconfiguration-swift.struct/multipleselectioncolor.md)
  The color to use for the separators of the item the configuration applies to when the item is in a multiple-selection group.
- [var visualEffect: UIVisualEffect?](uilistseparatorconfiguration-swift.struct/visualeffect.md)
  The visual effect to use for the separators of the item the configuration applies to.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [var showsSeparators: Bool](uicollectionlayoutlistconfiguration-swift.struct/showsseparators.md)
  A Boolean value that determines whether the list shows separators between cells.
- [var separatorConfiguration: UIListSeparatorConfiguration](uicollectionlayoutlistconfiguration-swift.struct/separatorconfiguration.md)
  The section’s preferred configuration for list separators.
- [var itemSeparatorHandler: UICollectionLayoutListConfiguration.ItemSeparatorHandler?](uicollectionlayoutlistconfiguration-swift.struct/itemseparatorhandler-swift.property.md)
  The closure that provides granular control over the list separator appearance of each item.
- [UICollectionLayoutListConfiguration.ItemSeparatorHandler](uicollectionlayoutlistconfiguration-swift.struct/itemseparatorhandler-swift.typealias.md)
  A closure that provides granular control over list separator appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilistseparatorconfiguration-swift.struct)*