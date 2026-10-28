# toolbarAllowedItemIdentifiers(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the array of identifier strings for the allowed toolbar items.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func toolbarAllowedItemIdentifiers(_ toolbar: NSToolbar) -> [NSToolbarItem.Identifier]
```

```objc
- (NSArray<NSString *> *) toolbarAllowedItemIdentifiers:(NSToolbar *) toolbar;
```

## Return Value

An array of [`NSString`](../../Foundation/nsstring.md) objects, each of which contains an identifier for an available toolbar item. The array must contain all of the items returned by the [`toolbarDefaultItemIdentifiers(_:)`](./toolbardefaultitemidentifiers%28_%29.md) method.

## Discussion

This method is called for tab view interfaces that use the [`NSTabViewController.TabStyle.toolbar`](./tabstyle-swift.enum/toolbar.md) style. Use this method to specify all possible items that may be included in the toolbar. The order of the items in the array is used to set their position in the toolbar configuration palette. If you include custom identifiers in the returned array, you must also override the [`toolbar(_:itemForItemIdentifier:willBeInsertedIntoToolbar:)`](./toolbar%28_,itemforitemidentifier,willbeinsertedintotoolbar%29.md) method to specify the content for those toolbar items.

If you override this method, you must call `super` at some point in your implementation. The default implementation of this method returns the identifiers for all toolbar items that correspond to tabs in the tab bar interface.

## Parameters

- `toolbar`: The toolbar making the request.

## See Also

### Responding to Toolbar Events
- [func toolbar(NSToolbar, itemForItemIdentifier: NSToolbarItem.Identifier, willBeInsertedIntoToolbar: Bool) -> NSToolbarItem?](./toolbar%28_,itemforitemidentifier,willbeinsertedintotoolbar%29.md)
  Returns the toolbar item for the specified identifier.
- [func toolbarDefaultItemIdentifiers(NSToolbar) -> [NSToolbarItem.Identifier]](./toolbardefaultitemidentifiers%28_%29.md)
  Returns the array of identifier strings for the default toolbar items.
- [func toolbarSelectableItemIdentifiers(NSToolbar) -> [NSToolbarItem.Identifier]](./toolbarselectableitemidentifiers%28_%29.md)
  Returns the array of identifier strings for the selectable toolbar items


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewcontroller/toolbaralloweditemidentifiers(_:))*