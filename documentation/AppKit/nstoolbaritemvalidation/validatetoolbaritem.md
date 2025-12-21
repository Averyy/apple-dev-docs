# validateToolbarItem(_:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Determines whether to enable or disable the toolbar item.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func validateToolbarItem(_ item: NSToolbarItem) -> Bool
```

#### Discussion

If this method is implemented and returns [`false`](https://developer.apple.com/documentation/Swift/false), [`NSToolbar`](nstoolbar.md) will disable `item`. Returning [`true`](https://developer.apple.com/documentation/Swift/true) causes `item` to be enabled.

[`NSToolbar`](nstoolbar.md) only calls this method for image items.

> **Note**:  [`validateToolbarItem:`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/validateToolbarItem:) is called very frequently, so it must be efficient.

If the receiver is the `target` for the actions of multiple toolbar items, it’s necessary to determine which toolbar item `item` refers to by testing the `itemIdentifier`.

```objc
-(BOOL)validateToolbarItem:(NSToolbarItem *)toolbarItem
{
    BOOL enable = NO;
    if ([[toolbarItem itemIdentifier] isEqual:SaveDocToolbarItemIdentifier]) {
        // We will return YES (enable the save item)
        // only when the document is dirty and needs saving
        enable = [self isDocumentEdited];
    } else if ([[toolbarItem itemIdentifier] isEqual:NSToolbarPrintItemIdentifier]) {
        // always enable print for this window
        enable = YES;
    }
    return enable;
}
```

## See Also

- [func validateVisibleItems()](nstoolbar/validatevisibleitems.md)
  Validates the toolbar’s visible items during a window update.
- [var action: Selector?](nstoolbaritem/action.md)
  The action method to call when someone clicks on the toolbar item.
- [var target: AnyObject?](nstoolbaritem/target.md)
  The object that defines the action method the toolbar item calls when clicked.
- [Toolbar Programming Topics for Cocoa](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Toolbars/Toolbars.html#//apple_ref/doc/uid/10000109i)
- [func validate()](nstoolbaritem/validate.md)
  Validates the toolbar item’s menu and its ability to perfrom its action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritemvalidation/validatetoolbaritem(_:))*