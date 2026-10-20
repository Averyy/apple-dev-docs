# controls

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) NSArray<__kindof AVCaptureControl *> * controls;
```

#### Discussion

You modify the contents of this array by calling the [`addControl(_:)`](./addcontrol%28_%29.md) and [`removeControl(_:)`](./removecontrol%28_%29.md) methods.

## See Also

### Configuring capture controls
- [var supportsControls: Bool](./supportscontrols.md)
  A Boolean value that indicates whether a capture session supports controls.
- [var maxControlsCount: Int](./maxcontrolscount.md)
  The maximum number of controls a capture session supports.
- [func canAddControl(AVCaptureControl) -> Bool](./canaddcontrol%28_%29.md)
  Returns a Boolean value that indicates whether a capture session add the specified control.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/controls)*