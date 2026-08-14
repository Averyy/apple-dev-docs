# canAddControl(_:)

**Framework**: AVFoundation  
**Kind**: method

Returns a Boolean value that indicates whether a capture session add the specified control.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
func canAddControl(_ control: AVCaptureControl) -> Bool
```

## Mentions

- [Enhancing your app experience with the Camera Control](enhancing-your-app-experience-with-the-camera-control.md)

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the capture session can add the control; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Call this method to determine whether you can successfully add a control to a capture session using the [`addControl(_:)`](avcapturesession/addcontrol(_:).md) method. A capture session may not be able to add a control due to its current session configuration or if unsupported by the host platform.

## Parameters

- `control`: The capture control to add.

## See Also

- [var supportsControls: Bool](avcapturesession/supportscontrols.md)
  A Boolean value that indicates whether a capture session supports controls.
- [var maxControlsCount: Int](avcapturesession/maxcontrolscount.md)
  The maximum number of controls a capture session supports.
- [var controls: [AVCaptureControl]](avcapturesession/controls.md)
  The controls that allow configuring the camera system from device hardware.
- [func addControl(AVCaptureControl)](avcapturesession/addcontrol(_:).md)
  Adds a control to a capture session.
- [func removeControl(AVCaptureControl)](avcapturesession/removecontrol(_:).md)
  Removes a control from a capture session.
- [func setControlsDelegate((any AVCaptureSessionControlsDelegate)?, queue: dispatch_queue_t?)](avcapturesession/setcontrolsdelegate(_:queue:).md)
  Sets a delegate object for the system to call when it activates and presents controls.
- [protocol AVCaptureSessionControlsDelegate](avcapturesessioncontrolsdelegate.md)
  A protocol that defines the interface to respond to capture control activation and presentation events.
- [var controlsDelegate: (any AVCaptureSessionControlsDelegate)?](avcapturesession/controlsdelegate.md)
  A delegate object that observes changes to the state of capture controls.
- [var controlsDelegateCallbackQueue: dispatch_queue_t?](avcapturesession/controlsdelegatecallbackqueue.md)
  The dispatch queue on which the system calls controls delegate methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/canaddcontrol(_:))*