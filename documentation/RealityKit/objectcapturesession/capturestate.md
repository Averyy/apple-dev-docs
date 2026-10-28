# ObjectCaptureSession.CaptureState

**Framework**: RealityKit  
**Kind**: enum  
**Role**: Enumeration

State of the capture session.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
enum CaptureState
```

## Overview

A session starts in `.initializing` state and proceeds through the other states via use of function calls until it reaches an end state.  A session is over when the capture state is set to `.completed` or `.failed(Error)`.

## Topics

### Operators
- [static func == (ObjectCaptureSession.CaptureState, ObjectCaptureSession.CaptureState) -> Bool](./capturestate/eqeq%28_,_%29.md)
  Two states are defined equal if they have the same case.  Specifically, a `.failed(Error)` state will match any other failed state regardless of the actual error payload.
### Enumeration Cases
- [ObjectCaptureSession.CaptureState.capturing](./capturestate/capturing.md)
  Auto-capture is in progress.
- [ObjectCaptureSession.CaptureState.completed](./capturestate/completed.md)
  The session has saved its data and can now be safely torn down and the images folder used for reconstruction.
- [ObjectCaptureSession.CaptureState.detecting](./capturestate/detecting.md)
  The object selection box is being detected / manipulated and is not yet complete. A call to `startCapturing()` in this state will move the session to `.capturing` to begin capturing the object indicated within the currently specified bounding box.
- [ObjectCaptureSession.CaptureState.failed(_:)](./capturestate/failed%28_%29.md)
  There was an unrecoverable error and the session is now invalid and needs to be torn down.
- [ObjectCaptureSession.CaptureState.finishing](./capturestate/finishing.md)
  The session is saving outstanding data and finishing up.
- [ObjectCaptureSession.CaptureState.initializing](./capturestate/initializing.md)
  The session and camera feed are initializing.
- [ObjectCaptureSession.CaptureState.ready](./capturestate/ready.md)
  The session is ready to begin taking calls to capture.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Monitoring the session
- [ObjectCaptureSession.Error](./error.md)
  Errors associated with the top-level computation of this class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/capturestate)*