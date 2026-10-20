# miniaturize(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes the window from the screen list and displays the minimized window in the Dock.

**Availability**:
- macOS

## Declaration

```swift
func miniaturize(_ sender: Any?)
```

```objc
- (void) miniaturize:(id) sender;
```

## Parameters

- `sender`: The message’s sender.

## See Also

### Minimizing Windows
- [var isMiniaturized: Bool](./isminiaturized.md)
  A Boolean value that indicates whether the window is minimized.
- [func performMiniaturize(Any?)](./performminiaturize%28_%29.md)
  Simulates the user clicking the minimize button by momentarily highlighting the button, then minimizing the window.
- [func deminiaturize(Any?)](./deminiaturize%28_%29.md)
  De-minimizes the window.
- [var miniwindowImage: NSImage?](./miniwindowimage.md)
  The custom miniaturized window image of the window.
- [var miniwindowTitle: String!](./miniwindowtitle.md)
  The title displayed in the window’s minimized window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/miniaturize(_:))*