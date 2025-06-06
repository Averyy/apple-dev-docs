# performMiniaturize(_:)

**Framework**: AppKit  
**Kind**: method

Simulates the user clicking the minimize button by momentarily highlighting the button, then minimizing the window.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func performMiniaturize(_ sender: Any?)
```

#### Discussion

If the window doesn’t have a minimize button or can’t be minimized for some reason, the system emits the alert sound.

## Parameters

- `sender`: The message’s sender.

## See Also

- [var styleMask: NSWindow.StyleMask](nswindow/stylemask-swift.property.md)
  Flags that describe the window’s current style, such as if it’s resizable or in full-screen mode.
- [func close()](nswindow/close.md)
  Removes the window from the screen.
- [func performClose(Any?)](nswindow/performclose(_:).md)
  Simulates the user clicking the close button by momentarily highlighting the button and then closing the window.
- [var isMiniaturized: Bool](nswindow/isminiaturized.md)
  A Boolean value that indicates whether the window is minimized.
- [func miniaturize(Any?)](nswindow/miniaturize(_:).md)
  Removes the window from the screen list and displays the minimized window in the Dock.
- [func deminiaturize(Any?)](nswindow/deminiaturize(_:).md)
  De-minimizes the window.
- [var miniwindowImage: NSImage?](nswindow/miniwindowimage.md)
  The custom miniaturized window image of the window.
- [var miniwindowTitle: String!](nswindow/miniwindowtitle.md)
  The title displayed in the window’s minimized window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/performminiaturize(_:))*