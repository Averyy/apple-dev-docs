# captureSession(_:didUpdate:)

**Framework**: RoomPlan  
**Kind**: method

Provides a default, blank implementation for when the session updates surfaces and objects during a scan.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 16.0+

## Declaration

```swift
func captureSession(_ session: RoomCaptureSession, didUpdate room: CapturedRoom)
```

#### Discussion

The system calls this implementation if your app doesn’t implement [`captureSession(_:didUpdate:)`](roomcapturesessiondelegate/capturesession(_:didupdate:).md) .

## Parameters

- `session`: An object that manages the room-scanning process.
- `room`: A structure that contains the surfaces and objects that the framework updates during the scan.

## See Also

- [func captureSession(RoomCaptureSession, didStartWith: RoomCaptureSession.Configuration)](roomcapturesessiondelegate/capturesession(_:didstartwith:)-3c74n.md)
  Provides a default, blank implementation for when the session starts.
- [func captureSession(RoomCaptureSession, didRemove: CapturedRoom)](roomcapturesessiondelegate/capturesession(_:didremove:)-9gs76.md)
  Provides a default, blank implementation for when the session removes surfaces and objects.
- [func captureSession(RoomCaptureSession, didChange: CapturedRoom)](roomcapturesessiondelegate/capturesession(_:didchange:)-gv3t.md)
  Provides a default, blank implementation for when the capture session updates the dimensions and the transform properties during a scan.
- [func captureSession(RoomCaptureSession, didProvide: RoomCaptureSession.Instruction)](roomcapturesessiondelegate/capturesession(_:didprovide:)-5hvhl.md)
  session has user guidance instructions
- [func captureSession(RoomCaptureSession, didEndWith: CapturedRoomData, error: (any Error)?)](roomcapturesessiondelegate/capturesession(_:didendwith:error:)-5f0mc.md)
  session ends with either CapturedRoom or error


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcapturesessiondelegate/capturesession(_:didupdate:)-77zyg)*