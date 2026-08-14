# windowShouldZoom(_:toFrame:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate whether the specified window should zoom to the specified frame.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func windowShouldZoom(_ window: NSWindow, toFrame newFrame: NSRect) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) to allow `window`’s frame to become `newFrame`; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `window`: The window being zoomed.
- `newFrame`: The rectangle to which the specified window is being zoomed.

## See Also

- [func windowWillUseStandardFrame(NSWindow, defaultFrame: NSRect) -> NSRect](nswindowdelegate/windowwillusestandardframe(_:defaultframe:).md)
  Called by `NSWindow`’s [`zoom(_:)`](nswindow/zoom(_:).md) method while determining the frame a window may be zoomed to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowshouldzoom(_:toframe:))*