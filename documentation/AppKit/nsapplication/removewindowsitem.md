# removeWindowsItem(_:)

**Framework**: AppKit  
**Kind**: method

Removes the Window menu item for a given window.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func removeWindowsItem(_ win: NSWindow)
```

#### Discussion

This method doesn’t prevent the item from being automatically added again. Use the [`isExcludedFromWindowsMenu`](nswindow/isexcludedfromwindowsmenu.md) method of [`NSWindow`](nswindow.md) if you want the item to remain excluded from the Window menu.

## Parameters

- `win`: The window whose menu item is to be removed.

## See Also

- [var windowsMenu: NSMenu?](nsapplication/windowsmenu.md)
  The Window menu of the app.
- [func addWindowsItem(NSWindow, title: String, filename: Bool)](nsapplication/addwindowsitem(_:title:filename:).md)
  Adds an item to the Window menu for a given window.
- [func changeWindowsItem(NSWindow, title: String, filename: Bool)](nsapplication/changewindowsitem(_:title:filename:).md)
  Changes the item for a given window in the Window menu to a given string.
- [func updateWindowsItem(NSWindow)](nsapplication/updatewindowsitem(_:).md)
  Updates the Window menu item for a given window to reflect the edited status of that window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/removewindowsitem(_:))*