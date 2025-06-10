# broadcastController(_:didFinishWithError:)

**Framework**: ReplayKit  
**Kind**: method  
**Required**: Yes

Tells the delegate that a broadcast ended due to an error.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
optional func broadcastController(_ broadcastController: RPBroadcastController, didFinishWithError error: (any Error)?)
```

#### Discussion

Use the returned error to inform the user why the broadcast failed and provide an option to resume the broadcast, if applicable.

## Parameters

- `broadcastController`: The current controller instance.
- `error`: An   error indicating why the broadcast finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastcontrollerdelegate/broadcastcontroller(_:didfinishwitherror:))*