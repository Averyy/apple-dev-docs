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

- [Requesting authorization to capture and save media](requesting-authorization-to-capture-and-save-media.md)
- [Setting Up a Capture Session](setting-up-a-capture-session.md)
- [Enhancing your app experience with the Camera Control](enhancing-your-app-experience-with-the-camera-control.md)
- [Choosing a Capture Device](choosing-a-capture-device.md)

#### Overview

Capture devices provide media data to capture session inputs that you connect to an [`AVCaptureSession`](avcapturesession.md). An individual device can provide one or more streams of media of a particular type.

You don’t create capture device instances directly. Instead, retrieve them using an instance of [`AVCaptureDevice.DiscoverySession`](avcapturedevice/discoverysession.md), or by calling the [`default(_:for:position:)`](avcapturedevice/default(_:for:position:).md) method.

A capture device provides several configuration options. Before attempting to configure device properties, such as its focus mode, exposure mode, and so on, you must first acquire a lock on the device by calling the [`lockForConfiguration()`](avcapturedevice/lockforconfiguration().md) method. You should also query the device’s capabilities to ensure that the new modes you intend to set are valid for the device. You can then set the properties and release the lock using the [`unlockForConfiguration()`](avcapturedevice/unlockforconfiguration().md) method. You may hold the lock if you want all settable device properties to remain unchanged. However, holding the device lock unnecessarily may degrade capture quality in other apps sharing the device and isn’t recommended.

## Topics

### Finding and Monitoring Devices
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
### Authorizing Device Access
- [class func requestAccess(for: AVMediaType, completionHandler: (Bool) -> Void)](avcapturedevice/requestaccess(for:completionhandler:).md)
  Requests the user’s permission to allow the app to capture media of a particular type.
- [class func authorizationStatus(for: AVMediaType) -> AVAuthorizationStatus](avcapturedevice/authorizationstatus(for:).md)
  Returns an authorization status that indicates whether the user grants the app permission to capture media of a particular type.
- [enum AVAuthorizationStatus](avauthorizationstatus.md)
  Constants that indicate the status of an app’s authorization to capture media.
### Identifying a Device
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
### Accessing Device State
- [var isConnected: Bool](avcapturedevice/isconnected.md)
  A Boolean value that indicates whether a device is currently connected to the system and available for use.
- [var isSuspended: Bool](avcapturedevice/issuspended.md)
  A Boolean value that indicates whether the device is in a suspended state.
- [var isInUseByAnotherApplication: Bool](avcapturedevice/isinusebyanotherapplication.md)
  A Boolean value that indicates whether another app is using the device.
### Inspecting Device Characteristics
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
### Monitoring Device Rotation
- [AVCaptureDevice.RotationCoordinator](avcapturedevice/rotationcoordinator.md)
  A class that monitors the physical orientation of a capture device and provides adjustment angles to keep images level, relative to gravity.
### Configuring Camera Hardware
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
- [White Balance](capture-device-white-balance.md)
  Configure the automatic white balance behavior of a camera, or manually control white balance settings.
- [Lighting](capture-device-lighting.md)
  Configure the device flash, torch, and low light settings.
- [Color](capture-device-color.md)
  Manage HDR and color space settings for a device.
- [Zoom](capture-device-zoom.md)
  Configure device zooming behavior and inspect hardware capabilities.
### Enabling Automatic Frame Rate
- [var isAutoVideoFrameRateEnabled: Bool](avcapturedevice/isautovideoframerateenabled.md)
  A Boolean value that indicates whether the capture device performs automatic video frame rate adjustments.
### Supporting Spatial Capture
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
### Supporting System Features
- [System Video Effects and Microphone Modes](system-video-effects-and-microphone-modes.md)
  Configure the state of system video effects like Center Stage, and inspect enhancements the system applies to microphone audio.
### Monitoring System Pressure
- [var systemPressureState: AVCaptureDevice.SystemPressureState](avcapturedevice/systempressurestate-swift.property.md)
  A value that indicates the capture device’s current system pressure state.
- [AVCaptureDevice.SystemPressureState](avcapturedevice/systempressurestate-swift.class.md)
  An object that provides information about OS and hardware status affecting capture system performance and availability.
- [let AVCaptureSessionInterruptionSystemPressureStateKey: String](avcapturesessioninterruptionsystempressurestatekey.md)
  A key to retrieve a state value that indicates the system pressure level and contributing factors that caused the interruption.
### Restricting Camera Switching
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
### Configuring macOS Features
- [macOS Capture Features](macos-capture-features.md)
  Control the transport behavior and input sources of capture hardware in macOS.
### Accessing Camera Extrinsics
- [class func extrinsicMatrix(from: AVCaptureDevice, to: AVCaptureDevice) -> Data?](avcapturedevice/extrinsicmatrix(from:to:).md)
  Returns the relative extrinsic matrix from one capture device to another.
### Determining Lens Stabilization
- [AVCaptureDevice.LensStabilizationStatus](avcapturedevice/lensstabilizationstatus.md)
  Constants that indicate the status of optical image stabilization hardware during a bracketed photo capture.

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

- [Choosing a Capture Device](choosing-a-capture-device.md)
  Select the front or back camera, or use advanced features like the TrueDepth camera or dual camera.
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