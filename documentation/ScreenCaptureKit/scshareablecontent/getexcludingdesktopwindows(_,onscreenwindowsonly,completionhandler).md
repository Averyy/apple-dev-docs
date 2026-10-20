# getExcludingDesktopWindows(_:onScreenWindowsOnly:completionHandler:)

**Framework**: ScreenCaptureKit  
**Kind**: method  
**Role**: Type Method

Retrieves the displays, apps, and windows that match your criteria.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
class func getExcludingDesktopWindows(_ excludeDesktopWindows: Bool, onScreenWindowsOnly: Bool, completionHandler: @escaping @Sendable (SCShareableContent?, (any Error)?) -> Void)
```

```swift
class func excludingDesktopWindows(_ excludeDesktopWindows: Bool, onScreenWindowsOnly: Bool) async throws -> SCShareableContent
```

```objc
+ (void) getShareableContentExcludingDesktopWindows:(BOOL) excludeDesktopWindows onScreenWindowsOnly:(BOOL) onScreenWindowsOnly completionHandler:(void (^)(SCShareableContent *shareableContent, NSError *error)) completionHandler;
```

#### Discussion

Use this method to retrieve the onscreen content matching your filtering criteria. If the call is successful, the system passes an [`SCShareableContent`](../scshareablecontent.md) instance to the completion handler; otherwise, it returns an error that describes the failure.

## Parameters

- `excludeDesktopWindows`: A Boolean value that indicates whether to exclude desktop windows like Finder, Dock, and Desktop from the set of shareable content.
- `onScreenWindowsOnly`: A Boolean value that indicates whether to include only onscreen windows in the set of shareable content.
- `completionHandler`: A callback the system invokes with the shareable content, or an error if a failure occurs.

## See Also

### Retrieving shareable content
- [class func getWithCompletionHandler((SCShareableContent?, (any Error)?) -> Void)](./getwithcompletionhandler%28_%29.md)
  Retrieves the displays, apps, and windows that your app can capture.
- [class func getExcludingDesktopWindows(Bool, onScreenWindowsOnlyAbove: SCWindow, completionHandler: (SCShareableContent?, (any Error)?) -> Void)](./getexcludingdesktopwindows%28_,onscreenwindowsonlyabove,completionhandler%29.md)
  Retrieves the displays, apps, and windows that are in front of the specified window.
- [class func getExcludingDesktopWindows(Bool, onScreenWindowsOnlyBelow: SCWindow, completionHandler: (SCShareableContent?, (any Error)?) -> Void)](./getexcludingdesktopwindows%28_,onscreenwindowsonlybelow,completionhandler%29.md)
  Retrieves the displays, apps, and windows that are behind the specified window.
- [class func info(for: SCContentFilter) -> SCShareableContentInfo](./info%28for%29.md)
  Retrieves any available sharable content information that matches the provided filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scshareablecontent/getexcludingdesktopwindows(_:onscreenwindowsonly:completionhandler:))*