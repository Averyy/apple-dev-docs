# arrangeInFront(_:)

**Framework**: AppKit  
**Kind**: method

Arranges windows listed in the Window menu in front of all other windows.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func arrangeInFront(_ sender: Any?)
```

#### Discussion

Windows associated with the app but not listed in the Window menu are not ordered to the front.

## Parameters

- `sender`: The object that sent the command.

## See Also

- [func addWindowsItem(NSWindow, title: String, filename: Bool)](nsapplication/addwindowsitem(_:title:filename:).md)
  Adds an item to the Window menu for a given window.
- [func removeWindowsItem(NSWindow)](nsapplication/removewindowsitem(_:).md)
  Removes the Window menu item for a given window.
- [func makeKeyAndOrderFront(Any?)](nswindow/makekeyandorderfront(_:).md)
  Moves the window to the front of the screen list, within its level, and makes it the key window; that is, it shows the window.
- [func preventWindowOrdering()](nsapplication/preventwindowordering.md)
  Suppresses the usual window ordering in handling the most recent mouse-down event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/arrangeinfront(_:))*