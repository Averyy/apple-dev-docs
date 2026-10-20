# RoomCaptureSessionDelegate

**Framework**: RoomPlan  
**Kind**: protocol  
**Role**: Protocol

A specification of important events in the room-scanning process.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
protocol RoomCaptureSessionDelegate : AnyObject
```

## Mentions

- [Scanning the rooms of a single structure](./scanning-the-rooms-of-a-single-structure.md)

#### Overview

The room-capture session’s [`delegate`](./roomcapturesession/delegate.md) property is of this type.

## Topics

### Beginning a session
- [func captureSession(RoomCaptureSession, didStartWith: RoomCaptureSession.Configuration)](./roomcapturesessiondelegate/capturesession%28_,didstartwith%29.md)
  Notifies the delegate when the session starts.
### Updating a session
- [func captureSession(RoomCaptureSession, didAdd: CapturedRoom)](./roomcapturesessiondelegate/capturesession%28_,didadd%29.md)
  Notifies the delegate of newly added surfaces and objects.
- [func captureSession(RoomCaptureSession, didRemove: CapturedRoom)](./roomcapturesessiondelegate/capturesession%28_,didremove%29.md)
  Notifies the delegate when the session removes surfaces and objects.
- [func captureSession(RoomCaptureSession, didChange: CapturedRoom)](./roomcapturesessiondelegate/capturesession%28_,didchange%29.md)
  Notifies the delegate when the session changes the dimensions and the transform properties of surfaces and objects.
- [func captureSession(RoomCaptureSession, didUpdate: CapturedRoom)](./roomcapturesessiondelegate/capturesession%28_,didupdate%29.md)
  Notifies the delegate when the session updates the scan results.
### Coaching the user
- [func captureSession(RoomCaptureSession, didProvide: RoomCaptureSession.Instruction)](./roomcapturesessiondelegate/capturesession%28_,didprovide%29.md)
  Notifies the delegate of an instruction to display to the user.
### Completing a session
- [func captureSession(RoomCaptureSession, didEndWith: CapturedRoomData, error: (any Error)?)](./roomcapturesessiondelegate/capturesession%28_,didendwith,error%29.md)
  Notifies the delegate of completion with either scan results or an error.
### Default implementations
- [func captureSession(RoomCaptureSession, didStartWith: RoomCaptureSession.Configuration)](./roomcapturesessiondelegate/capturesession%28_,didstartwith%29-3c74n.md)
  Provides a default, blank implementation for when the session starts.
- [func captureSession(RoomCaptureSession, didUpdate: CapturedRoom)](./roomcapturesessiondelegate/capturesession%28_,didupdate%29-77zyg.md)
  Provides a default, blank implementation for when the session updates surfaces and objects during a scan.
- [func captureSession(RoomCaptureSession, didRemove: CapturedRoom)](./roomcapturesessiondelegate/capturesession%28_,didremove%29-9gs76.md)
  Provides a default, blank implementation for when the session removes surfaces and objects.
- [func captureSession(RoomCaptureSession, didChange: CapturedRoom)](./roomcapturesessiondelegate/capturesession%28_,didchange%29-gv3t.md)
  Provides a default, blank implementation for when the capture session updates the dimensions and the transform properties during a scan.
- [func captureSession(RoomCaptureSession, didProvide: RoomCaptureSession.Instruction)](./roomcapturesessiondelegate/capturesession%28_,didprovide%29-5hvhl.md)
  Provides a default, blank implementation for when the capture session provides a user instruction.
- [func captureSession(RoomCaptureSession, didEndWith: CapturedRoomData, error: (any Error)?)](./roomcapturesessiondelegate/capturesession%28_,didendwith,error%29-5f0mc.md)
  Provides a default, blank implementation for when the capture session provides raw scan results.

## See Also

### Scanning Protocol
- [class RoomCaptureSession](./roomcapturesession.md)
  An object that manages the room-scanning process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcapturesessiondelegate)*