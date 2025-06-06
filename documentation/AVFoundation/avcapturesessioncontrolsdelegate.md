# AVCaptureSessionControlsDelegate

**Framework**: AVFoundation  
**Kind**: protocol

A protocol that defines the interface to respond to capture control activation and presentation events.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
protocol AVCaptureSessionControlsDelegate : NSObjectProtocol
```

## Mentions

- [Enhancing your app experience with the Camera Control](enhancing-your-app-experience-with-the-camera-control.md)

## Topics

### Responding to control events
- [func sessionControlsDidBecomeActive(AVCaptureSession)](avcapturesessioncontrolsdelegate/sessioncontrolsdidbecomeactive(_:).md)
  Tells the delegate when a capture session’s controls become active and available for interaction.
- [func sessionControlsWillEnterFullscreenAppearance(AVCaptureSession)](avcapturesessioncontrolsdelegate/sessioncontrolswillenterfullscreenappearance(_:).md)
  Tells the delegate when a capture session’s controls are about to enter a fullscreen appearance.
- [func sessionControlsWillExitFullscreenAppearance(AVCaptureSession)](avcapturesessioncontrolsdelegate/sessioncontrolswillexitfullscreenappearance(_:).md)
  Tells the delegate when a capture session’s controls are about to exit a fullscreen appearance.
- [func sessionControlsDidBecomeInactive(AVCaptureSession)](avcapturesessioncontrolsdelegate/sessioncontrolsdidbecomeinactive(_:).md)
  Tells the delegate when a capture session’s controls become inactive and unavailable for interaction.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

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
- [func setControlsDelegate((any AVCaptureSessionControlsDelegate)?, queue: dispatch_queue_t?)](avcapturesession/setcontrolsdelegate(_:queue:).md)
  Sets a delegate object for the system to call when it activates and presents controls.
- [var controlsDelegate: (any AVCaptureSessionControlsDelegate)?](avcapturesession/controlsdelegate.md)
  A delegate object that observes changes to the state of capture controls.
- [var controlsDelegateCallbackQueue: dispatch_queue_t?](avcapturesession/controlsdelegatecallbackqueue.md)
  The dispatch queue on which the system calls controls delegate methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesessioncontrolsdelegate)*