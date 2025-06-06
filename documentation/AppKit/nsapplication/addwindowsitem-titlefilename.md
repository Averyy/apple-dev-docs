# addWindowsItem(_:title:filename:)

**Framework**: AppKit  
**Kind**: method

Adds an item to the Window menu for a given window.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func addWindowsItem(_ win: NSWindow, title string: String, filename isFilename: Bool)
```

#### Discussion

You rarely need to invoke this method directly because Cocoa places an item in the Window menu automatically whenever you set the title of an `NSWindow` object.

## Parameters

- `win`: The window being added to the menu. If this window object already exists in the Window menu, this method has no effect.
- `string`: The string to display for the window’s menu item. How the string is interpreted is dependent on the value in the   parameter.
- `isFilename`: If  ,   appears literally in the menu; otherwise,   is assumed to be a converted pathname with the name of the file preceding the path (the way the   method   shows a title)

## See Also

- [var title: String](nswindow/title.md)
  The string that appears in the title bar of the window or the path to the represented file.
- [var windowsMenu: NSMenu?](nsapplication/windowsmenu.md)
  The Window menu of the app.
- [func changeWindowsItem(NSWindow, title: String, filename: Bool)](nsapplication/changewindowsitem(_:title:filename:).md)
  Changes the item for a given window in the Window menu to a given string.
- [func removeWindowsItem(NSWindow)](nsapplication/removewindowsitem(_:).md)
  Removes the Window menu item for a given window.
- [func updateWindowsItem(NSWindow)](nsapplication/updatewindowsitem(_:).md)
  Updates the Window menu item for a given window to reflect the edited status of that window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/addwindowsitem(_:title:filename:))*