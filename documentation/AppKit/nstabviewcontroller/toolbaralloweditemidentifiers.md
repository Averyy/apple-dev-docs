# toolbarAllowedItemIdentifiers(_:)

**Framework**: AppKit  
**Kind**: method

Returns the array of identifier strings for the allowed toolbar items.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func toolbarAllowedItemIdentifiers(_ toolbar: NSToolbar) -> [NSToolbarItem.Identifier]
```

#### Return Value

An array of [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) objects, each of which contains an identifier for an available toolbar item. The array must contain all of the items returned by the [`toolbarDefaultItemIdentifiers(_:)`](nstabviewcontroller/toolbardefaultitemidentifiers(_:).md) method.

#### Discussion

This method is called for tab view interfaces that use the [`NSTabViewController.TabStyle.toolbar`](nstabviewcontroller/tabstyle-swift.enum/toolbar.md) style. Use this method to specify all possible items that may be included in the toolbar. The order of the items in the array is used to set their position in the toolbar configuration palette. If you include custom identifiers in the returned array, you must also override the [`toolbar(_:itemForItemIdentifier:willBeInsertedIntoToolbar:)`](nstabviewcontroller/toolbar(_:itemforitemidentifier:willbeinsertedintotoolbar:).md) method to specify the content for those toolbar items.

If you override this method, you must call `super` at some point in your implementation. The default implementation of this method returns the identifiers for all toolbar items that correspond to tabs in the tab bar interface.

## Parameters

- `toolbar`: The toolbar making the request.

## See Also

- [func toolbar(NSToolbar, itemForItemIdentifier: NSToolbarItem.Identifier, willBeInsertedIntoToolbar: Bool) -> NSToolbarItem?](nstabviewcontroller/toolbar(_:itemforitemidentifier:willbeinsertedintotoolbar:).md)
  Returns the toolbar item for the specified identifier.
- [func toolbarDefaultItemIdentifiers(NSToolbar) -> [NSToolbarItem.Identifier]](nstabviewcontroller/toolbardefaultitemidentifiers(_:).md)
  Returns the array of identifier strings for the default toolbar items.
- [func toolbarSelectableItemIdentifiers(NSToolbar) -> [NSToolbarItem.Identifier]](nstabviewcontroller/toolbarselectableitemidentifiers(_:).md)
  Returns the array of identifier strings for the selectable toolbar items


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewcontroller/toolbaralloweditemidentifiers(_:))*