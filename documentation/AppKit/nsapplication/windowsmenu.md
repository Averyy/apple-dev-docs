# windowsMenu

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The Window menu of the app.

**Availability**:
- macOS

## Declaration

```swift
var windowsMenu: NSMenu? { get set }
```

```objc
@property (strong, nullable) NSMenu * windowsMenu;
```

#### Return Value

The window menu or `nil` if such a menu does not exist or has not yet been created.

#### Discussion

This property contains the app’s Window menu or `nil` if such a menu does not yet exist or has not yet been created. You can use this property to specify the Window menu for your app.

## See Also

### Managing the Window Menu
- [func addWindowsItem(NSWindow, title: String, filename: Bool)](./addwindowsitem%28_,title,filename%29.md)
  Adds an item to the Window menu for a given window.
- [func changeWindowsItem(NSWindow, title: String, filename: Bool)](./changewindowsitem%28_,title,filename%29.md)
  Changes the item for a given window in the Window menu to a given string.
- [func removeWindowsItem(NSWindow)](./removewindowsitem%28_%29.md)
  Removes the Window menu item for a given window.
- [func updateWindowsItem(NSWindow)](./updatewindowsitem%28_%29.md)
  Updates the Window menu item for a given window to reflect the edited status of that window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/windowsmenu)*