# CMHeadphoneMotionManager

**Framework**: Core Motion  
**Kind**: class

An object that starts and manages headphone motion services.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 14.0+
- watchOS 7.0+

## Declaration

```swift
class CMHeadphoneMotionManager
```

## Mentions

- [Getting processed device-motion data](getting-processed-device-motion-data.md)

#### Overview

This class delivers headphone motion updates to your app. Use an instance of the manager to determine if the device supports motion, and to start and stop updates. Adopt the [`CMHeadphoneMotionManagerDelegate`](cmheadphonemotionmanagerdelegate.md) protocol to receive and respond to motion updates. Before using this class, check [`isDeviceMotionAvailable`](cmheadphonemotionmanager/isdevicemotionavailable.md) to make sure the feature is available.

> ❗ **Important**:  In iOS and macOS, include the [`NSMotionUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSMotionUsageDescription) key in your app’s `Info.plist` file. If this key is absent, the system crashes your app when you start device-motion updates.

##### Identify the Coordinate Axes

To interpret attitude data, you need to know the orientation of the device’s coordinate axes. The following illustration shows the positive x-axis, positive y-axis, and positive z-axis for motion-capable Apple headphones.

![An illustration showing AirPods Max and AirPods Pro with labels representing the positive x-axis, positive y-axis, and positive z-axis on each device.](https://docs-assets.developer.apple.com/published/4f7825123ffe36ae9788ba56f7f92bd7/media-4302074%402x.png)

## Topics

### Checking Availability
- [var isDeviceMotionAvailable: Bool](cmheadphonemotionmanager/isdevicemotionavailable.md)
  A Boolean value that indicates whether the current device supports the headphone motion manager.
- [var isDeviceMotionActive: Bool](cmheadphonemotionmanager/isdevicemotionactive.md)
  A Boolean value that indicates whether the headphone motion manager is active.
- [var isConnectionStatusActive: Bool](cmheadphonemotionmanager/isconnectionstatusactive.md)
- [class func authorizationStatus() -> CMAuthorizationStatus](cmheadphonemotionmanager/authorizationstatus.md)
  Returns the authorization status for monitoring headphone motion.
### Starting and Stopping Updates
- [func startDeviceMotionUpdates()](cmheadphonemotionmanager/startdevicemotionupdates.md)
  Starts device-motion updates.
- [func startDeviceMotionUpdates(to: OperationQueue, withHandler: CMHeadphoneMotionManager.DeviceMotionHandler)](cmheadphonemotionmanager/startdevicemotionupdates(to:withhandler:).md)
  Starts device-motion updates with a handler.
- [func startConnectionStatusUpdates()](cmheadphonemotionmanager/startconnectionstatusupdates.md)
- [func stopDeviceMotionUpdates()](cmheadphonemotionmanager/stopdevicemotionupdates.md)
  Stops device-motion updates.
- [func stopConnectionStatusUpdates()](cmheadphonemotionmanager/stopconnectionstatusupdates.md)
### Getting the Delegate
- [var delegate: (any CMHeadphoneMotionManagerDelegate)?](cmheadphonemotionmanager/delegate.md)
  The object that receives headphone motion manager events.
- [protocol CMHeadphoneMotionManagerDelegate](cmheadphonemotionmanagerdelegate.md)
  A set of methods that defines an interface for connecting and disconnecting headphones.
### Getting Device-Motion Information
- [var deviceMotion: CMDeviceMotion?](cmheadphonemotionmanager/devicemotion.md)
  The latest device-motion data.

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

- [Getting processed device-motion data](getting-processed-device-motion-data.md)
  Retrieve motion data that the system processed to remove environmental bias, such as the effects of gravity.
- [class CMDeviceMotion](cmdevicemotion.md)
  Encapsulated measurements of the attitude, rotation rate, and acceleration of a device.
- [class CMAttitude](cmattitude.md)
  The device’s orientation relative to a known frame of reference at a point in time.
- [struct CMAttitudeReferenceFrame](cmattitudereferenceframe.md)
  Constants that indicate the frame of reference for attitude-related motion data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager)*