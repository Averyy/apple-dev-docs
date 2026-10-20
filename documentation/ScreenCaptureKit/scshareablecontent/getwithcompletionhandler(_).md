# getWithCompletionHandler(_:)

**Framework**: ScreenCaptureKit  
**Kind**: method  
**Role**: Type Method

Retrieves the displays, apps, and windows that your app can capture.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
class func getWithCompletionHandler(_ completionHandler: @escaping @Sendable (SCShareableContent?, (any Error)?) -> Void)
```

```swift
class var current: SCShareableContent { get async throws }
```

```objc
+ (void) getShareableContentWithCompletionHandler:(void (^)(SCShareableContent *shareableContent, NSError *error)) completionHandler;
```

#### Discussion

Use this method to retrieve the onscreen content that your app can capture. If the call is successful, the system returns the shareable content to the completion handler; otherwise, it returns an error that describes the failure.

## Parameters

- `completionHandler`: A callback the system invokes with the shareable content, or an error if a failure occurs.

## See Also

### Retrieving shareable content
- [class func getExcludingDesktopWindows(Bool, onScreenWindowsOnly: Bool, completionHandler: (SCShareableContent?, (any Error)?) -> Void)](./getexcludingdesktopwindows%28_,onscreenwindowsonly,completionhandler%29.md)
  Retrieves the displays, apps, and windows that match your criteria.
- [class func getExcludingDesktopWindows(Bool, onScreenWindowsOnlyAbove: SCWindow, completionHandler: (SCShareableContent?, (any Error)?) -> Void)](./getexcludingdesktopwindows%28_,onscreenwindowsonlyabove,completionhandler%29.md)
  Retrieves the displays, apps, and windows that are in front of the specified window.
- [class func getExcludingDesktopWindows(Bool, onScreenWindowsOnlyBelow: SCWindow, completionHandler: (SCShareableContent?, (any Error)?) -> Void)](./getexcludingdesktopwindows%28_,onscreenwindowsonlybelow,completionhandler%29.md)
  Retrieves the displays, apps, and windows that are behind the specified window.
- [class func info(for: SCContentFilter) -> SCShareableContentInfo](./info%28for%29.md)
  Retrieves any available sharable content information that matches the provided filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scshareablecontent/getwithcompletionhandler(_:))*