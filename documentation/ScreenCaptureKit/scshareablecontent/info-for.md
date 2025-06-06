# info(for:)

**Framework**: ScreenCaptureKit  
**Kind**: method

Retrieves any available sharable content information that matches the provided filter.

**Availability**:
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
class func info(for filter: SCContentFilter) -> SCShareableContentInfo
```

#### Return Value

The sharable content matching the filter, or `nil` if none is found.

## Parameters

- `filter`: The filter to match current sharable content against.

## See Also

- [class func getWithCompletionHandler((SCShareableContent?, (any Error)?) -> Void)](scshareablecontent/getwithcompletionhandler(_:).md)
  Retrieves the displays, apps, and windows that your app can capture.
- [class func getExcludingDesktopWindows(Bool, onScreenWindowsOnly: Bool, completionHandler: (SCShareableContent?, (any Error)?) -> Void)](scshareablecontent/getexcludingdesktopwindows(_:onscreenwindowsonly:completionhandler:).md)
  Retrieves the displays, apps, and windows that match your criteria.
- [class func getExcludingDesktopWindows(Bool, onScreenWindowsOnlyAbove: SCWindow, completionHandler: (SCShareableContent?, (any Error)?) -> Void)](scshareablecontent/getexcludingdesktopwindows(_:onscreenwindowsonlyabove:completionhandler:).md)
  Retrieves the displays, apps, and windows that are in front of the specified window.
- [class func getExcludingDesktopWindows(Bool, onScreenWindowsOnlyBelow: SCWindow, completionHandler: (SCShareableContent?, (any Error)?) -> Void)](scshareablecontent/getexcludingdesktopwindows(_:onscreenwindowsonlybelow:completionhandler:).md)
  Retrieves the displays, apps, and windows that are behind the specified window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scshareablecontent/info(for:))*