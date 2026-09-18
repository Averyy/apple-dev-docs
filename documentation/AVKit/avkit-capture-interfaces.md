# Capture interfaces

**Framework**: AVKit

Capture from hardware buttons and AirPods, present an audio input picker, and connect a nearby iPhone as a camera.

#### Overview

AVKit connects your capture app to the system features that surround capture. For example, people expect a camera app to work with the device the way the Camera app does. The volume button takes the photo, a click on AirPods starts a recording, and the microphone someone chose is the one that records audio.

These capture features are more integration than user interface. Your app keeps its own camera design and adds system behavior around it. Events arrive when someone presses a button, the system’s own picker appears when they choose an input, and a nearby iPhone becomes the camera when someone pairs it on Apple TV.

For information about building a camera app, see [`Capture setup`](https://developer.apple.com/documentation/avfoundation/capture-setup).

## Topics

### Capture events
- [class AVCaptureEventInteraction](avcaptureeventinteraction.md)
  An object that registers handlers to respond to capture events from system hardware buttons.
- [class AVCaptureEvent](avcaptureevent.md)
  An object that describes a user interaction with a system hardware button.
- [class AVCaptureEventSound](avcaptureeventsound.md)
  A sound object for a capture event.
### Camera facing direction
- [Choosing a camera by the direction it faces](choosing-a-camera-by-the-direction-it-faces.md)
  Find out which way each camera faces, and follow the change as someone opens and closes the device.
- [class AVCaptureDeviceDirectionCoordinator](avcapturedevicedirectioncoordinator.md)
  An object that tracks the direction each camera faces in relation to a view.
- [class AVCaptureDeviceDirectionMap](avcapturedevicedirectionmap.md)
  An object that groups the cameras a coordinator tracks by the direction they face.
- [class AVCaptureDeviceDescriptor](avcapturedevicedescriptor.md)
  An object that identifies a capture device and is safe to pass between actors.
### Audio input selection
- [class AVInputPickerInteraction](avinputpickerinteraction.md)
  An object that presents the system’s audio input picker so people can choose which microphone to use for recording audio.
### Camera access while multitasking
- [Accessing the camera while multitasking on iPad](accessing-the-camera-while-multitasking-on-ipad.md)
  Operate the camera in Split View, Slide Over, Picture in Picture, and Stage Manager modes.
### Continuity Camera
- [Supporting Continuity Camera in your tvOS app](supporting-continuity-camera-in-your-tvos-app.md)
  Capture high-quality photos, video, and audio in your Apple TV app by connecting an iPhone or iPad as a continuity device.
- [class AVContinuityDevicePickerViewController](avcontinuitydevicepickerviewcontroller.md)
  A view controller that provides an interface to a person so they can select and connect a continuity device to the system.
- [protocol AVContinuityDevicePickerViewControllerDelegate](avcontinuitydevicepickerviewcontrollerdelegate.md)
  An interface that responds to events from a continuity device picker view controller.
### Capture views
- [class AVCaptureView](avcaptureview.md)
  A view that displays standard user interface controls for capturing media data.
- [protocol AVCaptureViewDelegate](avcaptureviewdelegate.md)
  The protocol that defines the methods you can implement to respond to capture view events.

## See Also

- [Playback interfaces](avkit-playback-interfaces.md)
  Present video with the system player, complete with transport controls and Picture in Picture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avkit-capture-interfaces)*