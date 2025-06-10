# captureSession(_:didChange:)

**Framework**: RoomPlan  
**Kind**: method

Provides a default, blank implementation for when the capture session updates the dimensions and the transform properties during a scan.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS ?+

## Declaration

```swift
func captureSession(_ session: RoomCaptureSession, didChange room: CapturedRoom)
```

#### Discussion

The system calls this implementation if your app doesn’t implement [`captureSession(_:didChange:)`](roomcapturesessiondelegate/capturesession(_:didchange:).md).

## Parameters

- `session`: An object that manages the room-scanning process.
- `room`: A structure that contains the updated dimensions and transform properties.

## See Also

- [func captureSession(RoomCaptureSession, didStartWith: RoomCaptureSession.Configuration)](roomcapturesessiondelegate/capturesession(_:didstartwith:)-3c74n.md)
  Provides a default, blank implementation for when the session starts.
- [func captureSession(RoomCaptureSession, didUpdate: CapturedRoom)](roomcapturesessiondelegate/capturesession(_:didupdate:)-77zyg.md)
  Provides a default, blank implementation for when the session updates surfaces and objects during a scan.
- [func captureSession(RoomCaptureSession, didRemove: CapturedRoom)](roomcapturesessiondelegate/capturesession(_:didremove:)-9gs76.md)
  Provides a default, blank implementation for when the session removes surfaces and objects.
- [func captureSession(RoomCaptureSession, didProvide: RoomCaptureSession.Instruction)](roomcapturesessiondelegate/capturesession(_:didprovide:)-5hvhl.md)
  Provides a default, blank implementation for when the capture session provides a user instruction.
- [func captureSession(RoomCaptureSession, didEndWith: CapturedRoomData, error: (any Error)?)](roomcapturesessiondelegate/capturesession(_:didendwith:error:)-5f0mc.md)
  Provides a default, blank implementation for when the capture session provides raw scan results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcapturesessiondelegate/capturesession(_:didchange:)-gv3t)*