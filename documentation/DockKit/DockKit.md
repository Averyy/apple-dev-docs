# DockKit

**Framework**: DockKit  
**Kind**: module  
**Role**: Framework

Interact with accessories that track subjects on camera as they move around.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

#### Overview

DockKit interfaces with DockKit-compatible motorized stands known as dock accessories to track the location of objects that appear in video frames. It determines how to best position the iPhone camera to frame and track objects, with improved person tracking using combined body and face tracking for human subjects. This feature, known as *system tracking*, automatically starts as soon as a person docks iPhone onto a compatible motorized stand and launches the Camera app. For example, system tracking is useful for content creators who want the camera to follow them while they move around their space, or instructors on a video call who are walking around a classroom.

![iPhone mounted in landscape orientation on a dock accessory with its back facing outward. A cocentric circle near the camera indicates that it is active.](https://developer.apple.com/tutorials/images/com.apple.DockKit/dock@2x.png)

![iPhone mounted in landscape orientation on a dock accessory with its back facing outward. An arc around the base of the dock accessory indicates horizontal movement. An arc around the body of iPhone indicates up and down movement.](https://developer.apple.com/tutorials/images/com.apple.DockKit/move@2x.png)

![iPhone mounted in landscape orientation on a dock accessory with the back of the iPhone aimed at a person in a video frame. The person in the frame is in midair, in the process of jumping.](https://developer.apple.com/tutorials/images/com.apple.DockKit/track@2x.png)

You can disable system tracking and implement your own tracking behavior by using [`DockAccessoryManager`](./dockaccessorymanager.md) and [`DockAccessory`](./dockaccessory.md). Implement your own tracking behavior to follow a location of a custom object such as a pet, or a pair of hands performing a task. DockKit accessories integrate with [`AVCaptureSession`](../AVFoundation/avcapturesession.md) so apps with camera permissions work seamlessly together.

## Topics

### Controlling the dock accessory
- [Controlling a DockKit accessory using your camera app](./controlling-a-dockkit-accessory-using-your-camera-app.md)
  Follow subjects in real time using an iPhone that you mount on a DockKit accessory.
- [class DockAccessoryManager](./dockaccessorymanager.md)
  Observe the state of dock accessories and enable or disable system tracking.
- [class DockAccessory](./dockaccessory.md)
  Obtain accessory information and control tracking behavior.
- [enum DockKitError](./dockkiterror.md)
  A list of errors that DockKit sends.
### Customizing tracking behavior
- [Modify rotation and positioning programmatically](./modify-rotation-and-positioning-behavior-programmatically.md)
  Perform custom control of the dock accessory.
- [Track custom objects in a frame](./track-custom-objects-in-a-frame.md)
  Use your machine learning model to focus on a specific subject.


---

*[View on Apple Developer](https://developer.apple.com/documentation/DockKit)*