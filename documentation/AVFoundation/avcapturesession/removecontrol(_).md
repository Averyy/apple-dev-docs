# removeControl(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Removes a control from a capture session.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
func removeControl(_ control: AVCaptureControl)
```

```objc
- (void) removeControl:(AVCaptureControl *) control;
```

## Discussion

You may call this method while the session is running.

## Parameters

- `control`: The control to remove.

## See Also

### Configuring capture controls
- [var supportsControls: Bool](./supportscontrols.md)
  A Boolean value that indicates whether a capture session supports controls.
- [var maxControlsCount: Int](./maxcontrolscount.md)
  The maximum number of controls a capture session supports.
- [var controls: [AVCaptureControl]](./controls.md)
  The controls that allow configuring the camera system from device hardware.
- [func canAddControl(AVCaptureControl) -> Bool](./canaddcontrol%28_%29.md)
  Returns a Boolean value that indicates whether a capture session add the specified control.
- [func addControl(AVCaptureControl)](./addcontrol%28_%29.md)
  Adds a control to a capture session.
- [func setControlsDelegate((any AVCaptureSessionControlsDelegate)?, queue: dispatch_queue_t?)](./setcontrolsdelegate%28_,queue%29.md)
  Sets a delegate object for the system to call when it activates and presents controls.
- [protocol AVCaptureSessionControlsDelegate](../avcapturesessioncontrolsdelegate.md)
  A protocol that defines the interface to respond to capture control activation and presentation events.
- [var controlsDelegate: (any AVCaptureSessionControlsDelegate)?](./controlsdelegate.md)
  A delegate object that observes changes to the state of capture controls.
- [var controlsDelegateCallbackQueue: dispatch_queue_t?](./controlsdelegatecallbackqueue.md)
  The dispatch queue on which the system calls controls delegate methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/removecontrol(_:))*