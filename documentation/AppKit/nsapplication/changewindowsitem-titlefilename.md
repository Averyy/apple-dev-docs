# changeWindowsItem(_:title:filename:)

**Framework**: AppKit  
**Kind**: method

Changes the item for a given window in the Window menu to a given string.

**Availability**:
- macOS ?+

## Declaration

```swift
func changeWindowsItem(_ win: NSWindow, title string: String, filename isFilename: Bool)
```

## Parameters

- `win`: The window whose title you want to change in the Window menu. If `aWindow` is not in the Window menu, this method adds it.
- `string`: The string to display for the window’s menu item. How the string is interpreted is dependent on the value in the `isFilename` parameter.
- `isFilename`: If [`false`](https://developer.apple.com/documentation/Swift/false), `aString` appears literally in the menu; otherwise, `aString` is assumed to be a converted pathname with the name of the file preceding the path (the way the `NSWindow` method [`setTitleWithRepresentedFilename(_:)`](nswindow/settitlewithrepresentedfilename(_:).md) shows a title)

## See Also

- [var title: String](nswindow/title.md)
  The string that appears in the title bar of the window or the path to the represented file.
- [var windowsMenu: NSMenu?](nsapplication/windowsmenu.md)
  The Window menu of the app.
- [func addWindowsItem(NSWindow, title: String, filename: Bool)](nsapplication/addwindowsitem(_:title:filename:).md)
  Adds an item to the Window menu for a given window.
- [func removeWindowsItem(NSWindow)](nsapplication/removewindowsitem(_:).md)
  Removes the Window menu item for a given window.
- [func updateWindowsItem(NSWindow)](nsapplication/updatewindowsitem(_:).md)
  Updates the Window menu item for a given window to reflect the edited status of that window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/changewindowsitem(_:title:filename:))*