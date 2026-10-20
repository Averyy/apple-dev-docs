# init(display:including:)

**Framework**: ScreenCaptureKit  
**Kind**: init  
**Role**: Initializer

Creates a filter that captures only specific windows from a display.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
init(display: SCDisplay, including includedWindows: [SCWindow])
```

```objc
- (instancetype) initWithDisplay:(SCDisplay *) display includingWindows:(NSArray<SCWindow *> *) includedWindows;
```

## Parameters

- `display`: A display to capture.
- `includedWindows`: An array of windows to include in the output.

## See Also

### Creating a filter
- [init(desktopIndependentWindow: SCWindow)](./init%28desktopindependentwindow%29.md)
  Creates a filter that captures only the specified window.
- [init(display: SCDisplay, excludingWindows: [SCWindow])](./init%28display,excludingwindows%29.md)
  Creates a filter that captures the contents of a display, excluding the specified windows.
- [init(display: SCDisplay, including: [SCRunningApplication], exceptingWindows: [SCWindow])](./init%28display,including,exceptingwindows%29.md)
  Creates a filter that captures a display, including only windows of the specified apps.
- [init(display: SCDisplay, excludingApplications: [SCRunningApplication], exceptingWindows: [SCWindow])](./init%28display,excludingapplications,exceptingwindows%29.md)
  Creates a filter that captures a display, excluding windows of the specified apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/sccontentfilter/init(display:including:))*