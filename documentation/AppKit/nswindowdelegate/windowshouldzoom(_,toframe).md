# windowShouldZoom(_:toFrame:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether the specified window should zoom to the specified frame.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func windowShouldZoom(_ window: NSWindow, toFrame newFrame: NSRect) -> Bool
```

```objc
- (BOOL) windowShouldZoom:(NSWindow *) window toFrame:(NSRect) newFrame;
```

#### Return Value

[`true`](../../Swift/true.md) to allow `window`’s frame to become `newFrame`; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `window`: The window being zoomed.
- `newFrame`: The rectangle to which the specified window is being zoomed.

## See Also

### Zooming Window
- [func windowWillUseStandardFrame(NSWindow, defaultFrame: NSRect) -> NSRect](./windowwillusestandardframe%28_,defaultframe%29.md)
  Called by `NSWindow`’s [`zoom(_:)`](../nswindow/zoom%28_%29.md) method while determining the frame a window may be zoomed to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowshouldzoom(_:toframe:))*