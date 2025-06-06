# toolbarImmovableItemIdentifiers(_:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate to provide the items that people can’t remove from the toolbar or rearrange during the customization process.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
@MainActor
optional func toolbarImmovableItemIdentifiers(_ toolbar: NSToolbar) -> Set<NSToolbarItem.Identifier>
```

#### Return Value

The set of item identifiers that people can’t remove from the toolbar or move to other locations in the toolbar. Return an empty set to let someone customize all toolbar items.

#### Discussion

Implement this method in your delegate and return any items you don’t want people to remove or rearrange. If you don’t implement this method, the toolbar lets people rearrange and remove all toolbar items.

## Parameters

- `toolbar`: The toolbar that contains the items.

## See Also

- [func toolbarAllowedItemIdentifiers(NSToolbar) -> [NSToolbarItem.Identifier]](nstoolbardelegate/toolbaralloweditemidentifiers(_:).md)
  Asks the delegate to provide the items allowed on the toolbar.
- [func toolbarDefaultItemIdentifiers(NSToolbar) -> [NSToolbarItem.Identifier]](nstoolbardelegate/toolbardefaultitemidentifiers(_:).md)
  Asks the delegate to provide the default items to display on the toolbar.
- [func toolbarSelectableItemIdentifiers(NSToolbar) -> [NSToolbarItem.Identifier]](nstoolbardelegate/toolbarselectableitemidentifiers(_:).md)
  Asks the delegate to provide the set of selectable items in the toolbar.
- [func toolbar(NSToolbar, itemIdentifier: NSToolbarItem.Identifier, canBeInsertedAt: Int) -> Bool](nstoolbardelegate/toolbar(_:itemidentifier:canbeinsertedat:).md)
  Asks the delegate for a Boolean value that indicates whether the toolbar can place the item at the specified position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbardelegate/toolbarimmovableitemidentifiers(_:))*