# requestSharingOfWindow(_:completionHandler:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 15.0+

## Declaration

```swift
func requestSharingOfWindow(_ window: NSWindow, completionHandler: @escaping ((any Error)?) -> Void)
```

```swift
func requestSharingOfWindow(_ window: NSWindow) async throws
```

```objc
- (void) requestSharingOfWindow:(NSWindow *) window completionHandler:(void (^)(NSError *error)) completionHandler;
```

#### Discussion

Request sharing of window.  If there is an available ScreenCaptureKit sharing session, an alert will be presented asking the user to confirm the share

The error will be non-nil if the request does not result in a window being shared.  The error will be NSUserCancelledError if there is no ScreenCaptureKit session, or if the user rejects the offer to share.  If sharing fails for some other reason, the error will provide the details.

## Parameters

- `window`: The window to share
- `completionHandler`: A completion block that is called after the request finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/requestsharingofwindow(_:completionhandler:))*