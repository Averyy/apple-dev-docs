# updateWindowsItem(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Updates the Window menu item for a given window to reflect the edited status of that window.

**Availability**:
- macOS

## Declaration

```swift
func updateWindowsItem(_ win: NSWindow)
```

```objc
- (void) updateWindowsItem:(NSWindow *) win;
```

#### Discussion

You rarely need to invoke this method because it is invoked automatically when the edit status of an [`NSWindow`](../nswindow.md) object is set.

## Parameters

- `win`: The window whose menu item is to be updated.

## See Also

### Related Documentation
- [var isDocumentEdited: Bool](../nswindow/isdocumentedited.md)
  A Boolean value that indicates whether the window’s document has been edited.
### Managing the Window Menu
- [var windowsMenu: NSMenu?](./windowsmenu.md)
  The Window menu of the app.
- [func addWindowsItem(NSWindow, title: String, filename: Bool)](./addwindowsitem%28_,title,filename%29.md)
  Adds an item to the Window menu for a given window.
- [func changeWindowsItem(NSWindow, title: String, filename: Bool)](./changewindowsitem%28_,title,filename%29.md)
  Changes the item for a given window in the Window menu to a given string.
- [func removeWindowsItem(NSWindow)](./removewindowsitem%28_%29.md)
  Removes the Window menu item for a given window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/updatewindowsitem(_:))*