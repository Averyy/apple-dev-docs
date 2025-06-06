# init(desktopIndependentWindow:)

**Framework**: ScreenCaptureKit  
**Kind**: init

Creates a filter that captures only the specified window.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
init(desktopIndependentWindow window: SCWindow)
```

## Parameters

- `window`: A window to capture.

## See Also

- [init(display: SCDisplay, including: [SCWindow])](sccontentfilter/init(display:including:).md)
  Creates a filter that captures only specific windows from a display.
- [init(display: SCDisplay, excludingWindows: [SCWindow])](sccontentfilter/init(display:excludingwindows:).md)
  Creates a filter that captures the contents of a display, excluding the specified windows.
- [init(display: SCDisplay, including: [SCRunningApplication], exceptingWindows: [SCWindow])](sccontentfilter/init(display:including:exceptingwindows:).md)
  Creates a filter that captures a display, including only windows of the specified apps.
- [init(display: SCDisplay, excludingApplications: [SCRunningApplication], exceptingWindows: [SCWindow])](sccontentfilter/init(display:excludingapplications:exceptingwindows:).md)
  Creates a filter that captures a display, excluding windows of the specified apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/sccontentfilter/init(desktopindependentwindow:))*