# broadcastActivityController(_:didFinishWith:error:)

**Framework**: ReplayKit  
**Kind**: method  
**Required**: Yes

Tells the delegate that a user selected a broadcast.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func broadcastActivityController(_ broadcastActivityController: RPBroadcastActivityController, didFinishWith broadcastController: RPBroadcastController?, error: (any Error)?)
```

## Parameters

- `broadcastActivityController`: The broadcast activity controller instance.
- `broadcastController`: The broadcast controller instance used to start and stop broadcasts to a user selected service.
- `error`: An optional error indicating a failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastactivitycontrollerdelegate/broadcastactivitycontroller(_:didfinishwith:error:))*