# toolbarDidRemoveItem(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the toolbar removed the specified item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func toolbarDidRemoveItem(_ notification: Notification)
```

```objc
- (void) toolbarDidRemoveItem:(NSNotification *) notification;
```

## Discussion

Use this method to update data structures related to your toolbar items.

## Parameters

- `notification`: A notification named [`didRemoveItemNotification`](../nstoolbar/didremoveitemnotification.md).

## See Also

### Adding and removing items
- [func toolbar(NSToolbar, itemForItemIdentifier: NSToolbarItem.Identifier, willBeInsertedIntoToolbar: Bool) -> NSToolbarItem?](./toolbar%28_,itemforitemidentifier,willbeinsertedintotoolbar%29.md)
  Asks the delegate for the toolbar item associated with the specified identifier.
- [func toolbarWillAddItem(Notification)](./toolbarwilladditem%28_%29.md)
  Tells the delegate that the toolbar is about to add the specified item.
- [NSToolbar.Identifier](../nstoolbar/identifier-swift.typealias.md)
  A string value that you use to differentiate your app’s toolbars.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbardelegate/toolbardidremoveitem(_:))*