# UICollectionLayoutListConfiguration.ItemSeparatorHandler

**Framework**: UIKit  
**Kind**: typealias

A closure that provides granular control over list separator appearance.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
typealias ItemSeparatorHandler = (IndexPath, UIListSeparatorConfiguration) -> UIListSeparatorConfiguration
```

#### Return Value

The configuration to use for the separators at `indexPath`.

## Parameters

- `indexPath`: The   of the cell to configure separators for.
- `sectionSeparatorConfiguration`: The list section’s separator configuration for the cell at  . This configuration contains the values for separator visibility and insets according to the current state of the item.

## See Also

- [var showsSeparators: Bool](uicollectionlayoutlistconfiguration-swift.struct/showsseparators.md)
  A Boolean value that determines whether the list shows separators between cells.
- [var separatorConfiguration: UIListSeparatorConfiguration](uicollectionlayoutlistconfiguration-swift.struct/separatorconfiguration.md)
  The section’s preferred configuration for list separators.
- [struct UIListSeparatorConfiguration](uilistseparatorconfiguration-swift.struct.md)
  A configuration that controls the list separator appearance in a list section.
- [var itemSeparatorHandler: UICollectionLayoutListConfiguration.ItemSeparatorHandler?](uicollectionlayoutlistconfiguration-swift.struct/itemseparatorhandler-swift.property.md)
  The closure that provides granular control over the list separator appearance of each item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/itemseparatorhandler-swift.typealias)*