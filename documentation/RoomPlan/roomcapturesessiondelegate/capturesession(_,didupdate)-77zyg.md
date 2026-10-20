# captureSession(_:didUpdate:)

**Framework**: RoomPlan  
**Kind**: method  
**Role**: Instance Method

Provides a default, blank implementation for when the session updates surfaces and objects during a scan.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
func captureSession(_ session: RoomCaptureSession, didUpdate room: CapturedRoom)
```

#### Discussion

The system calls this implementation if your app doesn’t implement [`captureSession(_:didUpdate:)`](./capturesession%28_,didupdate%29.md) .

## Parameters

- `session`: An object that manages the room-scanning process.
- `room`: A structure that contains the surfaces and objects that the framework updates during the scan.

## See Also

### Default implementations
- [func captureSession(RoomCaptureSession, didStartWith: RoomCaptureSession.Configuration)](./capturesession%28_,didstartwith%29-3c74n.md)
  Provides a default, blank implementation for when the session starts.
- [func captureSession(RoomCaptureSession, didRemove: CapturedRoom)](./capturesession%28_,didremove%29-9gs76.md)
  Provides a default, blank implementation for when the session removes surfaces and objects.
- [func captureSession(RoomCaptureSession, didChange: CapturedRoom)](./capturesession%28_,didchange%29-gv3t.md)
  Provides a default, blank implementation for when the capture session updates the dimensions and the transform properties during a scan.
- [func captureSession(RoomCaptureSession, didProvide: RoomCaptureSession.Instruction)](./capturesession%28_,didprovide%29-5hvhl.md)
  Provides a default, blank implementation for when the capture session provides a user instruction.
- [func captureSession(RoomCaptureSession, didEndWith: CapturedRoomData, error: (any Error)?)](./capturesession%28_,didendwith,error%29-5f0mc.md)
  Provides a default, blank implementation for when the capture session provides raw scan results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcapturesessiondelegate/capturesession(_:didupdate:)-77zyg)*