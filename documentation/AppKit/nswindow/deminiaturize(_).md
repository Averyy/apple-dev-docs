# deminiaturize(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

De-minimizes the window.

**Availability**:
- macOS

## Declaration

```swift
func deminiaturize(_ sender: Any?)
```

```objc
- (void) deminiaturize:(id) sender;
```

## Discussion

Invoke this method to programmatically deminimize a minimized window in the Dock.

## Parameters

- `sender`: The message’s sender.

## See Also

### Related Documentation
- [var styleMask: NSWindow.StyleMask](./stylemask-swift.property.md)
  Flags that describe the window’s current style, such as if it’s resizable or in full-screen mode.
### Minimizing Windows
- [var isMiniaturized: Bool](./isminiaturized.md)
  A Boolean value that indicates whether the window is minimized.
- [func performMiniaturize(Any?)](./performminiaturize%28_%29.md)
  Simulates the user clicking the minimize button by momentarily highlighting the button, then minimizing the window.
- [func miniaturize(Any?)](./miniaturize%28_%29.md)
  Removes the window from the screen list and displays the minimized window in the Dock.
- [var miniwindowImage: NSImage?](./miniwindowimage.md)
  The custom miniaturized window image of the window.
- [var miniwindowTitle: String!](./miniwindowtitle.md)
  The title displayed in the window’s minimized window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/deminiaturize(_:))*