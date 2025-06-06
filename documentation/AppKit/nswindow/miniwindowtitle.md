# miniwindowTitle

**Framework**: AppKit  
**Kind**: property

The title displayed in the window’s minimized window.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var miniwindowTitle: String! { get set }
```

#### Discussion

A minimized window’s title usually reflects that of its full-size counterpart, abbreviated to fit if necessary. Although this property allows you to set the minimized window’s title explicitly, changing the full-size `NSWindow` object’s title (through [`title`](nswindow/title.md) or [`setTitleWithRepresentedFilename(_:)`](nswindow/settitlewithrepresentedfilename(_:).md)) automatically changes the minimized window’s title as well.

## See Also

- [var isMiniaturized: Bool](nswindow/isminiaturized.md)
  A Boolean value that indicates whether the window is minimized.
- [func performMiniaturize(Any?)](nswindow/performminiaturize(_:).md)
  Simulates the user clicking the minimize button by momentarily highlighting the button, then minimizing the window.
- [func miniaturize(Any?)](nswindow/miniaturize(_:).md)
  Removes the window from the screen list and displays the minimized window in the Dock.
- [func deminiaturize(Any?)](nswindow/deminiaturize(_:).md)
  De-minimizes the window.
- [var miniwindowImage: NSImage?](nswindow/miniwindowimage.md)
  The custom miniaturized window image of the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/miniwindowtitle)*