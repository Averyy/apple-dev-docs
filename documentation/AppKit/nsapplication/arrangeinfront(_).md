# arrangeInFront(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Arranges windows listed in the Window menu in front of all other windows.

**Availability**:
- macOS

## Declaration

```swift
func arrangeInFront(_ sender: Any?)
```

```objc
- (void) arrangeInFront:(id) sender;
```

#### Discussion

Windows associated with the app but not listed in the Window menu are not ordered to the front.

## Parameters

- `sender`: The object that sent the command.

## See Also

### Related Documentation
- [func addWindowsItem(NSWindow, title: String, filename: Bool)](./addwindowsitem%28_,title,filename%29.md)
  Adds an item to the Window menu for a given window.
- [func removeWindowsItem(NSWindow)](./removewindowsitem%28_%29.md)
  Removes the Window menu item for a given window.
- [func makeKeyAndOrderFront(Any?)](../nswindow/makekeyandorderfront%28_%29.md)
  Moves the window to the front of the screen list, within its level, and makes it the key window; that is, it shows the window.
### Managing Window Layers
- [func preventWindowOrdering()](./preventwindowordering%28%29.md)
  Suppresses the usual window ordering in handling the most recent mouse-down event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/arrangeinfront(_:))*