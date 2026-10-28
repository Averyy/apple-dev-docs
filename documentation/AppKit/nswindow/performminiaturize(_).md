# performMiniaturize(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Simulates the user clicking the minimize button by momentarily highlighting the button, then minimizing the window.

**Availability**:
- macOS

## Declaration

```swift
func performMiniaturize(_ sender: Any?)
```

```objc
- (void) performMiniaturize:(id) sender;
```

## Discussion

If the window doesn’t have a minimize button or can’t be minimized for some reason, the system emits the alert sound.

## Parameters

- `sender`: The message’s sender.

## See Also

### Related Documentation
- [var styleMask: NSWindow.StyleMask](./stylemask-swift.property.md)
  Flags that describe the window’s current style, such as if it’s resizable or in full-screen mode.
- [func close()](./close%28%29.md)
  Removes the window from the screen.
- [func performClose(Any?)](./performclose%28_%29.md)
  Simulates the user clicking the close button by momentarily highlighting the button and then closing the window.
### Minimizing Windows
- [var isMiniaturized: Bool](./isminiaturized.md)
  A Boolean value that indicates whether the window is minimized.
- [func miniaturize(Any?)](./miniaturize%28_%29.md)
  Removes the window from the screen list and displays the minimized window in the Dock.
- [func deminiaturize(Any?)](./deminiaturize%28_%29.md)
  De-minimizes the window.
- [var miniwindowImage: NSImage?](./miniwindowimage.md)
  The custom miniaturized window image of the window.
- [var miniwindowTitle: String!](./miniwindowtitle.md)
  The title displayed in the window’s minimized window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/performminiaturize(_:))*