# RoomCaptureSession

**Framework**: RoomPlan  
**Kind**: class

An object that manages the room-scanning process.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS ?+

## Declaration

```swift
class RoomCaptureSession
```

## Mentions

- [Scanning the rooms of a single structure](scanning-the-rooms-of-a-single-structure.md)

#### Overview

This class scans a room on the app’s behalf and provides the necessary callbacks for you to display your own UI.

As an alternate approach to the UX of the framework-provided view ([`RoomCaptureView`](roomcaptureview.md)), this class is appropriate for apps that intend to display their own view and scanning experience. You can start your own AR experience by accessing this class’s [`arSession`](roomcapturesession/arsession.md), or by providing your own [`ARSession`](https://developer.apple.com/documentation/ARKit/ARSession) instance to the [`init(arSession:)`](roomcapturesession/init(arsession:).md) initializer.

To produce a 3D asset of the user’s environment, this class:

- Utilizes an ARKit session ([`arSession`](roomcapturesession/arsession.md)) that enables the device’s LiDAR Scanner to capture the environment’s physical layout.
- Provides instructions that you display to the user to coach them on moving the device appropriately to collect the necessary data.

## Topics

### Creating a session
- [init(arSession: ARSession?)](roomcapturesession/init(arsession:).md)
### Ensuring device support
- [static var isSupported: Bool](roomcapturesession/issupported.md)
  A Boolean value that indicates whether the user’s device supports the framework.
### Controlling a session
- [func run(configuration: RoomCaptureSession.Configuration)](roomcapturesession/run(configuration:).md)
  Starts a room-capture session with the specified configuration.
- [RoomCaptureSession.Configuration](roomcapturesession/configuration.md)
  Settings that configure the room-scanning process.
- [func stop()](roomcapturesession/stop.md)
  Stops the room-capture session.
- [func stop(pauseARSession: Bool)](roomcapturesession/stop(pausearsession:).md)
  Stops the room-capture session and indicates whether the app pauses the underlying AR session.
### Responding to events
- [var delegate: (any RoomCaptureSessionDelegate)?](roomcapturesession/delegate.md)
  An object that observes important events in the room-scanning process.
- [RoomCaptureSession.CaptureError](roomcapturesession/captureerror.md)
  Errors that can occur during a room-capture session.
### Accessing the AR session
- [var arSession: ARSession](roomcapturesession/arsession.md)
  An object that manages an ARKit session.
### Displaying user instructions
- [RoomCaptureSession.Instruction](roomcapturesession/instruction.md)
  Instructions that the framework recommends the app display to the user.
### Initializers
- [init()](roomcapturesession/init.md)
  Creates a room-capture session with the given AR session.

## See Also

- [protocol RoomCaptureSessionDelegate](roomcapturesessiondelegate.md)
  A specification of important events in the room-scanning process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcapturesession)*