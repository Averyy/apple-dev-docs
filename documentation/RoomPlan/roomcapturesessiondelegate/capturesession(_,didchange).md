# captureSession(_:didChange:)

**Framework**: RoomPlan  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Notifies the delegate when the session changes the dimensions and the transform properties of surfaces and objects.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
func captureSession(_ session: RoomCaptureSession, didChange room: CapturedRoom)
```

## Parameters

- `session`: An object that manages the room-scanning process.
- `room`: A structure that contains only the surfaces/objects that experience recent changes.

## Default Implementations

### RoomCaptureSessionDelegate Implementations
- [func captureSession(RoomCaptureSession, didChange: CapturedRoom)](./capturesession%28_,didchange%29-gv3t.md)
  Provides a default, blank implementation for when the capture session updates the dimensions and the transform properties during a scan.

## See Also

### Updating a session
- [func captureSession(RoomCaptureSession, didAdd: CapturedRoom)](./capturesession%28_,didadd%29.md)
  Notifies the delegate of newly added surfaces and objects.
- [func captureSession(RoomCaptureSession, didRemove: CapturedRoom)](./capturesession%28_,didremove%29.md)
  Notifies the delegate when the session removes surfaces and objects.
- [func captureSession(RoomCaptureSession, didUpdate: CapturedRoom)](./capturesession%28_,didupdate%29.md)
  Notifies the delegate when the session updates the scan results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcapturesessiondelegate/capturesession(_:didchange:))*