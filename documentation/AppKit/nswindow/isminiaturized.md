# isMiniaturized

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the window is minimized.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isMiniaturized: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) if the window is minimized; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false). A minimized window is removed from the screen and replaced by a image, icon, or button that represents it, called the counterpart.

## See Also

- [func performMiniaturize(Any?)](nswindow/performminiaturize(_:).md)
  Simulates the user clicking the minimize button by momentarily highlighting the button, then minimizing the window.
- [func miniaturize(Any?)](nswindow/miniaturize(_:).md)
  Removes the window from the screen list and displays the minimized window in the Dock.
- [func deminiaturize(Any?)](nswindow/deminiaturize(_:).md)
  De-minimizes the window.
- [var miniwindowImage: NSImage?](nswindow/miniwindowimage.md)
  The custom miniaturized window image of the window.
- [var miniwindowTitle: String!](nswindow/miniwindowtitle.md)
  The title displayed in the window’s minimized window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/isminiaturized)*