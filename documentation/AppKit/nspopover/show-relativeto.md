# show(relativeTo:)

**Framework**: AppKit  
**Kind**: method

Shows the popover anchored to the specified toolbar item.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
func show(relativeTo toolbarItem: NSToolbarItem)
```

#### Discussion

Use this method to display a popover relative to a toolbar item. When the item is in the overflow menu, the popover presents itself from another appropriate affordance in the window. See [`show(relativeTo:of:preferredEdge:)`](nspopover/show(relativeto:of:preferrededge:).md) for popover behavior.

This method raises an [`invalidArgumentException`](https://developer.apple.com/documentation/foundation/nsexceptionname/1415426-invalidargumentexception) if it can’t locate the toolbar item. This could occur if the item isn’t in a toolbar, or because the toolbar isn’t in the window.

## Parameters

- `toolbarItem`: The toolbar item anchoring the popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover/show(relativeto:))*