# itemSeparatorHandler

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The closure that provides granular control over the list separator appearance of each item.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- visionOS

## Declaration

```swift
var itemSeparatorHandler: UICollectionLayoutListConfiguration.ItemSeparatorHandler? { get set }
```

#### Discussion

The list section treats the configuration that returns from this closure as the final separator configuration for the item at the input index path.

## See Also

### Configuring separators
- [var showsSeparators: Bool](./showsseparators.md)
  A Boolean value that determines whether the list shows separators between cells.
- [var separatorConfiguration: UIListSeparatorConfiguration](./separatorconfiguration.md)
  The section’s preferred configuration for list separators.
- [struct UIListSeparatorConfiguration](../uilistseparatorconfiguration-swift.struct.md)
  A configuration that controls the list separator appearance in a list section.
- [UICollectionLayoutListConfiguration.ItemSeparatorHandler](./itemseparatorhandler-swift.typealias.md)
  A closure that provides granular control over list separator appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/itemseparatorhandler-swift.property)*