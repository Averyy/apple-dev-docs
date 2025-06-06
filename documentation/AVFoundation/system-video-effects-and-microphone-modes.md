# System Video Effects and Microphone Modes

**Framework**: AVFoundation

Configure the state of system video effects like Center Stage, and inspect enhancements the system applies to microphone audio.

## Topics

### Performing Reaction Effects
- [class var reactionEffectsEnabled: Bool](avcapturedevice/reactioneffectsenabled.md)
  A Boolean value that indicates whether the app supports performing reaction effects.
- [var canPerformReactionEffects: Bool](avcapturedevice/canperformreactioneffects.md)
  A Boolean value that indicates whether you can perform reaction effects on a capture device.
- [var availableReactionTypes: Set<AVCaptureReactionType>](avcapturedevice/availablereactiontypes.md)
  A set of reactions types that a device supports performing.
- [class var reactionEffectGesturesEnabled: Bool](avcapturedevice/reactioneffectgesturesenabled.md)
  A Boolean value that indicates whether gesture detection triggers reaction effects on the video stream.
- [func performEffect(for: AVCaptureReactionType)](avcapturedevice/performeffect(for:).md)
  Performs the specified reaction type on the video stream.
- [var reactionEffectsInProgress: [AVCaptureReactionEffectState]](avcapturedevice/reactioneffectsinprogress.md)
  An array of reaction effects that the device is currently performing, sorted by timestamp.
- [class AVCaptureReactionEffectState](avcapturereactioneffectstate.md)
  An object that reports the state of a reaction effect performed on a capture device.
### Configuring Center Stage
- [var isCenterStageActive: Bool](avcapturedevice/iscenterstageactive.md)
  A Boolean value that indicates whether Center Stage is active on a device.
- [class var isCenterStageEnabled: Bool](avcapturedevice/iscenterstageenabled.md)
  A Boolean value that indicates whether a user or an app enabled Center Stage on a device.
- [var centerStageRectOfInterest: CGRect](avcapturedevice/centerstagerectofinterest.md)
  The effective region within the output pixel buffer to perform Center Stage framing.
- [class var centerStageControlMode: AVCaptureDevice.CenterStageControlMode](avcapturedevice/centerstagecontrolmode-swift.type.property.md)
  A value that indicates the current mode of Center Stage control.
- [AVCaptureDevice.CenterStageControlMode](avcapturedevice/centerstagecontrolmode-swift.enum.md)
  Constants that indicate the current Center Stage control mode.
### Configuring Studio Light
- [var isStudioLightActive: Bool](avcapturedevice/isstudiolightactive.md)
  A Boolean value that indicates whether Studio Light is active on a device.
- [class var isStudioLightEnabled: Bool](avcapturedevice/isstudiolightenabled.md)
  A Boolean value that indicates whether a user enabled Studio Light on a device.
### Inspecting the Portrait Effect Settings
- [var isPortraitEffectActive: Bool](avcapturedevice/isportraiteffectactive.md)
  A Boolean value that indicates whether the Portrait video effect is active on a device.
- [class var isPortraitEffectEnabled: Bool](avcapturedevice/isportraiteffectenabled.md)
  A Boolean value that indicates whether the user enabled the Portrait video effect in Control Center.
### Inspecting the Microphone Mode
- [class var activeMicrophoneMode: AVCaptureDevice.MicrophoneMode](avcapturedevice/activemicrophonemode.md)
  The device’s active microphone mode.
- [class var preferredMicrophoneMode: AVCaptureDevice.MicrophoneMode](avcapturedevice/preferredmicrophonemode.md)
  The microphone mode that the user selects in Control Center.
- [AVCaptureDevice.MicrophoneMode](avcapturedevice/microphonemode.md)
  Constants that define the available microphone modes.
### Presenting the Configuration User Interface
- [class func showSystemUserInterface(AVCaptureDevice.SystemUserInterface)](avcapturedevice/showsystemuserinterface(_:).md)
  Displays the system’s user interface to configure video effects or microphone modes.
- [AVCaptureDevice.SystemUserInterface](avcapturedevice/systemuserinterface.md)
  Constants that describe the capture device configuration user interfaces.
### Configuring Background Replacement
- [var isBackgroundReplacementActive: Bool](avcapturedevice/isbackgroundreplacementactive.md)
  A Boolean value that indicates whether Background Replacement is currently active on a capture device.
- [class var isBackgroundReplacementEnabled: Bool](avcapturedevice/isbackgroundreplacementenabled.md)
  A class property that indicates whether a person enables the Background Replacement feature for this app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/system-video-effects-and-microphone-modes)*