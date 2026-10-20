# broadcastActivityController(_:didFinishWith:error:)

**Framework**: ReplayKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate that a user selected a broadcast.

**Availability**:
- macOS 11.0+ - Deprecated in 27.0

> **Deprecated**: No longer supported

## Declaration

```swift
func broadcastActivityController(_ broadcastActivityController: RPBroadcastActivityController, didFinishWith broadcastController: RPBroadcastController?, error: (any Error)?)
```

```objc
- (void) broadcastActivityController:(RPBroadcastActivityController *) broadcastActivityController didFinishWithBroadcastController:(RPBroadcastController *) broadcastController error:(NSError *) error;
```

## Parameters

- `broadcastActivityController`: The broadcast activity controller instance.
- `broadcastController`: The broadcast controller instance used to start and stop broadcasts to a user selected service.
- `error`: An optional error indicating a failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastactivitycontrollerdelegate/broadcastactivitycontroller(_:didfinishwith:error:))*