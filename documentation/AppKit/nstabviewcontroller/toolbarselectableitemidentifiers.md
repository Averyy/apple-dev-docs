# toolbarSelectableItemIdentifiers(_:)

**Framework**: AppKit  
**Kind**: method

Returns the array of identifier strings for the selectable toolbar items

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func toolbarSelectableItemIdentifiers(_ toolbar: NSToolbar) -> [NSToolbarItem.Identifier]
```

#### Return Value

An array of [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) objects, each of which contains an identifier for a toolbar item that may be selected.

#### Discussion

This method is called for tab view interfaces that use the [`NSTabViewController.TabStyle.toolbar`](nstabviewcontroller/tabstyle-swift.enum/toolbar.md) style. Use this method to indicate which toolbar items are selectable. When an item is selected, the toolbar displays it with a visual highlight and updates the [`selectedTabViewItemIndex`](nstabviewcontroller/selectedtabviewitemindex.md) property. Typically, the toolbar items associated with tabs are selectable so that the user can tell which tab is selected.

If you override this method, you must call `super` at some point in your implementation. The default implementation of this method returns the identifiers for all toolbar items that correspond to tabs in the tab bar interface.

## Parameters

- `toolbar`: The toolbar making the request.

## See Also

- [func toolbar(NSToolbar, itemForItemIdentifier: NSToolbarItem.Identifier, willBeInsertedIntoToolbar: Bool) -> NSToolbarItem?](nstabviewcontroller/toolbar(_:itemforitemidentifier:willbeinsertedintotoolbar:).md)
  Returns the toolbar item for the specified identifier.
- [func toolbarAllowedItemIdentifiers(NSToolbar) -> [NSToolbarItem.Identifier]](nstabviewcontroller/toolbaralloweditemidentifiers(_:).md)
  Returns the array of identifier strings for the allowed toolbar items.
- [func toolbarDefaultItemIdentifiers(NSToolbar) -> [NSToolbarItem.Identifier]](nstabviewcontroller/toolbardefaultitemidentifiers(_:).md)
  Returns the array of identifier strings for the default toolbar items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewcontroller/toolbarselectableitemidentifiers(_:))*