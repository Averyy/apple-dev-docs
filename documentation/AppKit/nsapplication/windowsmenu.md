# windowsMenu

**Framework**: AppKit  
**Kind**: property

The Window menu of the app.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var windowsMenu: NSMenu? { get set }
```

#### Return Value

The window menu or `nil` if such a menu does not exist or has not yet been created.

#### Discussion

This property contains the app’s Window menu or `nil` if such a menu does not yet exist or has not yet been created. You can use this property to specify the Window menu for your app.

## See Also

- [func addWindowsItem(NSWindow, title: String, filename: Bool)](nsapplication/addwindowsitem(_:title:filename:).md)
  Adds an item to the Window menu for a given window.
- [func changeWindowsItem(NSWindow, title: String, filename: Bool)](nsapplication/changewindowsitem(_:title:filename:).md)
  Changes the item for a given window in the Window menu to a given string.
- [func removeWindowsItem(NSWindow)](nsapplication/removewindowsitem(_:).md)
  Removes the Window menu item for a given window.
- [func updateWindowsItem(NSWindow)](nsapplication/updatewindowsitem(_:).md)
  Updates the Window menu item for a given window to reflect the edited status of that window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/windowsmenu)*