# init(display:excludingWindows:)

**Framework**: ScreenCaptureKit  
**Kind**: init  
**Role**: Initializer

Creates a filter that captures the contents of a display, excluding the specified windows.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
init(display: SCDisplay, excludingWindows excluded: [SCWindow])
```

```objc
- (instancetype) initWithDisplay:(SCDisplay *) display excludingWindows:(NSArray<SCWindow *> *) excluded;
```

## Parameters

- `display`: A display to capture.
- `excluded`: An array of windows to exclude from the output.

## See Also

### Creating a filter
- [init(desktopIndependentWindow: SCWindow)](./init%28desktopindependentwindow%29.md)
  Creates a filter that captures only the specified window.
- [init(display: SCDisplay, including: [SCWindow])](./init%28display,including%29.md)
  Creates a filter that captures only specific windows from a display.
- [init(display: SCDisplay, including: [SCRunningApplication], exceptingWindows: [SCWindow])](./init%28display,including,exceptingwindows%29.md)
  Creates a filter that captures a display, including only windows of the specified apps.
- [init(display: SCDisplay, excludingApplications: [SCRunningApplication], exceptingWindows: [SCWindow])](./init%28display,excludingapplications,exceptingwindows%29.md)
  Creates a filter that captures a display, excluding windows of the specified apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/sccontentfilter/init(display:excludingwindows:))*