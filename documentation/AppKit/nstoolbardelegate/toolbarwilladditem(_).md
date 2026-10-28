# toolbarWillAddItem(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the toolbar is about to add the specified item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func toolbarWillAddItem(_ notification: Notification)
```

```objc
- (void) toolbarWillAddItem:(NSNotification *) notification;
```

## Discussion

Use this method to cache references to new toolbar items or perform any tasks related to the addition of those items.

## Parameters

- `notification`: A notification named [`willAddItemNotification`](../nstoolbar/willadditemnotification.md).

## See Also

### Adding and removing items
- [func toolbar(NSToolbar, itemForItemIdentifier: NSToolbarItem.Identifier, willBeInsertedIntoToolbar: Bool) -> NSToolbarItem?](./toolbar%28_,itemforitemidentifier,willbeinsertedintotoolbar%29.md)
  Asks the delegate for the toolbar item associated with the specified identifier.
- [func toolbarDidRemoveItem(Notification)](./toolbardidremoveitem%28_%29.md)
  Tells the delegate that the toolbar removed the specified item.
- [NSToolbar.Identifier](../nstoolbar/identifier-swift.typealias.md)
  A string value that you use to differentiate your app’s toolbars.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbardelegate/toolbarwilladditem(_:))*