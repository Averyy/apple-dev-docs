# toolbarDefaultItemIdentifiers(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the array of identifier strings for the default toolbar items.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func toolbarDefaultItemIdentifiers(_ toolbar: NSToolbar) -> [NSToolbarItem.Identifier]
```

```objc
- (NSArray<NSString *> *) toolbarDefaultItemIdentifiers:(NSToolbar *) toolbar;
```

#### Return Value

An array of [`NSString`](../../Foundation/nsstring.md) objects, each of which contains an identifier for a toolbar item that is part of the default configuration. The order of items in the array is used to set the order of items in the toolbar.

#### Discussion

This method is called for tab view interfaces that use the [`NSTabViewController.TabStyle.toolbar`](./tabstyle-swift.enum/toolbar.md) style. Use this method to return the default set of toolbar items, including any extra toolbar items you want included. For example, include [`flexibleSpace`](../nstoolbaritem/identifier/flexiblespace.md) strings as the first and last elements of the array to center the remaining toolbar items. If you add custom identifiers, you must also override the [`toolbar(_:itemForItemIdentifier:willBeInsertedIntoToolbar:)`](./toolbar%28_,itemforitemidentifier,willbeinsertedintotoolbar%29.md) method to specify the content for those toolbar items.

If you override this method, you must call `super` at some point in your implementation. The default implementation of this method returns the identifiers for all toolbar items that correspond to tabs in the tab bar interface.

## Parameters

- `toolbar`: The toolbar making the request.

## See Also

### Responding to Toolbar Events
- [func toolbar(NSToolbar, itemForItemIdentifier: NSToolbarItem.Identifier, willBeInsertedIntoToolbar: Bool) -> NSToolbarItem?](./toolbar%28_,itemforitemidentifier,willbeinsertedintotoolbar%29.md)
  Returns the toolbar item for the specified identifier.
- [func toolbarAllowedItemIdentifiers(NSToolbar) -> [NSToolbarItem.Identifier]](./toolbaralloweditemidentifiers%28_%29.md)
  Returns the array of identifier strings for the allowed toolbar items.
- [func toolbarSelectableItemIdentifiers(NSToolbar) -> [NSToolbarItem.Identifier]](./toolbarselectableitemidentifiers%28_%29.md)
  Returns the array of identifier strings for the selectable toolbar items


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewcontroller/toolbardefaultitemidentifiers(_:))*