# itemSeparatorHandler

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The closure that provides granular control over the list separator appearance of each item.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, copy, nullable) UICollectionLayoutListItemSeparatorHandler itemSeparatorHandler;
```

## Discussion

The list section treats the configuration that returns from this closure as the final separator configuration for the item at the input index path.

## See Also

### Configuring separators
- [showsSeparators](./showsseparators.md)
  A Boolean value that determines whether the list shows separators between cells.
- [separatorConfiguration](./separatorconfiguration.md)
  The section’s preferred configuration for list separators.
- [UIListSeparatorConfiguration](../uilistseparatorconfiguration-c.class.md)
  A configuration that controls the list separator appearance in a list section.
- [UICollectionLayoutListItemSeparatorHandler](../uicollectionlayoutlistitemseparatorhandler.md)
  A closure that provides granular control over list separator appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-c.class/itemseparatorhandler)*