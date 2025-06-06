# RoomCaptureSessionDelegate

**Framework**: RoomPlan  
**Kind**: protocol

A specification of important events in the room-scanning process.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 16.0+

## Declaration

```swift
protocol RoomCaptureSessionDelegate : AnyObject
```

## Mentions

- [Scanning the rooms of a single structure](scanning-the-rooms-of-a-single-structure.md)

#### Overview

The room-capture session’s [`delegate`](roomcapturesession/delegate.md) property is of this type.

## Topics

### Beginning a session
- [func captureSession(RoomCaptureSession, didStartWith: RoomCaptureSession.Configuration)](roomcapturesessiondelegate/capturesession(_:didstartwith:).md)
  session starts with a configuration
### Updating a session
- [func captureSession(RoomCaptureSession, didAdd: CapturedRoom)](roomcapturesessiondelegate/capturesession(_:didadd:).md)
  session has newly added surfaces and objects
- [func captureSession(RoomCaptureSession, didRemove: CapturedRoom)](roomcapturesessiondelegate/capturesession(_:didremove:).md)
  session has recently removed surfaces and objects
- [func captureSession(RoomCaptureSession, didChange: CapturedRoom)](roomcapturesessiondelegate/capturesession(_:didchange:).md)
  Notifies the delegate when the session changes the dimensions and the transform properties of surfaces and objects.
- [func captureSession(RoomCaptureSession, didUpdate: CapturedRoom)](roomcapturesessiondelegate/capturesession(_:didupdate:).md)
  Notifies the delegate when the session updates the scan results.
### Coaching the user
- [func captureSession(RoomCaptureSession, didProvide: RoomCaptureSession.Instruction)](roomcapturesessiondelegate/capturesession(_:didprovide:).md)
  Notifies the delegate of an instruction to display to the user.
### Completing a session
- [func captureSession(RoomCaptureSession, didEndWith: CapturedRoomData, error: (any Error)?)](roomcapturesessiondelegate/capturesession(_:didendwith:error:).md)
  Notifies the delegate of completion with either scan results or an error.
### Default implementations
- [func captureSession(RoomCaptureSession, didStartWith: RoomCaptureSession.Configuration)](roomcapturesessiondelegate/capturesession(_:didstartwith:)-3c74n.md)
  Provides a default, blank implementation for when the session starts.
- [func captureSession(RoomCaptureSession, didUpdate: CapturedRoom)](roomcapturesessiondelegate/capturesession(_:didupdate:)-77zyg.md)
  Provides a default, blank implementation for when the session updates surfaces and objects during a scan.
- [func captureSession(RoomCaptureSession, didRemove: CapturedRoom)](roomcapturesessiondelegate/capturesession(_:didremove:)-9gs76.md)
  Provides a default, blank implementation for when the session removes surfaces and objects.
- [func captureSession(RoomCaptureSession, didChange: CapturedRoom)](roomcapturesessiondelegate/capturesession(_:didchange:)-gv3t.md)
  Provides a default, blank implementation for when the capture session updates the dimensions and the transform properties during a scan.
- [func captureSession(RoomCaptureSession, didProvide: RoomCaptureSession.Instruction)](roomcapturesessiondelegate/capturesession(_:didprovide:)-5hvhl.md)
  session has user guidance instructions
- [func captureSession(RoomCaptureSession, didEndWith: CapturedRoomData, error: (any Error)?)](roomcapturesessiondelegate/capturesession(_:didendwith:error:)-5f0mc.md)
  session ends with either CapturedRoom or error

## See Also

- [class RoomCaptureSession](roomcapturesession.md)
  An object that manages the room-scanning process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcapturesessiondelegate)*