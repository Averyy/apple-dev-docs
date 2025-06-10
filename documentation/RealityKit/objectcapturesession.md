# ObjectCaptureSession

**Framework**: RealityKit  
**Kind**: class

A session object that monitors and controls image capture for photogrammetry.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
@MainActor
class ObjectCaptureSession
```

#### Overview

An [`ObjectCaptureSession`](objectcapturesession.md) is used together with an [`ObjectCaptureView`](objectcaptureview.md) to present a view that assists in capturing images of an object for reconstruction of a 3D model by using a [`PhotogrammetrySession`](photogrammetrysession.md).

A capture session contains functions for starting and advancing the capture session through a state machine that controls the image capture process. Your app can also observe several properties of the capture session to determine the current state of the capture process.

Once a session enters the `.completed` state, your app can transfer the images to a Mac or use them locally on the iOS device for use in object reconstruction using [`PhotogrammetrySession`](photogrammetrysession.md). Model reconstruction is a separate phase which this session does not directly monitor or control.

## Topics

### Creating a session
- [init()](objectcapturesession/init.md)
  Creates a new object capture session.
### Checking availability
- [static var isSupported: Bool](objectcapturesession/issupported.md)
  A Boolean that indicates whether the current device supports object capture sessions.
### Configuring a session
- [var feedback: Set<ObjectCaptureSession.Feedback>](objectcapturesession/feedback-swift.property.md)
  The current set of active `Feedback` states.
- [ObjectCaptureSession.Feedback](objectcapturesession/feedback-swift.enum.md)
  Provides information about possible problems with the capture session.
- [var isPaused: Bool](objectcapturesession/ispaused.md)
  A Boolean value that indicates if the capture session is paused.
- [var state: ObjectCaptureSession.CaptureState](objectcapturesession/state.md)
  The current state of the capture session.
- [var cameraTracking: ObjectCaptureSession.Tracking](objectcapturesession/cameratracking.md)
  The current state of ARKit camera tracking.
- [ObjectCaptureSession.Tracking](objectcapturesession/tracking.md)
  A data structure that describes the current tracking state for the camera.
### Monitoring the session
- [ObjectCaptureSession.CaptureState](objectcapturesession/capturestate.md)
  State of the capture session.
- [ObjectCaptureSession.Error](objectcapturesession/error.md)
  Errors associated with the top-level computation of this class.
### Controlling the session
- [func cancel()](objectcapturesession/cancel.md)
  Requests that the capture session be canceled.
- [func finish()](objectcapturesession/finish.md)
  Requests that the capture session be stopped and all data saved.
- [func pause()](objectcapturesession/pause.md)
  Pauses the automatic capture and other resource-intense algorithms.
- [func requestImageCapture()](objectcapturesession/requestimagecapture.md)
  Requests a manual image capture.
- [func resume()](objectcapturesession/resume.md)
  Resumes object tracking algorithms after [`pause()`](objectcapturesession/pause().md) is called.
- [func startCapturing()](objectcapturesession/startcapturing.md)
  Begins taking images for object capture.
### Structures
- [ObjectCaptureSession.Configuration](objectcapturesession/configuration-swift.struct.md)
  The configuration options for the session which are passed into the `start(imagesDirectory:configuration:)` call.
- [ObjectCaptureSession.Updates](objectcapturesession/updates.md)
  Used to provide an `AsyncSequence` of change events for the observable properties.
### Instance Properties
- [var cameraTrackingUpdates: ObjectCaptureSession.Updates<ObjectCaptureSession.Tracking>](objectcapturesession/cameratrackingupdates.md)
  The `Updates` `AsyncSequence` for the `cameraTracking` property.
- [var canRequestImageCapture: Bool](objectcapturesession/canrequestimagecapture.md)
  Will be `true` only when a call to [`requestImageCapture()`](objectcapturesession/requestimagecapture().md) is expected to be successful. It will be `false` when not in the `.capturing` state or if the session is too busy to currently process a new request. There is a period of time after requesting an image capture where this property will be `false` and a new call to [`requestImageCapture()`](objectcapturesession/requestimagecapture().md)  will not produce a new image.
- [var canRequestImageCaptureUpdates: ObjectCaptureSession.Updates<Bool>](objectcapturesession/canrequestimagecaptureupdates.md)
  The `Updates` `AsyncSequence` for the `canRequestImagecapture` property.
- [var configuration: ObjectCaptureSession.Configuration](objectcapturesession/configuration-swift.property.md)
  The read-only `Configuration` used to start the capture session.  The configuration can be set by passing it to the `start()` call and it remains immutable after the session is started successfully.
- [var feedbackUpdates: ObjectCaptureSession.Updates<Set<ObjectCaptureSession.Feedback>>](objectcapturesession/feedbackupdates.md)
  The `Updates` `AsyncSequence` for the `feedback` property.
- [var isAutoCaptureEnabled: Bool](objectcapturesession/isautocaptureenabled.md)
  Enables/disables auto-capture system.  If disabled, only manually triggered shots are taken.
- [var isPausedUpdates: ObjectCaptureSession.Updates<Bool>](objectcapturesession/ispausedupdates.md)
  The `Updates` `AsyncSequence` for the `isPaused` property.
- [var maximumNumberOfInputImages: Int](objectcapturesession/maximumnumberofinputimages.md)
  The maximum number of images that can be used for on-device reconstruction.
- [var numberOfShotsTaken: Int](objectcapturesession/numberofshotstaken.md)
  The number of shots taken in the entire capture session so far, including both automatic capture and manual capture.
- [var numberOfShotsTakenUpdates: ObjectCaptureSession.Updates<Int>](objectcapturesession/numberofshotstakenupdates.md)
  The `Updates` `AsyncSequence` for the `numberOfShotsTaken` property.
- [var shouldPlayHaptics: Bool](objectcapturesession/shouldplayhaptics.md)
  Enables/disables haptics on devices that support it.
- [var stateUpdates: ObjectCaptureSession.Updates<ObjectCaptureSession.CaptureState>](objectcapturesession/stateupdates.md)
  The `Updates` `AsyncSequence` for the `state` property.
- [var userCompletedScanPass: Bool](objectcapturesession/usercompletedscanpass.md)
  This property starts out `false` at the start of a capture and will switch to `true` when the user has moved the device in a full circular scan pass around the bounding box of the target object and captured enough data to fill completely the capture dial.
- [var userCompletedScanPassUpdates: ObjectCaptureSession.Updates<Bool>](objectcapturesession/usercompletedscanpassupdates.md)
  The `Updates` `AsyncSequence` for the `userCompletedScanPass` property.
### Instance Methods
- [func beginNewScanPass()](objectcapturesession/beginnewscanpass.md)
  Resets the state of the capture dial such that the user will need to perform another complete scan pass to fill it and generate a new event in the published property [`userCompletedScanPass`](objectcapturesession/usercompletedscanpass.md).
- [func beginNewScanPassAfterFlip()](objectcapturesession/beginnewscanpassafterflip.md)
  Starts the capturing of a new side of the object, to be called after the object is scanned one side and flipped.
- [func resetDetection() -> Bool](objectcapturesession/resetdetection.md)
  Moves the session state from `.detecting` back to `.ready` to reset the bounding box and prepare to select a new one with a new call to `startDetecting()`.
- [func start(imagesDirectory: URL, configuration: ObjectCaptureSession.Configuration)](objectcapturesession/start(imagesdirectory:configuration:).md)
  Starts the session with the provided output image directory and optional checkpoint directory.
- [func startDetecting() -> Bool](objectcapturesession/startdetecting.md)
  Requests that the session should start detecting the object in the center of the camera.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Observable](../Observation/Observable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Capturing photographs for RealityKit Object Capture](capturing-photographs-for-realitykit-object-capture.md)
  Take high-quality images of objects to generate 3D models.
- [Creating 3D objects from photographs](creating-3d-objects-from-photographs.md)
  Construct virtual objects to use in your AR experiences.
- [Scanning objects using Object Capture](scanning-objects-using-object-capture.md)
  Implement a full scanning workflow for capturing objects on iOS devices.
- [Building an object reconstruction app](building-an-object-reconstruction-app.md)
  Reconstruct objects from user-selected input images by using photogrammetry.
- [Creating a Photogrammetry Command-Line App](creating_a_photogrammetry_command-line_app.md)
  Generate 3D objects from images using RealityKit Object Capture.
- [Using object capture assets in RealityKit](using_object_capture_assets_in_realitykit.md)
  Create a chess game using RealityKit and assets created using Object Capture.
- [class PhotogrammetrySession](photogrammetrysession.md)
  Manages the creation of a 3D model from a set of images.
- [struct PhotogrammetrySample](photogrammetrysample.md)
  An object that represents one image and its corresponding metadata.
- [struct ObjectCaptureView](objectcaptureview.md)
  A view that guides a user through capturing images for object capture.
- [struct ObjectCapturePointCloudView](objectcapturepointcloudview.md)
  Renders the current state of the point cloud from an object capture session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession)*