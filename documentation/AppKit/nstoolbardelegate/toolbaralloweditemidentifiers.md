# toolbarAllowedItemIdentifiers(_:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate to provide the items allowed on the toolbar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
@MainActor
optional func toolbarAllowedItemIdentifiers(_ toolbar: NSToolbar) -> [NSToolbarItem.Identifier]
```

#### Return Value

An array of toolbar item identifiers, each of which represents an item that appears in the customization palette. Arrange the identifiers in the order you want them to appear in the palette, with the first item appearing on the palette’s leading edge.

#### Discussion

Include all of your toolbar’s items, including standard ones defined by [`NSToolbar.Identifier`](nstoolbar/identifier-swift.typealias.md). The array must include all of the default menu items in your toolbar.

> ❗ **Important**:  Even though this is an optional method, you must implement it if you create the toolbar programatically.

 Even though this is an optional method, you must implement it if you create the toolbar programatically.

## Parameters

- `toolbar`: The toolbar whose allowed item identifiers are to be returned.

## See Also

- [func toolbarDefaultItemIdentifiers(NSToolbar) -> [NSToolbarItem.Identifier]](nstoolbardelegate/toolbardefaultitemidentifiers(_:).md)
  Asks the delegate to provide the default items to display on the toolbar.
- [func toolbarImmovableItemIdentifiers(NSToolbar) -> Set<NSToolbarItem.Identifier>](nstoolbardelegate/toolbarimmovableitemidentifiers(_:).md)
  Asks the delegate to provide the items that people can’t remove from the toolbar or rearrange during the customization process.
- [func toolbarSelectableItemIdentifiers(NSToolbar) -> [NSToolbarItem.Identifier]](nstoolbardelegate/toolbarselectableitemidentifiers(_:).md)
  Asks the delegate to provide the set of selectable items in the toolbar.
- [func toolbar(NSToolbar, itemIdentifier: NSToolbarItem.Identifier, canBeInsertedAt: Int) -> Bool](nstoolbardelegate/toolbar(_:itemidentifier:canbeinsertedat:).md)
  Asks the delegate for a Boolean value that indicates whether the toolbar can place the item at the specified position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbardelegate/toolbaralloweditemidentifiers(_:))*