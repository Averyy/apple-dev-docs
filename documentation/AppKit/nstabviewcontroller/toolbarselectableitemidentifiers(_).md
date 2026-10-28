# toolbarSelectableItemIdentifiers(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the array of identifier strings for the selectable toolbar items

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func toolbarSelectableItemIdentifiers(_ toolbar: NSToolbar) -> [NSToolbarItem.Identifier]
```

```objc
- (NSArray<NSString *> *) toolbarSelectableItemIdentifiers:(NSToolbar *) toolbar;
```

## Return Value

An array of [`NSString`](../../Foundation/nsstring.md) objects, each of which contains an identifier for a toolbar item that may be selected.

## Discussion

This method is called for tab view interfaces that use the [`NSTabViewController.TabStyle.toolbar`](./tabstyle-swift.enum/toolbar.md) style. Use this method to indicate which toolbar items are selectable. When an item is selected, the toolbar displays it with a visual highlight and updates the [`selectedTabViewItemIndex`](./selectedtabviewitemindex.md) property. Typically, the toolbar items associated with tabs are selectable so that the user can tell which tab is selected.

If you override this method, you must call `super` at some point in your implementation. The default implementation of this method returns the identifiers for all toolbar items that correspond to tabs in the tab bar interface.

## Parameters

- `toolbar`: The toolbar making the request.

## See Also

### Responding to Toolbar Events
- [func toolbar(NSToolbar, itemForItemIdentifier: NSToolbarItem.Identifier, willBeInsertedIntoToolbar: Bool) -> NSToolbarItem?](./toolbar%28_,itemforitemidentifier,willbeinsertedintotoolbar%29.md)
  Returns the toolbar item for the specified identifier.
- [func toolbarAllowedItemIdentifiers(NSToolbar) -> [NSToolbarItem.Identifier]](./toolbaralloweditemidentifiers%28_%29.md)
  Returns the array of identifier strings for the allowed toolbar items.
- [func toolbarDefaultItemIdentifiers(NSToolbar) -> [NSToolbarItem.Identifier]](./toolbardefaultitemidentifiers%28_%29.md)
  Returns the array of identifier strings for the default toolbar items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewcontroller/toolbarselectableitemidentifiers(_:))*