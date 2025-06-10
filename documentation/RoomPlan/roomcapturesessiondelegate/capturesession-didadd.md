# captureSession(_:didAdd:)

**Framework**: RoomPlan  
**Kind**: method  
**Required**: Yes

Notifies the delegate of newly added surfaces and objects.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS ?+

## Declaration

```swift
func captureSession(_ session: RoomCaptureSession, didAdd room: CapturedRoom)
```

## Parameters

- `session`: An object that manages the room-scanning process.
- `room`: A structure that contains the newest surfaces and objects that the framework identifies during the scan.

## See Also

- [func captureSession(RoomCaptureSession, didRemove: CapturedRoom)](roomcapturesessiondelegate/capturesession(_:didremove:).md)
  Notifies the delegate when the session removes surfaces and objects.
- [func captureSession(RoomCaptureSession, didChange: CapturedRoom)](roomcapturesessiondelegate/capturesession(_:didchange:).md)
  Notifies the delegate when the session changes the dimensions and the transform properties of surfaces and objects.
- [func captureSession(RoomCaptureSession, didUpdate: CapturedRoom)](roomcapturesessiondelegate/capturesession(_:didupdate:).md)
  Notifies the delegate when the session updates the scan results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcapturesessiondelegate/capturesession(_:didadd:))*