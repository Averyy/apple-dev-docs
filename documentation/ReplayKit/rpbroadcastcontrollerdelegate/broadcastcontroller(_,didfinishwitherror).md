# broadcastController(_:didFinishWithError:)

**Framework**: ReplayKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that a broadcast ended due to an error.

**Availability**:
- iOS 10.0+ - Deprecated in 27.0
- iPadOS 10.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: No longer supported

## Declaration

```swift
optional func broadcastController(_ broadcastController: RPBroadcastController, didFinishWithError error: (any Error)?)
```

```objc
- (void) broadcastController:(RPBroadcastController *) broadcastController didFinishWithError:(NSError *) error;
```

## Discussion

Use the returned error to inform the user why the broadcast failed and provide an option to resume the broadcast, if applicable.

## Parameters

- `broadcastController`: The current controller instance.
- `error`: An [`RPRecordingErrorCode`](../rprecordingerrorcode.md) error indicating why the broadcast finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastcontrollerdelegate/broadcastcontroller(_:didfinishwitherror:))*