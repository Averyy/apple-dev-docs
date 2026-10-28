# captureSession(_:didEndWith:error:)

**Framework**: RoomPlan  
**Kind**: method  
**Role**: Instance Method

Provides a default, blank implementation for when the capture session provides raw scan results.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
func captureSession(_ session: RoomCaptureSession, didEndWith data: CapturedRoomData, error: (any Error)?)
```

## Mentions

- [Scanning the rooms of a single structure](../scanning-the-rooms-of-a-single-structure.md)

## Discussion

The system calls this implementation if your app doesn’t implement [`captureSession(_:didEndWith:error:)`](./capturesession%28_,didendwith,error%29.md).

## Parameters

- `session`: An object that manages the room-scanning process.
- `data`: A data object that contains the raw scan results.
- `error`: An object that describes the problem when an error occurs; otherwise, `nil`.

## See Also

### Default implementations
- [func captureSession(RoomCaptureSession, didStartWith: RoomCaptureSession.Configuration)](./capturesession%28_,didstartwith%29-3c74n.md)
  Provides a default, blank implementation for when the session starts.
- [func captureSession(RoomCaptureSession, didUpdate: CapturedRoom)](./capturesession%28_,didupdate%29-77zyg.md)
  Provides a default, blank implementation for when the session updates surfaces and objects during a scan.
- [func captureSession(RoomCaptureSession, didRemove: CapturedRoom)](./capturesession%28_,didremove%29-9gs76.md)
  Provides a default, blank implementation for when the session removes surfaces and objects.
- [func captureSession(RoomCaptureSession, didChange: CapturedRoom)](./capturesession%28_,didchange%29-gv3t.md)
  Provides a default, blank implementation for when the capture session updates the dimensions and the transform properties during a scan.
- [func captureSession(RoomCaptureSession, didProvide: RoomCaptureSession.Instruction)](./capturesession%28_,didprovide%29-5hvhl.md)
  Provides a default, blank implementation for when the capture session provides a user instruction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcapturesessiondelegate/capturesession(_:didendwith:error:)-5f0mc)*