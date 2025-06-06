# setControlsDelegate(_:queue:)

**Framework**: AVFoundation  
**Kind**: method

Sets a delegate object for the system to call when it activates and presents controls.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
func setControlsDelegate(_ controlsDelegate: (any AVCaptureSessionControlsDelegate)?, queue controlsDelegateCallbackQueue: dispatch_queue_t?)
```

## Mentions

- [Enhancing your app experience with the Camera Control](enhancing-your-app-experience-with-the-camera-control.md)

#### Discussion

People interact with capture controls by performing specific gestures to enable their visibility. Specify a delegate to for the system to call when it presents and dismisses controls. The system calls the delegate’s methods on the specified callback queue.

## Parameters

- `controlsDelegate`: An object that adopts the controls delegate protocol.
- `controlsDelegateCallbackQueue`: This argument must not be   unless the   argument is also   otherwise, the system throws an  .

## See Also

- [var supportsControls: Bool](avcapturesession/supportscontrols.md)
  A Boolean value that indicates whether a capture session supports controls.
- [var maxControlsCount: Int](avcapturesession/maxcontrolscount.md)
  The maximum number of controls a capture session supports.
- [var controls: [AVCaptureControl]](avcapturesession/controls.md)
  The controls that allow configuring the camera system from device hardware.
- [func canAddControl(AVCaptureControl) -> Bool](avcapturesession/canaddcontrol(_:).md)
  Returns a Boolean value that indicates whether a capture session add the specified control.
- [func addControl(AVCaptureControl)](avcapturesession/addcontrol(_:).md)
  Adds a control to a capture session.
- [func removeControl(AVCaptureControl)](avcapturesession/removecontrol(_:).md)
  Removes a control from a capture session.
- [protocol AVCaptureSessionControlsDelegate](avcapturesessioncontrolsdelegate.md)
  A protocol that defines the interface to respond to capture control activation and presentation events.
- [var controlsDelegate: (any AVCaptureSessionControlsDelegate)?](avcapturesession/controlsdelegate.md)
  A delegate object that observes changes to the state of capture controls.
- [var controlsDelegateCallbackQueue: dispatch_queue_t?](avcapturesession/controlsdelegatecallbackqueue.md)
  The dispatch queue on which the system calls controls delegate methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/setcontrolsdelegate(_:queue:))*