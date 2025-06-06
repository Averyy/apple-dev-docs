# toolbar(_:itemForItemIdentifier:willBeInsertedIntoToolbar:)

**Framework**: AppKit  
**Kind**: method

Returns the toolbar item for the specified identifier.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func toolbar(_ toolbar: NSToolbar, itemForItemIdentifier itemIdentifier: NSToolbarItem.Identifier, willBeInsertedIntoToolbar flag: Bool) -> NSToolbarItem?
```

#### Return Value

The requested toolbar item or `nil` to indicate that the specified item is not supported. When the same item is requested again, you may return the same [`NSToolbarItem`](nstoolbaritem.md) object or a different one.

#### Discussion

This method is called for tab view interfaces that use the [`NSTabViewController.TabStyle.toolbar`](nstabviewcontroller/tabstyle-swift.enum/toolbar.md) style. Use this method to create toolbar items for any custom identifiers you specified in the [`toolbarAllowedItemIdentifiers(_:)`](nstabviewcontroller/toolbaralloweditemidentifiers(_:).md) and [`toolbarDefaultItemIdentifiers(_:)`](nstabviewcontroller/toolbardefaultitemidentifiers(_:).md) methods.

If you override this method, you must call `super` at some point in your implementation. The default implementation of this method returns toolbar items for the tabs in the tab bar interface. The identifier for each toolbar item is the same as the identifier for the corresponding tab view item. Similarly, the toolbar item’s [`label`](nstoolbaritem/label.md), [`image`](nstoolbaritem/image.md) and [`toolTip`](nstoolbaritem/tooltip.md) properties are bound to those of the corresponding tab view item.

## Parameters

- `toolbar`: The toolbar making the request.
- `itemIdentifier`: The identifier of the toolbar item being requested.
- `flag`: A Boolean indicating whether the item is inserted immediately into the toolbar. A value of   means the item is inserted into the toolbar. A value of   means the item is added to the toolbar’s configuration palette. The same item may be requested more than once with different values for this flag.

## See Also

- [func toolbarAllowedItemIdentifiers(NSToolbar) -> [NSToolbarItem.Identifier]](nstabviewcontroller/toolbaralloweditemidentifiers(_:).md)
  Returns the array of identifier strings for the allowed toolbar items.
- [func toolbarDefaultItemIdentifiers(NSToolbar) -> [NSToolbarItem.Identifier]](nstabviewcontroller/toolbardefaultitemidentifiers(_:).md)
  Returns the array of identifier strings for the default toolbar items.
- [func toolbarSelectableItemIdentifiers(NSToolbar) -> [NSToolbarItem.Identifier]](nstabviewcontroller/toolbarselectableitemidentifiers(_:).md)
  Returns the array of identifier strings for the selectable toolbar items


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewcontroller/toolbar(_:itemforitemidentifier:willbeinsertedintotoolbar:))*