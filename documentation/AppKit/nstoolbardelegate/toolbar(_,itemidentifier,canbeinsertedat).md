# toolbar(_:itemIdentifier:canBeInsertedAt:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate for a Boolean value that indicates whether the toolbar can place the item at the specified position.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
@MainActor
optional func toolbar(_ toolbar: NSToolbar, itemIdentifier: NSToolbarItem.Identifier, canBeInsertedAt index: Int) -> Bool
```

```objc
- (BOOL) toolbar:(NSToolbar *) toolbar itemIdentifier:(NSToolbarItemIdentifier) itemIdentifier canBeInsertedAtIndex:(NSInteger) index;
```

#### Return Value

[`true`](../../Swift/true.md) to allow the toolbar to place the item at the specified location, or [`false`](../../Swift/false.md) to prevent the toolbar from placing the item in that location.

#### Discussion

Implement this method to control the placement of items in the toolbar. During a drag operation, the toolbar calls this method to determine if the specified index is an acceptable location for the item. Return a Boolean value that indicates whether the new posiition is acceptable.

Don’t use the `index` parameter to determine the final location of the toolbar item. During a drag operation, the toolbar can call this method multiple times, so the index value can change later.

## Parameters

- `toolbar`: The toolbar that contains the items.
- `itemIdentifier`: The identifier of the toolbar item to insert at the specified index.
- `index`: The proposed index at which to place the item. If the toolbar is removing the item, this value is [`NSNotFound`](../../Foundation/nsnotfound-4qp9h.md).

## See Also

### Configuring the behavior of items
- [func toolbarAllowedItemIdentifiers(NSToolbar) -> [NSToolbarItem.Identifier]](./toolbaralloweditemidentifiers%28_%29.md)
  Asks the delegate to provide the items allowed on the toolbar.
- [func toolbarDefaultItemIdentifiers(NSToolbar) -> [NSToolbarItem.Identifier]](./toolbardefaultitemidentifiers%28_%29.md)
  Asks the delegate to provide the default items to display on the toolbar.
- [func toolbarImmovableItemIdentifiers(NSToolbar) -> Set<NSToolbarItem.Identifier>](./toolbarimmovableitemidentifiers%28_%29.md)
  Asks the delegate to provide the items that people can’t remove from the toolbar or rearrange during the customization process.
- [func toolbarSelectableItemIdentifiers(NSToolbar) -> [NSToolbarItem.Identifier]](./toolbarselectableitemidentifiers%28_%29.md)
  Asks the delegate to provide the set of selectable items in the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbardelegate/toolbar(_:itemidentifier:canbeinsertedat:))*