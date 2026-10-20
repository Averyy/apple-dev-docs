# broadcastActivityViewController(_:didFinishWith:error:)

**Framework**: ReplayKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Indicates that the broadcast activity view controller is ready to be dismissed.

**Availability**:
- iOS 10.0+ - Deprecated in 27.0
- iPadOS 10.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: No longer supported

## Declaration

```swift
func broadcastActivityViewController(_ broadcastActivityViewController: RPBroadcastActivityViewController, didFinishWith broadcastController: RPBroadcastController?, error: (any Error)?)
```

```objc
- (void) broadcastActivityViewController:(RPBroadcastActivityViewController *) broadcastActivityViewController didFinishWithBroadcastController:(RPBroadcastController *) broadcastController error:(NSError *) error;
```

#### Discussion

When this method is called after a broadcast has been set up successfully, retain a reference to the [`RPBroadcastController`](../rpbroadcastcontroller.md) instance contained in the `broadcastController` parameter to start and stop broadcasting.

## Parameters

- `broadcastActivityViewController`: The broadcast activity view controller to be dismissed.
- `broadcastController`: Optional. The [`RPBroadcastController`](../rpbroadcastcontroller.md) instance used to start and stop broadcasts to a selected service.  When the user cancels service setup, this parameter is nil.
- `error`: An [`RPRecordingErrorDomain`](../rprecordingerrordomain.md) error. When a connection to a broadcast service has been set up successfully and the app is ready to broadcast, this parameter is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastactivityviewcontrollerdelegate/broadcastactivityviewcontroller(_:didfinishwith:error:))*