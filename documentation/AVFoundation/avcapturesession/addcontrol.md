# addControl(_:)

**Framework**: AVFoundation  
**Kind**: method

Adds a control to a capture session.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
func addControl(_ control: AVCaptureControl)
```

## Mentions

- [Enhancing your app experience with the Camera Control](enhancing-your-app-experience-with-the-camera-control.md)

#### Discussion

A capture session may not be able to add a control due to configuration reasons or limits of the host platform. Before calling this method, determine whether you can successfully add a control by calling the capture session’s [`canAddControl(_:)`](avcapturesession/canaddcontrol(_:).md) method.

You may call this method while the session is running.

> ❗ **Important**:  For a control to become active, you must set a [`AVCaptureSessionControlsDelegate`](avcapturesessioncontrolsdelegate.md) on the session.

 For a control to become active, you must set a [`AVCaptureSessionControlsDelegate`](avcapturesessioncontrolsdelegate.md) on the session.

## Parameters

- `control`: The capture control to add.

## See Also

- [var supportsControls: Bool](avcapturesession/supportscontrols.md)
  A Boolean value that indicates whether a capture session supports controls.
- [var maxControlsCount: Int](avcapturesession/maxcontrolscount.md)
  The maximum number of controls a capture session supports.
- [var controls: [AVCaptureControl]](avcapturesession/controls.md)
  The controls that allow configuring the camera system from device hardware.
- [func canAddControl(AVCaptureControl) -> Bool](avcapturesession/canaddcontrol(_:).md)
  Returns a Boolean value that indicates whether a capture session add the specified control.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/addcontrol(_:))*