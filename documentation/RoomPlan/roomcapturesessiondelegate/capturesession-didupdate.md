# captureSession(_:didUpdate:)

**Framework**: RoomPlan  
**Kind**: method  
**Required**: Yes

Notifies the delegate when the session updates the scan results.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS ?+

## Declaration

```swift
func captureSession(_ session: RoomCaptureSession, didUpdate room: CapturedRoom)
```

#### Discussion

The `room` structure contains all surfaces/objects in the captured room regardless of the recent changes.

## Parameters

- `session`: An object that manages the room-scanning process.
- `room`: A structure that represents a snapshot of the room being captured.

## See Also

- [func captureSession(RoomCaptureSession, didAdd: CapturedRoom)](roomcapturesessiondelegate/capturesession(_:didadd:).md)
  Notifies the delegate of newly added surfaces and objects.
- [func captureSession(RoomCaptureSession, didRemove: CapturedRoom)](roomcapturesessiondelegate/capturesession(_:didremove:).md)
  Notifies the delegate when the session removes surfaces and objects.
- [func captureSession(RoomCaptureSession, didChange: CapturedRoom)](roomcapturesessiondelegate/capturesession(_:didchange:).md)
  Notifies the delegate when the session changes the dimensions and the transform properties of surfaces and objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcapturesessiondelegate/capturesession(_:didupdate:))*