# UIListSeparatorConfiguration

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A configuration that controls the list separator appearance in a list section.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- visionOS 1.0+

## Declaration

```objc
@interface UIListSeparatorConfiguration : NSObject
```

#### Overview

To specify list separator appearance for a section, set a default sectionwide [`separatorConfiguration`](./uicollectionlayoutlistconfiguration-c.class/separatorconfiguration.md) on your [`UICollectionLayoutListConfiguration`](./uicollectionlayoutlistconfiguration-swift.struct.md) when you create your list.

```swift
var listConfig = UICollectionLayoutListConfiguration(appearance: .plain)
listConfig.separatorConfiguration.color = .tertiarySystemFill
let layout = UICollectionViewCompositionalLayout.list(using: listConfig)
```

To override list separator appearance on a per-item basis, use the [`itemSeparatorHandler`](./uicollectionlayoutlistconfiguration-c.class/itemseparatorhandler.md) property.

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
- [- initWithListAppearance:](./uilistseparatorconfiguration-c.class/initwithlistappearance_.md)
  Creates a list separator configuration with default values according to the specified list appearance.
### Controlling separator visibility
- [topSeparatorVisibility](./uilistseparatorconfiguration-c.class/topseparatorvisibility.md)
  The visibility of the top separator for the item the configuration applies to.
- [bottomSeparatorVisibility](./uilistseparatorconfiguration-c.class/bottomseparatorvisibility.md)
  The visibility of the bottom separator for the item the configuration applies to.
- [UIListSeparatorVisibility](./uilistseparatorvisibility.md)
  An enumeration that defines the visibility of list separators.
### Configuring separator insets
- [topSeparatorInsets](./uilistseparatorconfiguration-c.class/topseparatorinsets.md)
  Insets to apply to the top separator of the item the configuration applies to.
- [bottomSeparatorInsets](./uilistseparatorconfiguration-c.class/bottomseparatorinsets.md)
  Insets to apply to the bottom separator of the item the configuration applies to.
- [UIListSeparatorAutomaticInsets](./uilistseparatorautomaticinsets.md)
  A constant that specifies a placeholder size for separator insets.
### Configuring separator appearance
- [color](./uilistseparatorconfiguration-c.class/color.md)
  The color to use for the separators of the item the configuration applies to.
- [multipleSelectionColor](./uilistseparatorconfiguration-c.class/multipleselectioncolor.md)
  The color to use for the separators of the item the configuration applies to when the item is in a multiple-selection group.
- [visualEffect](./uilistseparatorconfiguration-c.class/visualeffect.md)
  The visual effect to use for the separators of the item the configuration applies to.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Configuring separators
- [showsSeparators](./uicollectionlayoutlistconfiguration-c.class/showsseparators.md)
  A Boolean value that determines whether the list shows separators between cells.
- [separatorConfiguration](./uicollectionlayoutlistconfiguration-c.class/separatorconfiguration.md)
  The section’s preferred configuration for list separators.
- [itemSeparatorHandler](./uicollectionlayoutlistconfiguration-c.class/itemseparatorhandler.md)
  The closure that provides granular control over the list separator appearance of each item.
- [UICollectionLayoutListItemSeparatorHandler](./uicollectionlayoutlistitemseparatorhandler.md)
  A closure that provides granular control over list separator appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilistseparatorconfiguration-c.class)*