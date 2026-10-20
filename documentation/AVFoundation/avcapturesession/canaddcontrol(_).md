# canAddControl(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) canAddControl:(AVCaptureControl *) control;
```

## Mentions

- [Enhancing your app experience with the Camera Control](../enhancing-your-app-experience-with-the-camera-control.md)

#### Return Value

[`true`](../../Swift/true.md) if the capture session can add the control; otherwise, [`false`](../../Swift/false.md).

#### Discussion

Call this method to determine whether you can successfully add a control to a capture session using the [`addControl(_:)`](./addcontrol%28_%29.md) method. A capture session may not be able to add a control due to its current session configuration or if unsupported by the host platform.

## Parameters

- `control`: The capture control to add.

## See Also

### Configuring capture controls
- [var supportsControls: Bool](./supportscontrols.md)
  A Boolean value that indicates whether a capture session supports controls.
- [var maxControlsCount: Int](./maxcontrolscount.md)
  The maximum number of controls a capture session supports.
- [var controls: [AVCaptureControl]](./controls.md)
  The controls that allow configuring the camera system from device hardware.
- [func addControl(AVCaptureControl)](./addcontrol%28_%29.md)
  Adds a control to a capture session.
- [func removeControl(AVCaptureControl)](./removecontrol%28_%29.md)
  Removes a control from a capture session.
- [func setControlsDelegate((any AVCaptureSessionControlsDelegate)?, queue: dispatch_queue_t?)](./setcontrolsdelegate%28_,queue%29.md)
  Sets a delegate object for the system to call when it activates and presents controls.
- [protocol AVCaptureSessionControlsDelegate](../avcapturesessioncontrolsdelegate.md)
  A protocol that defines the interface to respond to capture control activation and presentation events.
- [var controlsDelegate: (any AVCaptureSessionControlsDelegate)?](./controlsdelegate.md)
  A delegate object that observes changes to the state of capture controls.
- [var controlsDelegateCallbackQueue: dispatch_queue_t?](./controlsdelegatecallbackqueue.md)
  The dispatch queue on which the system calls controls delegate methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/canaddcontrol(_:))*