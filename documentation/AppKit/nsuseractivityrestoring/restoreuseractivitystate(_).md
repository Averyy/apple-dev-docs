# restoreUserActivityState(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Restores the state necessary to continue the specified user activity.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func restoreUserActivityState(_ userActivity: NSUserActivity)
```

```objc
- (void) restoreUserActivityState:(NSUserActivity *) userActivity;
```

## Discussion

Implement this method to restore an object’s state using the specified user activity. The system calls this method on any responders or documents passed to the `restorationHandler` in [`application(_:continue:restorationHandler:)`](../nsapplicationdelegate/application%28_,continue,restorationhandler%29.md). The system calls this method on the main thread. Your implementation should use the state data contained in the specified user activity’s [`userInfo`](../../Foundation/nsuseractivity/userinfo.md) dictionary to restore the object.

On macOS, the system can automatically restore activities managed by [`NSDocument`](../nsdocument.md) if you don’t implement [`application(_:continue:restorationHandler:)`](../nsapplicationdelegate/application%28_,continue,restorationhandler%29.md), or if you return [`false`](../../Swift/false.md). When this occurs, the system opens the document using [`openDocument(withContentsOf:display:completionHandler:)`](../nsdocumentcontroller/opendocument%28withcontentsof,display,completionhandler%29.md), and calls `restoreUserActivityState` on it.

## Parameters

- `userActivity`: The user activity to continue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuseractivityrestoring/restoreuseractivitystate(_:))*