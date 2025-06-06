# restoreUserActivityState(_:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Restores the state necessary to continue the specified user activity.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func restoreUserActivityState(_ userActivity: NSUserActivity)
```

#### Discussion

Implement this method to restore an object’s state using the specified user activity. The system calls this method on any responders or documents passed to the `restorationHandler` in [`application(_:continue:restorationHandler:)`](nsapplicationdelegate/application(_:continue:restorationhandler:).md). The system calls this method on the main thread. Your implementation should use the state data contained in the specified user activity’s [`userInfo`](https://developer.apple.com/documentation/foundation/nsuseractivity/1411706-userinfo) dictionary to restore the object.

On macOS, the system can automatically restore activities managed by [`NSDocument`](nsdocument.md) if you don’t implement [`application(_:continue:restorationHandler:)`](nsapplicationdelegate/application(_:continue:restorationhandler:).md), or if you return [`false`](https://developer.apple.com/documentation/swift/false). When this occurs, the system opens the document using [`openDocument(withContentsOf:display:completionHandler:)`](nsdocumentcontroller/opendocument(withcontentsof:display:completionhandler:).md), and calls `restoreUserActivityState` on it.

## Parameters

- `userActivity`: The user activity to continue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuseractivityrestoring/restoreuseractivitystate(_:))*