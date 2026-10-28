# separatorConfiguration

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The section’s preferred configuration for list separators.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- visionOS

## Declaration

```swift
var separatorConfiguration: UIListSeparatorConfiguration { get set }
```

## Discussion

This configuration only takes effect if [`showsSeparators`](./showsseparators.md) is [`true`](../../Swift/true.md).

For more granular control over list separator appearance, use [`itemSeparatorHandler`](./itemseparatorhandler-swift.property.md).

## See Also

### Configuring separators
- [var showsSeparators: Bool](./showsseparators.md)
  A Boolean value that determines whether the list shows separators between cells.
- [struct UIListSeparatorConfiguration](../uilistseparatorconfiguration-swift.struct.md)
  A configuration that controls the list separator appearance in a list section.
- [var itemSeparatorHandler: UICollectionLayoutListConfiguration.ItemSeparatorHandler?](./itemseparatorhandler-swift.property.md)
  The closure that provides granular control over the list separator appearance of each item.
- [UICollectionLayoutListConfiguration.ItemSeparatorHandler](./itemseparatorhandler-swift.typealias.md)
  A closure that provides granular control over list separator appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/separatorconfiguration)*