# miniaturize(_:)

**Framework**: AppKit  
**Kind**: method

Removes the window from the screen list and displays the minimized window in the Dock.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func miniaturize(_ sender: Any?)
```

## Parameters

- `sender`: The message’s sender.

## See Also

- [var isMiniaturized: Bool](nswindow/isminiaturized.md)
  A Boolean value that indicates whether the window is minimized.
- [func performMiniaturize(Any?)](nswindow/performminiaturize(_:).md)
  Simulates the user clicking the minimize button by momentarily highlighting the button, then minimizing the window.
- [func deminiaturize(Any?)](nswindow/deminiaturize(_:).md)
  De-minimizes the window.
- [var miniwindowImage: NSImage?](nswindow/miniwindowimage.md)
  The custom miniaturized window image of the window.
- [var miniwindowTitle: String!](nswindow/miniwindowtitle.md)
  The title displayed in the window’s minimized window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/miniaturize(_:))*