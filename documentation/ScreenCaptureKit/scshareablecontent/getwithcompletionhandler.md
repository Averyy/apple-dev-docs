# getWithCompletionHandler(_:)

**Framework**: ScreenCaptureKit  
**Kind**: method

Retrieves the displays, apps, and windows that your app can capture.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
class var current: SCShareableContent { get async throws }
```

#### Discussion

Use this method to retrieve the onscreen content that your app can capture. If the call is successful, the system returns the shareable content to the completion handler; otherwise, it returns an error that describes the failure.

## Parameters

- `completionHandler`: A callback the system invokes with the shareable content, or an error if a failure occurs.

## See Also

- [class func getExcludingDesktopWindows(Bool, onScreenWindowsOnly: Bool, completionHandler: (SCShareableContent?, (any Error)?) -> Void)](scshareablecontent/getexcludingdesktopwindows(_:onscreenwindowsonly:completionhandler:).md)
  Retrieves the displays, apps, and windows that match your criteria.
- [class func getExcludingDesktopWindows(Bool, onScreenWindowsOnlyAbove: SCWindow, completionHandler: (SCShareableContent?, (any Error)?) -> Void)](scshareablecontent/getexcludingdesktopwindows(_:onscreenwindowsonlyabove:completionhandler:).md)
  Retrieves the displays, apps, and windows that are in front of the specified window.
- [class func getExcludingDesktopWindows(Bool, onScreenWindowsOnlyBelow: SCWindow, completionHandler: (SCShareableContent?, (any Error)?) -> Void)](scshareablecontent/getexcludingdesktopwindows(_:onscreenwindowsonlybelow:completionhandler:).md)
  Retrieves the displays, apps, and windows that are behind the specified window.
- [class func info(for: SCContentFilter) -> SCShareableContentInfo](scshareablecontent/info(for:).md)
  Retrieves any available sharable content information that matches the provided filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scshareablecontent/getwithcompletionhandler(_:))*