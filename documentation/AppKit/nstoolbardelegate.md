# NSToolbarDelegate

**Framework**: AppKit  
**Kind**: protocol

A set of optional methods you use to configure the toolbar and respond to changes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
protocol NSToolbarDelegate : NSObjectProtocol
```

#### Overview

Use the methods of [`NSToolbarDelegate`](nstoolbardelegate.md) to customize the behavior of your toolbars. You might use these methods to track the addition or removal of toolbar items, or use them to prevent someone from rearranging or removing specific items. Adopt this protocol in one of your custom objects and assign that object to the [`delegate`](nstoolbar/delegate.md) property of the [`NSToolbar`](nstoolbar.md) object you want to manage.

## Topics

### Adding and removing items
- [func toolbar(NSToolbar, itemForItemIdentifier: NSToolbarItem.Identifier, willBeInsertedIntoToolbar: Bool) -> NSToolbarItem?](nstoolbardelegate/toolbar(_:itemforitemidentifier:willbeinsertedintotoolbar:).md)
  Asks the delegate for the toolbar item associated with the specified identifier.
- [func toolbarWillAddItem(Notification)](nstoolbardelegate/toolbarwilladditem(_:).md)
  Tells the delegate that the toolbar is about to add the specified item.
- [func toolbarDidRemoveItem(Notification)](nstoolbardelegate/toolbardidremoveitem(_:).md)
  Tells the delegate that the toolbar removed the specified item.
- [NSToolbar.Identifier](nstoolbar/identifier-swift.typealias.md)
  A string value that you use to differentiate your app’s toolbars.
### Configuring the behavior of items
- [func toolbarAllowedItemIdentifiers(NSToolbar) -> [NSToolbarItem.Identifier]](nstoolbardelegate/toolbaralloweditemidentifiers(_:).md)
  Asks the delegate to provide the items allowed on the toolbar.
- [func toolbarDefaultItemIdentifiers(NSToolbar) -> [NSToolbarItem.Identifier]](nstoolbardelegate/toolbardefaultitemidentifiers(_:).md)
  Asks the delegate to provide the default items to display on the toolbar.
- [func toolbarImmovableItemIdentifiers(NSToolbar) -> Set<NSToolbarItem.Identifier>](nstoolbardelegate/toolbarimmovableitemidentifiers(_:).md)
  Asks the delegate to provide the items that people can’t remove from the toolbar or rearrange during the customization process.
- [func toolbarSelectableItemIdentifiers(NSToolbar) -> [NSToolbarItem.Identifier]](nstoolbardelegate/toolbarselectableitemidentifiers(_:).md)
  Asks the delegate to provide the set of selectable items in the toolbar.
- [func toolbar(NSToolbar, itemIdentifier: NSToolbarItem.Identifier, canBeInsertedAt: Int) -> Bool](nstoolbardelegate/toolbar(_:itemidentifier:canbeinsertedat:).md)
  Asks the delegate for a Boolean value that indicates whether the toolbar can place the item at the specified position.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [NSTabViewController](nstabviewcontroller.md)

## See Also

- [var delegate: (any NSToolbarDelegate)?](nstoolbar/delegate.md)
  The object you use to customize the toolbar contents and configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbardelegate)*