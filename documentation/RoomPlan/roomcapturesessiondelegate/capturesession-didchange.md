# captureSession(_:didChange:)

**Framework**: RoomPlan  
**Kind**: method  
**Required**: Yes

Notifies the delegate when the session changes the dimensions and the transform properties of surfaces and objects.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 16.0+

## Declaration

```swift
func captureSession(_ session: RoomCaptureSession, didChange room: CapturedRoom)
```

## Parameters

- `session`: An object that manages the room-scanning process.
- `room`: A structure that contains only the surfaces/objects that experience recent changes.

## See Also

- [func captureSession(RoomCaptureSession, didAdd: CapturedRoom)](roomcapturesessiondelegate/capturesession(_:didadd:).md)
  session has newly added surfaces and objects
- [func captureSession(RoomCaptureSession, didRemove: CapturedRoom)](roomcapturesessiondelegate/capturesession(_:didremove:).md)
  session has recently removed surfaces and objects
- [func captureSession(RoomCaptureSession, didUpdate: CapturedRoom)](roomcapturesessiondelegate/capturesession(_:didupdate:).md)
  Notifies the delegate when the session updates the scan results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcapturesessiondelegate/capturesession(_:didchange:))*