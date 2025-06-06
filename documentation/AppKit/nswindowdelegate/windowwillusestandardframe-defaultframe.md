# windowWillUseStandardFrame(_:defaultFrame:)

**Framework**: AppKit  
**Kind**: method

Called by `NSWindow`’s [`zoom(_:)`](nswindow/zoom(_:).md) method while determining the frame a window may be zoomed to.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func windowWillUseStandardFrame(_ window: NSWindow, defaultFrame newFrame: NSRect) -> NSRect
```

#### Return Value

The specified window’s standard frame.

#### Discussion

The standard frame for a window should supply the size and location that are “best” for the type of information shown in the window, taking into account the available display or displays. For example, the best width for a window that displays a word-processing document is the width of a page or the width of the display, whichever is smaller. The best height can be determined similarly. On return from this method, the [`zoom(_:)`](nswindow/zoom(_:).md) method modifies the returned standard frame, if necessary, to fit on the current screen.

## Parameters

- `window`: The window whose frame size is being determined.
- `newFrame`: The size of the current screen, which is the screen containing the largest part of the window’s current frame, possibly reduced on the top, bottom, left, or right, depending on the current interface style. The frame is reduced on the top to leave room for the menu bar.

## See Also

- [func windowShouldZoom(NSWindow, toFrame: NSRect) -> Bool](nswindowdelegate/windowshouldzoom(_:toframe:).md)
  Asks the delegate whether the specified window should zoom to the specified frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowwillusestandardframe(_:defaultframe:))*