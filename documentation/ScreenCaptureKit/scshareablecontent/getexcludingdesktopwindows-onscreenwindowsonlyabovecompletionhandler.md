# getExcludingDesktopWindows(_:onScreenWindowsOnlyAbove:completionHandler:)

**Framework**: ScreenCaptureKit  
**Kind**: method

Retrieves the displays, apps, and windows that are in front of the specified window.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
class func excludingDesktopWindows(_ excludeDesktopWindows: Bool, onScreenWindowsOnlyAbove window: SCWindow) async throws -> SCShareableContent
```

#### Discussion

Use this method to retrieve the onscreen content matching your filtering criteria. If the call is successful, the system passes an [`SCShareableContent`](scshareablecontent.md) instance to the completion handler; otherwise, it returns an error that describes the failure.

## Parameters

- `excludeDesktopWindows`: A Boolean value that indicates whether to exclude desktop windows like Finder, Dock, and Desktop from the set of shareable content.
- `window`: The window above which to retrieve shareable content.
- `completionHandler`: A callback the system invokes with the shareable content, or an error if a failure occurs.

## See Also

- [class func getWithCompletionHandler((SCShareableContent?, (any Error)?) -> Void)](scshareablecontent/getwithcompletionhandler(_:).md)
  Retrieves the displays, apps, and windows that your app can capture.
- [class func getExcludingDesktopWindows(Bool, onScreenWindowsOnly: Bool, completionHandler: (SCShareableContent?, (any Error)?) -> Void)](scshareablecontent/getexcludingdesktopwindows(_:onscreenwindowsonly:completionhandler:).md)
  Retrieves the displays, apps, and windows that match your criteria.
- [class func getExcludingDesktopWindows(Bool, onScreenWindowsOnlyBelow: SCWindow, completionHandler: (SCShareableContent?, (any Error)?) -> Void)](scshareablecontent/getexcludingdesktopwindows(_:onscreenwindowsonlybelow:completionhandler:).md)
  Retrieves the displays, apps, and windows that are behind the specified window.
- [class func info(for: SCContentFilter) -> SCShareableContentInfo](scshareablecontent/info(for:).md)
  Retrieves any available sharable content information that matches the provided filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scshareablecontent/getexcludingdesktopwindows(_:onscreenwindowsonlyabove:completionhandler:))*