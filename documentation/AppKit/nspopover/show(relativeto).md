# show(relativeTo:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Shows the popover anchored to the specified toolbar item.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func show(relativeTo toolbarItem: NSToolbarItem)
```

```objc
- (void) showRelativeToToolbarItem:(NSToolbarItem *) toolbarItem;
```

#### Discussion

Use this method to display a popover relative to a toolbar item. When the item is in the overflow menu, the popover presents itself from another appropriate affordance in the window. See [`show(relativeTo:of:preferredEdge:)`](./show%28relativeto,of,preferrededge%29.md) for popover behavior.

This method raises an [`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md) if it can’t locate the toolbar item. This could occur if the item isn’t in a toolbar, or because the toolbar isn’t in the window.

## Parameters

- `toolbarItem`: The toolbar item anchoring the popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover/show(relativeto:))*