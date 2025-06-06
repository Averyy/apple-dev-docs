# toolbar(_:itemForItemIdentifier:willBeInsertedIntoToolbar:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate for the toolbar item associated with the specified identifier.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
@MainActor
optional func toolbar(_ toolbar: NSToolbar, itemForItemIdentifier itemIdentifier: NSToolbarItem.Identifier, willBeInsertedIntoToolbar flag: Bool) -> NSToolbarItem?
```

#### Return Value

A new [`NSToolbarItem`](nstoolbaritem.md) object, or `nil` if no toolbar item is available for the specified identifier.

#### Discussion

Use this method to create new [`NSToolbarItem`](nstoolbaritem.md) objects when the toolbar asks for them. If your toolbar item uses a custom view, make sure that view is fully configured before you return the item. The toolbar becomes the owner of the returned item, but can display the item either in the toolbar or the customization palette.

Don’t recycle toolbar items; always provide a new instance, even if the toolbar previously asked for an item with the same identifier.

> ❗ **Important**:  Even though this is an optional method, you must implement it if you create the toolbar programatically.

 Even though this is an optional method, you must implement it if you create the toolbar programatically.

## Parameters

- `toolbar`: The toolbar for which the item is being requested.
- `itemIdentifier`: The identifier for the requested item.
- `flag`:   if the toolbar will insert the item immediately. If this parameter is  , provide a canonical representation for the item. For example, provide a version of the item suitable for display in the toolbar customization sheet.

## See Also

- [Toolbar Programming Topics for Cocoa](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Toolbars/Toolbars.html#//apple_ref/doc/uid/10000109i)
- [func toolbarWillAddItem(Notification)](nstoolbardelegate/toolbarwilladditem(_:).md)
  Tells the delegate that the toolbar is about to add the specified item.
- [func toolbarDidRemoveItem(Notification)](nstoolbardelegate/toolbardidremoveitem(_:).md)
  Tells the delegate that the toolbar removed the specified item.
- [NSToolbar.Identifier](nstoolbar/identifier-swift.typealias.md)
  A string value that you use to differentiate your app’s toolbars.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbardelegate/toolbar(_:itemforitemidentifier:willbeinsertedintotoolbar:))*