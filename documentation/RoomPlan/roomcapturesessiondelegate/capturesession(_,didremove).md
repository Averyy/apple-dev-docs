# captureSession(_:didRemove:)

**Framework**: RoomPlan  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Notifies the delegate when the session removes surfaces and objects.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
func captureSession(_ session: RoomCaptureSession, didRemove room: CapturedRoom)
```

## Parameters

- `session`: An object that manages the room-scanning process.
- `room`: A structure that contains surfaces and objects that the framework removes from the scan.

## Default Implementations

### RoomCaptureSessionDelegate Implementations
- [func captureSession(RoomCaptureSession, didRemove: CapturedRoom)](./capturesession%28_,didremove%29-9gs76.md)
  Provides a default, blank implementation for when the session removes surfaces and objects.

## See Also

### Updating a session
- [func captureSession(RoomCaptureSession, didAdd: CapturedRoom)](./capturesession%28_,didadd%29.md)
  Notifies the delegate of newly added surfaces and objects.
- [func captureSession(RoomCaptureSession, didChange: CapturedRoom)](./capturesession%28_,didchange%29.md)
  Notifies the delegate when the session changes the dimensions and the transform properties of surfaces and objects.
- [func captureSession(RoomCaptureSession, didUpdate: CapturedRoom)](./capturesession%28_,didupdate%29.md)
  Notifies the delegate when the session updates the scan results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcapturesessiondelegate/capturesession(_:didremove:))*