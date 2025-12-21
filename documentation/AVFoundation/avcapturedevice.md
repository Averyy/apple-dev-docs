# AVCaptureDevice

**Framework**: AVFoundation  
**Kind**: class

An object that represents a hardware or virtual capture device like a camera or microphone.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class AVCaptureDevice
```

## Mentions

- [Choosing a capture device](choosing-a-capture-device.md)
- [Enhancing your app experience with the Camera Control](enhancing-your-app-experience-with-the-camera-control.md)
- [Requesting authorization to capture and save media](requesting-authorization-to-capture-and-save-media.md)
- [Setting up a capture session](setting-up-a-capture-session.md)

#### Overview

Capture devices provide media data to capture session inputs that you connect to an [`AVCaptureSession`](avcapturesession.md). An individual device can provide one or more streams of media of a particular type.

You don’t create capture device instances directly. Instead, retrieve them using an instance of [`AVCaptureDevice.DiscoverySession`](avcapturedevice/discoverysession.md), or by calling the [`default(_:for:position:)`](avcapturedevice/default(_:for:position:).md) method.

A capture device provides several configuration options. Before attempting to configure device properties, such as its focus mode, exposure mode, and so on, you must first acquire a lock on the device by calling the [`lockForConfiguration()`](avcapturedevice/lockforconfiguration().md) method. You should also query the device’s capabilities to ensure that the new modes you intend to set are valid for the device. You can then set the properties and release the lock using the [`unlockForConfiguration()`](avcapturedevice/unlockforconfiguration().md) method. You may hold the lock if you want all settable device properties to remain unchanged. However, holding the device lock unnecessarily may degrade capture quality in other apps sharing the device and isn’t recommended.

## Topics

### Finding and monitoring devices
- [AVCaptureDevice.DiscoverySession](avcapturedevice/discoverysession.md)
  An object that finds capture devices that match specific search criteria.
- [class func `default`(AVCaptureDevice.DeviceType, for: AVMediaType?, position: AVCaptureDevice.Position) -> AVCaptureDevice?](avcapturedevice/default(_:for:position:).md)
  Returns the default device for the specified device type, media type, and position.
- [class func `default`(for: AVMediaType) -> AVCaptureDevice?](avcapturedevice/default(for:).md)
  Returns the default device that captures the specified media type.
- [init?(uniqueID: String)](avcapturedevice/init(uniqueid:).md)
  Creates an object that represents a device with the specified identifier.
- [class let wasConnectedNotification: NSNotification.Name](avcapturedevice/wasconnectednotification.md)
  A notification the system posts when a new capture device becomes available.
- [class let wasDisconnectedNotification: NSNotification.Name](avcapturedevice/wasdisconnectednotification.md)
  A notification the system posts when an existing device becomes unavailable.
- [class func devices(for: AVMediaType) -> [AVCaptureDevice]](avcapturedevice/devices(for:).md)
  Returns devices capable of capturing media of the specified type.
- [class func devices() -> [AVCaptureDevice]](avcapturedevice/devices.md)
  Returns all available capture devices on the system.
### Authorizing device access
- [class func requestAccess(for: AVMediaType, completionHandler: (Bool) -> Void)](avcapturedevice/requestaccess(for:completionhandler:).md)
  Requests the user’s permission to allow the app to capture media of a particular type.
- [class func authorizationStatus(for: AVMediaType) -> AVAuthorizationStatus](avcapturedevice/authorizationstatus(for:).md)
  Returns an authorization status that indicates whether the user grants the app permission to capture media of a particular type.
- [enum AVAuthorizationStatus](avauthorizationstatus.md)
  Constants that indicate the status of an app’s authorization to capture media.
### Identifying a device
- [var uniqueID: String](avcapturedevice/uniqueid.md)
  An identifier that uniquely identifies the device.
- [var modelID: String](avcapturedevice/modelid.md)
  A model identifier for the device.
- [var localizedName: String](avcapturedevice/localizedname.md)
  A localized device name for display in the user interface.
- [var manufacturer: String](avcapturedevice/manufacturer.md)
  A human-readable string for the manufacturer of the device.
- [var deviceType: AVCaptureDevice.DeviceType](avcapturedevice/devicetype-swift.property.md)
  The type of device, such as a built-in microphone or wide-angle camera.
- [AVCaptureDevice.DeviceType](avcapturedevice/devicetype-swift.struct.md)
  A structure that defines the device types the framework supports.
- [var position: AVCaptureDevice.Position](avcapturedevice/position-swift.property.md)
  The physical position of the capture device hardware.
- [AVCaptureDevice.Position](avcapturedevice/position-swift.enum.md)
  Constants that indicate the physical position of a capture device.
### Accessing device state
- [var isConnected: Bool](avcapturedevice/isconnected.md)
  A Boolean value that indicates whether a device is currently connected to the system and available for use.
- [var isSuspended: Bool](avcapturedevice/issuspended.md)
  A Boolean value that indicates whether the device is in a suspended state.
- [var isInUseByAnotherApplication: Bool](avcapturedevice/isinusebyanotherapplication.md)
  A Boolean value that indicates whether another app is using the device.
### Inspecting device characteristics
- [var isVirtualDevice: Bool](avcapturedevice/isvirtualdevice.md)
  A Boolean value that indicates whether the device consists of two or more physical devices.
- [var constituentDevices: [AVCaptureDevice]](avcapturedevice/constituentdevices.md)
  An array of physical devices that make up a virtual device.
- [func hasMediaType(AVMediaType) -> Bool](avcapturedevice/hasmediatype(_:).md)
  Returns a Boolean value that indicates whether the device captures media of a particular type.
- [var transportType: Int32](avcapturedevice/transporttype.md)
  The transport type of the device.
- [func supportsSessionPreset(AVCaptureSession.Preset) -> Bool](avcapturedevice/supportssessionpreset(_:).md)
  Returns a Boolean value that indicates whether you can use the device with capture session configured with the specified preset.
### Monitoring device rotation
- [AVCaptureDevice.RotationCoordinator](avcapturedevice/rotationcoordinator.md)
  A class that monitors the physical orientation of a capture device and provides adjustment angles to keep images level, relative to gravity.
### Configuring camera hardware
- [func lockForConfiguration() throws](avcapturedevice/lockforconfiguration.md)
  Requests exclusive access to configure device hardware properties.
- [func unlockForConfiguration()](avcapturedevice/unlockforconfiguration.md)
  Releases exclusive control over device hardware properties.
- [var isSubjectAreaChangeMonitoringEnabled: Bool](avcapturedevice/issubjectareachangemonitoringenabled.md)
  A Boolean value that indicates whether the device monitors the subject area for changes.
- [class let subjectAreaDidChangeNotification: NSNotification.Name](avcapturedevice/subjectareadidchangenotification.md)
  A notification the system posts when a capture device detects a substantial change to the video subject area.
- [Formats](capture-device-formats.md)
  Configure capture formats and camera frame rates.
- [Focus](capture-device-focus.md)
  Configure the automatic focus behavior of a camera, or manually set its lens position.
- [Exposure](capture-device-exposure.md)
  Configure the automatic exposure behavior of a camera, or manually control its exposure settings.
- [White balance](capture-device-white-balance.md)
  Configure the automatic white balance behavior of a camera, or manually control white balance settings.
- [Lighting](capture-device-lighting.md)
  Configure the device flash, torch, and low light settings.
- [Color](capture-device-color.md)
  Manage HDR and color space settings for a device.
- [Zoom](capture-device-zoom.md)
  Configure device zooming behavior and inspect hardware capabilities.
### Configuring Cinematic video
- [func setCinematicVideoFixedFocus(at: CGPoint, focusMode: AVCaptureDevice.CinematicVideoFocusMode)](avcapturedevice/setcinematicvideofixedfocus(at:focusmode:).md)
  Fix focus at a distance.
- [func setCinematicVideoTrackingFocus(at: CGPoint, focusMode: AVCaptureDevice.CinematicVideoFocusMode)](avcapturedevice/setcinematicvideotrackingfocus(at:focusmode:).md)
  Focus on and start tracking an object if it can be detected at the region specified by the point.
- [func setCinematicVideoTrackingFocus(detectedObjectID: Int, focusMode: AVCaptureDevice.CinematicVideoFocusMode)](avcapturedevice/setcinematicvideotrackingfocus(detectedobjectid:focusmode:).md)
  Focus on and start tracking a detected object.
- [AVCaptureDevice.CinematicVideoFocusMode](avcapturedevice/cinematicvideofocusmode.md)
  Constants indicating the focus behavior when recording a Cinematic Video.
- [struct AVCaptureSceneMonitoringStatus](avcapturescenemonitoringstatus.md)
  An informative status about the scene observed by the device.
- [static let notEnoughLight: AVCaptureSceneMonitoringStatus](avcapturescenemonitoringstatus/notenoughlight.md)
  The light level of the current scene is insufficient for the current set of features to function optimally.
- [var cinematicVideoCaptureSceneMonitoringStatuses: Set<AVCaptureSceneMonitoringStatus>](avcapturedevice/cinematicvideocapturescenemonitoringstatuses.md)
  The current scene monitoring statuses related to Cinematic Video capture.
### Configuring smart framing
- [var smartFramingMonitor: AVCaptureSmartFramingMonitor?](avcapturedevice/smartframingmonitor.md)
  A monitor owned by the device that recommends an optimal framing based on the content in the scene.
- [class AVCaptureSmartFramingMonitor](avcapturesmartframingmonitor.md)
  An object associated with a capture device that monitors the scene and suggests an optimal framing.
- [class AVCaptureFraming](avcaptureframing.md)
  A framing, consisting of an aspect ratio and a zoom factor.
### Configuring dynamic aspect ratio
- [func setDynamicAspectRatio(AVCaptureDevice.AspectRatio, completionHandler: ((CMTime, (any Error)?) -> Void)?)](avcapturedevice/setdynamicaspectratio(_:completionhandler:).md)
  Updates the dynamic aspect ratio of the device.
- [AVCaptureDevice.AspectRatio](avcapturedevice/aspectratio.md)
  String constants describing the different video aspect ratios you can configure for a particular device.
- [var dynamicAspectRatio: AVCaptureDevice.AspectRatio?](avcapturedevice/dynamicaspectratio.md)
  A key-value observable property indicating the current aspect ratio for a device.
- [var dynamicDimensions: CMVideoDimensions](avcapturedevice/dynamicdimensions.md)
  A key-value observable property describing the output dimensions of the video buffer based on the device’s dynamic aspect ratio.
### Enabling automatic frame rate
- [var isAutoVideoFrameRateEnabled: Bool](avcapturedevice/isautovideoframerateenabled.md)
  A Boolean value that indicates whether the capture device performs automatic video frame rate adjustments.
### Supporting spatial capture
- [var spatialCaptureDiscomfortReasons: Set<AVSpatialCaptureDiscomfortReason>](avcapturedevice/spatialcapturediscomfortreasons.md)
  Reasons why current environmental conditions aren’t suitable to capturing spatial videos that are comfortable to view.
- [struct AVSpatialCaptureDiscomfortReason](avspatialcapturediscomfortreason.md)
  Constants that indicate the suitability of the current scene to create a comfortable viewing experience.
### Supporting Continuity Camera
- [class var systemPreferredCamera: AVCaptureDevice?](avcapturedevice/systempreferredcamera.md)
  A camera the system prefers to use for video and photo capture.
- [class var userPreferredCamera: AVCaptureDevice?](avcapturedevice/userpreferredcamera.md)
  A camera the user prefers to use for video and photo capture.
- [var isContinuityCamera: Bool](avcapturedevice/iscontinuitycamera.md)
  A Boolean value that indicates whether the device is a Continuity Camera.
- [var companionDeskViewCamera: AVCaptureDevice?](avcapturedevice/companiondeskviewcamera.md)
  A Desk View camera associated with a device.
### Supporting system features
- [System video effects and microphone modes](system-video-effects-and-microphone-modes.md)
  Configure the state of system video effects like Center Stage, and inspect enhancements the system applies to microphone audio.
### Monitoring system pressure
- [var systemPressureState: AVCaptureDevice.SystemPressureState](avcapturedevice/systempressurestate-swift.property.md)
  A value that indicates the capture device’s current system pressure state.
- [AVCaptureDevice.SystemPressureState](avcapturedevice/systempressurestate-swift.class.md)
  An object that provides information about OS and hardware status affecting capture system performance and availability.
- [let AVCaptureSessionInterruptionSystemPressureStateKey: String](avcapturesessioninterruptionsystempressurestatekey.md)
  A key to retrieve a state value that indicates the system pressure level and contributing factors that caused the interruption.
### Restricting camera switching
- [func setPrimaryConstituentDeviceSwitchingBehavior(AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior, restrictedSwitchingBehaviorConditions: AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions)](avcapturedevice/setprimaryconstituentdeviceswitchingbehavior(_:restrictedswitchingbehaviorconditions:).md)
  Sets the switching behavior of the primary constituent device.
- [var primaryConstituentDeviceSwitchingBehavior: AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior](avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.property.md)
  The switching behavior for the primary constituent device.
- [var primaryConstituentDeviceRestrictedSwitchingBehaviorConditions: AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions](avcapturedevice/primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.property.md)
  The conditions that restrict the primary constituent device’s switching behavior.
- [var activePrimaryConstituentDeviceSwitchingBehavior: AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior](avcapturedevice/activeprimaryconstituentdeviceswitchingbehavior.md)
  The switching behavior of the active constituent device.
- [var activePrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions: AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions](avcapturedevice/activeprimaryconstituentdevicerestrictedswitchingbehaviorconditions.md)
  The conditions that restrict camera switching behavior for the active primary constituent device.
- [var activePrimaryConstituent: AVCaptureDevice?](avcapturedevice/activeprimaryconstituent.md)
  A virtual device’s active primary constituent device.
- [AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior](avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.enum.md)
  Constants that control when to allow a virtual device to switch its active primary constituent device.
- [AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions](avcapturedevice/primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.struct.md)
  A structure that defines the conditions in which to restrict camera switching.
- [var supportedFallbackPrimaryConstituentDevices: [AVCaptureDevice]](avcapturedevice/supportedfallbackprimaryconstituentdevices.md)
  The constituent devices available to select as a fallback for a longer focal length primary constituent device.
- [var fallbackPrimaryConstituentDevices: [AVCaptureDevice]](avcapturedevice/fallbackprimaryconstituentdevices.md)
  The fallback devices to use when a constituent device with a longer focal length becomes limited by its light sensitivity or minimum focus distance.
### Configuring macOS features
- [macOS capture features](macos-capture-features.md)
  Control the transport behavior and input sources of capture hardware in macOS.
### Accessing camera extrinsics
- [class func extrinsicMatrix(from: AVCaptureDevice, to: AVCaptureDevice) -> Data?](avcapturedevice/extrinsicmatrix(from:to:).md)
  Returns the relative extrinsic matrix from one capture device to another.
### Accessing the focal length
- [var nominalFocalLengthIn35mmFilm: Float](avcapturedevice/nominalfocallengthin35mmfilm.md)
  The nominal 35mm equivalent focal length of the capture device’s lens.
### Determining lens stabilization
- [AVCaptureDevice.LensStabilizationStatus](avcapturedevice/lensstabilizationstatus.md)
  Constants that indicate the status of optical image stabilization hardware during a bracketed photo capture.
### Configuring lens smudge detection
- [var isCameraLensSmudgeDetectionEnabled: Bool](avcapturedevice/iscameralenssmudgedetectionenabled.md)
  Whether camera lens smudge detection is enabled.
- [func setCameraLensSmudgeDetectionEnabled(Bool, detectionInterval: CMTime)](avcapturedevice/setcameralenssmudgedetectionenabled(_:detectioninterval:).md)
  Specify whether to enable camera lens smudge detection, and the interval time between each run of detections.
- [var cameraLensSmudgeDetectionInterval: CMTime](avcapturedevice/cameralenssmudgedetectioninterval.md)
  The camera lens smudge detection interval.
- [var cameraLensSmudgeDetectionStatus: AVCaptureCameraLensSmudgeDetectionStatus](avcapturedevice/cameralenssmudgedetectionstatus.md)
  A value specifying the status of camera lens smudge detection.
- [enum AVCaptureCameraLensSmudgeDetectionStatus](avcapturecameralenssmudgedetectionstatus.md)
  Constants indicating the current camera lens smudge detection status.
### Synchronizing with external devices
- [var isFollowingExternalSyncDevice: Bool](avcapturedevice/isfollowingexternalsyncdevice.md)
  Whether the device is following an external sync device.
- [var minSupportedExternalSyncFrameDuration: CMTime](avcapturedevice/minsupportedexternalsyncframeduration.md)
  The minimum frame duration that can be passed as the `videoFrameDuration` when directing your device input to follow an external sync device.
- [var isVideoFrameDurationLocked: Bool](avcapturedevice/isvideoframedurationlocked.md)
  Whether the device’s video frame rate (expressed as a duration) is currently locked.
- [var minSupportedLockedVideoFrameDuration: CMTime](avcapturedevice/minsupportedlockedvideoframeduration.md)
  The maximum frame rate (expressed as a minimum duration) that can be set on an input associated with this device.
### Type Properties
- [class var isEdgeLightActive: Bool](avcapturedevice/isedgelightactive.md)
  A class property indicating whether the edge light UI is actively being shown on a screen.
- [class var isEdgeLightEnabled: Bool](avcapturedevice/isedgelightenabled.md)
  A class property indicating whether the Edge Light feature is currently enabled in Control Center.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Choosing a capture device](choosing-a-capture-device.md)
  Select the front or back camera, or use advanced features like the TrueDepth camera or dual camera.
- [Adopting smart framing in your camera app](adopting-smart-framing-in-your-camera-app.md)
  Capture the optimal shot by providing automatic framing recommendations.
- [class AVCaptureDeviceInput](avcapturedeviceinput.md)
  An object that provides media input from a capture device to a capture session.
- [class AVContinuityDevice](avcontinuitydevice.md)
  A class that represents a physical iOS device that’s nearby and can provide access to its cameras and microphones.
- [class AVExternalStorageDevice](avexternalstoragedevice.md)
  Represents a physical external storage device that stores media assets.
- [class AVExternalStorageDeviceDiscoverySession](avexternalstoragedevicediscoverysession.md)
  Informs your app when the external storage devices connect to and disconnect from the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice)*