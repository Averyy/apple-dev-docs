# info(for:)

**Framework**: ScreenCaptureKit  
**Kind**: method  
**Role**: Type Method

Retrieves any available sharable content information that matches the provided filter.

**Availability**:
- Mac Catalyst 18.2+
- macOS 14.0+

## Declaration

```swift
class func info(for filter: SCContentFilter) -> SCShareableContentInfo
```

```objc
+ (SCShareableContentInfo *) infoForFilter:(SCContentFilter *) filter;
```

#### Return Value

The sharable content matching the filter, or `nil` if none is found.

## Parameters

- `filter`: The filter to match current sharable content against.

## See Also

### Retrieving shareable content
- [class func getWithCompletionHandler((SCShareableContent?, (any Error)?) -> Void)](./getwithcompletionhandler%28_%29.md)
  Retrieves the displays, apps, and windows that your app can capture.
- [class func getExcludingDesktopWindows(Bool, onScreenWindowsOnly: Bool, completionHandler: (SCShareableContent?, (any Error)?) -> Void)](./getexcludingdesktopwindows%28_,onscreenwindowsonly,completionhandler%29.md)
  Retrieves the displays, apps, and windows that match your criteria.
- [class func getExcludingDesktopWindows(Bool, onScreenWindowsOnlyAbove: SCWindow, completionHandler: (SCShareableContent?, (any Error)?) -> Void)](./getexcludingdesktopwindows%28_,onscreenwindowsonlyabove,completionhandler%29.md)
  Retrieves the displays, apps, and windows that are in front of the specified window.
- [class func getExcludingDesktopWindows(Bool, onScreenWindowsOnlyBelow: SCWindow, completionHandler: (SCShareableContent?, (any Error)?) -> Void)](./getexcludingdesktopwindows%28_,onscreenwindowsonlybelow,completionhandler%29.md)
  Retrieves the displays, apps, and windows that are behind the specified window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scshareablecontent/info(for:))*