# init(display:including:exceptingWindows:)

**Framework**: ScreenCaptureKit  
**Kind**: init

Creates a filter that captures a display, including only windows of the specified apps.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
init(display: SCDisplay, including applications: [SCRunningApplication], exceptingWindows: [SCWindow])
```

#### Discussion

The initializer arguments provide a three-stage filter that gives you fine-grained control over the output:

1. Specify a display to capture. If you don’t specify additional filter criteria, the stream includes all content for a display.
2. Specify one or more apps to capture only the windows that they own.
3. Specify one or more windows that are exceptions to the previous rules. If the previous rules include a window, specifying it as an exception excludes it from the output. Likewise, if the previous rules exclude a window, specifying it as an exception includes it in the output.

## Parameters

- `display`: A display to capture.
- `applications`: An array of apps with windows to capture.
- `exceptingWindows`: An array of windows that are exceptions to the previous rules.

## See Also

- [init(desktopIndependentWindow: SCWindow)](sccontentfilter/init(desktopindependentwindow:).md)
  Creates a filter that captures only the specified window.
- [init(display: SCDisplay, including: [SCWindow])](sccontentfilter/init(display:including:).md)
  Creates a filter that captures only specific windows from a display.
- [init(display: SCDisplay, excludingWindows: [SCWindow])](sccontentfilter/init(display:excludingwindows:).md)
  Creates a filter that captures the contents of a display, excluding the specified windows.
- [init(display: SCDisplay, excludingApplications: [SCRunningApplication], exceptingWindows: [SCWindow])](sccontentfilter/init(display:excludingapplications:exceptingwindows:).md)
  Creates a filter that captures a display, excluding windows of the specified apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/sccontentfilter/init(display:including:exceptingwindows:))*