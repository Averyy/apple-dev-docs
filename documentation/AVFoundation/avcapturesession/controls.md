# controls

**Framework**: AVFoundation  
**Kind**: property

The controls that allow configuring the camera system from device hardware.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
var controls: [AVCaptureControl] { get }
```

#### Discussion

You modify the contents of this array by calling the [`addControl(_:)`](avcapturesession/addcontrol(_:).md) and [`removeControl(_:)`](avcapturesession/removecontrol(_:).md) methods.

## See Also

- [var supportsControls: Bool](avcapturesession/supportscontrols.md)
  A Boolean value that indicates whether a capture session supports controls.
- [var maxControlsCount: Int](avcapturesession/maxcontrolscount.md)
  The maximum number of controls a capture session supports.
- [func canAddControl(AVCaptureControl) -> Bool](avcapturesession/canaddcontrol(_:).md)
  Returns a Boolean value that indicates whether a capture session add the specified control.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/controls)*