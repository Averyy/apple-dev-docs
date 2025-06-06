# window(_:willResizeForVersionBrowserWithMaxPreferredSize:maxAllowedSize:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate the window will resize for presentation during version browsing.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func window(_ window: NSWindow, willResizeForVersionBrowserWithMaxPreferredSize maxPreferredFrameSize: NSSize, maxAllowedSize maxAllowedFrameSize: NSSize) -> NSSize
```

#### Return Value

The size that the window should be.

#### Discussion

Windows entering the version browser will be resized to the size returned by this method. If either dimension of the returned size is larger than the `maxPreferredFrameSize`, the window will also be scaled down to ensure it fits properly in the version browser.

If this method is not implemented, the version browser will use [`windowWillUseStandardFrame(_:defaultFrame:)`](nswindowdelegate/windowwillusestandardframe(_:defaultframe:).md) to determine the resulting window frame size.

## Parameters

- `window`: The window being presented in a version browser.
- `maxPreferredFrameSize`: The maximum size the version browser would prefer the window to be.
- `maxAllowedFrameSize`: The maximum allowed size for the window (the full-screen frame minus the margins required to ensure the Versions controls are still visible).

## See Also

- [func windowWillEnterVersionBrowser(Notification)](nswindowdelegate/windowwillenterversionbrowser(_:).md)
  Tells the delegate the window is about to enter version browsing.
- [func windowDidEnterVersionBrowser(Notification)](nswindowdelegate/windowdidenterversionbrowser(_:).md)
  Tells the delegate that the window has entered version browsing.
- [func windowWillExitVersionBrowser(Notification)](nswindowdelegate/windowwillexitversionbrowser(_:).md)
  Tells the delegate that the window is about to leave version browsing.
- [func windowDidExitVersionBrowser(Notification)](nswindowdelegate/windowdidexitversionbrowser(_:).md)
  Tells the delegate that the window has left version browsing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/window(_:willresizeforversionbrowserwithmaxpreferredsize:maxallowedsize:))*