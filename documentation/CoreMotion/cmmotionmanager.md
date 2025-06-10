# CMMotionManager

**Framework**: Core Motion  
**Kind**: class

The object for starting and managing motion services.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class CMMotionManager
```

## Mentions

- [Getting raw gyroscope events](getting-raw-gyroscope-events.md)
- [Getting raw accelerometer events](getting-raw-accelerometer-events.md)
- [Getting processed device-motion data](getting-processed-device-motion-data.md)

#### Overview

Use a [`CMMotionManager`](cmmotionmanager.md) object to start the services that report movement detected by the device’s onboard sensors. Use this object to receive four types of motion data:

- , indicating the instantaneous acceleration of the device in three dimensional space.
- , indicating the instantaneous rotation around the device’s three primary axes.
- , indicating the device’s orientation relative to Earth’s magnetic field.
- , indicating key motion-related attributes such as the device’s user-initiated acceleration, its attitude, rotation rates, orientation relative to calibrated magnetic fields, and orientation relative to gravity. Core Motion’s sensor fusion algorithms provide this data.

The processed device-motion data gives the device’s attitude, rotation rate, calibrated magnetic fields, the direction of gravity, and the amount of acceleration the user contributes to the device.

> ❗ **Important**:  Create only one [`CMMotionManager`](cmmotionmanager.md) object for your app. Multiple instances of this class can affect the rate at which the system receives data from the accelerometer and gyroscope.

You can receive live sensor data at a specified update interval, or you can let the sensors collect data and store it for retrieval later. With both of these approaches,  call the appropriate stop method ([`stopAccelerometerUpdates()`](cmmotionmanager/stopaccelerometerupdates().md), [`stopGyroUpdates()`](cmmotionmanager/stopgyroupdates().md), [`stopMagnetometerUpdates()`](cmmotionmanager/stopmagnetometerupdates().md), and [`stopDeviceMotionUpdates()`](cmmotionmanager/stopdevicemotionupdates().md)) when you no longer need the data.

##### Receive Regular Motion Updates

To receive motion data at specific intervals, the app calls a start method that takes an operation queue (instance of [`OperationQueue`](https://developer.apple.com/documentation/Foundation/OperationQueue)) and a block handler of a specific type for processing those updates.  The motion data is passed into the block handler. The frequency of updates is determined by the value of an interval property.

-  Set the [`accelerometerUpdateInterval`](cmmotionmanager/accelerometerupdateinterval.md) property to specify an update interval. Call  the [`startAccelerometerUpdates(to:withHandler:)`](cmmotionmanager/startaccelerometerupdates(to:withhandler:).md) method, passing in a block of type [`CMAccelerometerHandler`](cmaccelerometerhandler.md). Accelerometer data is passed into the block as [`CMAccelerometerData`](cmaccelerometerdata.md) objects.
-  Set the [`gyroUpdateInterval`](cmmotionmanager/gyroupdateinterval.md) property to specify an update interval. Call  the [`startGyroUpdates(to:withHandler:)`](cmmotionmanager/startgyroupdates(to:withhandler:).md) method, passing in a block of type [`CMGyroHandler`](cmgyrohandler.md). Rotation-rate data is passed into the block as [`CMGyroData`](cmgyrodata.md) objects.
-  Set the [`magnetometerUpdateInterval`](cmmotionmanager/magnetometerupdateinterval.md) property to specify an update interval. Call the [`startMagnetometerUpdates(to:withHandler:)`](cmmotionmanager/startmagnetometerupdates(to:withhandler:).md) method, passing a block of type [`CMMagnetometerHandler`](cmmagnetometerhandler.md). Magnetic-field data is passed into the block as [`CMMagnetometerData`](cmmagnetometerdata.md) objects.
-  Set the [`deviceMotionUpdateInterval`](cmmotionmanager/devicemotionupdateinterval.md) property to specify an update interval. Call the [`startDeviceMotionUpdates(using:)`](cmmotionmanager/startdevicemotionupdates(using:).md)or [`startDeviceMotionUpdates(using:to:withHandler:)`](cmmotionmanager/startdevicemotionupdates(using:to:withhandler:).md) or [`startDeviceMotionUpdates(to:withHandler:)`](cmmotionmanager/startdevicemotionupdates(to:withhandler:).md) method, passing in a block of type [`CMDeviceMotionHandler`](cmdevicemotionhandler.md). With the former method, you can specify a reference frame to be used for the attitude estimates. Rotation-rate data is passed into the block as [`CMDeviceMotion`](cmdevicemotion.md) objects.

##### Sample Motion Data Periodically

To sample motion data periodically, start a motion service using a method that takes no parameters and periodically access the properties of the [`CMMotionManager`](cmmotionmanager.md). This approach is the recommended approach for apps such as games. Handling accelerometer data in a block introduces additional overhead, and most game apps are only interested in the latest sample of motion data when they render a frame.

-  Call [`startAccelerometerUpdates()`](cmmotionmanager/startaccelerometerupdates().md) to begin updates and periodically access [`CMAccelerometerData`](cmaccelerometerdata.md) objects by reading the [`accelerometerData`](cmmotionmanager/accelerometerdata.md) property.
-  Call [`startGyroUpdates()`](cmmotionmanager/startgyroupdates().md) to begin updates and periodically access [`CMGyroData`](cmgyrodata.md) objects by reading the [`gyroData`](cmmotionmanager/gyrodata.md) property.
-  Call [`startMagnetometerUpdates()`](cmmotionmanager/startmagnetometerupdates().md) to begin updates and periodically access [`CMMagnetometerData`](cmmagnetometerdata.md) objects by reading the [`magnetometerData`](cmmotionmanager/magnetometerdata.md) property.
-  Call the [`startDeviceMotionUpdates(using:)`](cmmotionmanager/startdevicemotionupdates(using:).md) or [`startDeviceMotionUpdates()`](cmmotionmanager/startdevicemotionupdates().md) method to begin updates and periodically access [`CMDeviceMotion`](cmdevicemotion.md) objects by reading the [`deviceMotion`](cmmotionmanager/devicemotion.md) property. The [`startDeviceMotionUpdates(using:)`](cmmotionmanager/startdevicemotionupdates(using:).md) method lets you specify a reference frame for the attitude estimates.

##### Determine Hardware Availability and State

If a hardware feature (for example, a gyroscope) is not available on a device, calling a start method related to that feature has no effect. You can find out whether a hardware feature is available or active by checking the appropriate property; for example, for gyroscope data, you can check the value of the [`isGyroAvailable`](cmmotionmanager/isgyroavailable.md) or [`isGyroActive`](cmmotionmanager/isgyroactive.md) properties.

##### Identify the Coordinate Axes of the Device

To interpret accelerometer, gyroscope, or attitude information, you need to know the orientation of the device’s coordinate axes. The following illustration shows the positive x-axis, positive y-axis, and positive z-axis for motion-capable Apple devices.

![An illustration showing iPhone, iPad, Apple Watch, and Apple Vision Pro with labels representing the positive x-axis, positive y-axis, and positive z-axis on each device.](https://docs-assets.developer.apple.com/published/b702f8aa95f1359d3b1b7a05b575569b/media-4302073%402x.png)

## Topics

### Determining the Availability of Services
- [var isDeviceMotionAvailable: Bool](cmmotionmanager/isdevicemotionavailable.md)
  A Boolean value that indicates whether the device-motion service is available on the device.
- [var isAccelerometerAvailable: Bool](cmmotionmanager/isaccelerometeravailable.md)
  A Boolean value that indicates whether an accelerometer is available on the device.
- [var isGyroAvailable: Bool](cmmotionmanager/isgyroavailable.md)
  A Boolean value that indicates whether a gyroscope is available on the device.
- [var isMagnetometerAvailable: Bool](cmmotionmanager/ismagnetometeravailable.md)
  A Boolean value that indicates whether a magnetometer is available on the device.
### Determining Which Services Are Active
- [var isDeviceMotionActive: Bool](cmmotionmanager/isdevicemotionactive.md)
  A Boolean value that determines whether the app is receiving updates from the device-motion service.
- [var isAccelerometerActive: Bool](cmmotionmanager/isaccelerometeractive.md)
  A Boolean value that indicates whether accelerometer updates are currently happening.
- [var isGyroActive: Bool](cmmotionmanager/isgyroactive.md)
  A Boolean value that determines whether gyroscope updates are currently happening.
- [var isMagnetometerActive: Bool](cmmotionmanager/ismagnetometeractive.md)
  A Boolean value that determines whether magnetometer updates are currently happening.
### Managing Device Motion Updates
- [var showsDeviceMovementDisplay: Bool](cmmotionmanager/showsdevicemovementdisplay.md)
  Controls whether the device-movement display is shown.
- [var deviceMotionUpdateInterval: TimeInterval](cmmotionmanager/devicemotionupdateinterval.md)
  The interval, in seconds, for providing device-motion updates to the block handler.
- [func startDeviceMotionUpdates(using: CMAttitudeReferenceFrame, to: OperationQueue, withHandler: CMDeviceMotionHandler)](cmmotionmanager/startdevicemotionupdates(using:to:withhandler:).md)
  Starts device-motion updates on an operation queue and using a specified reference frame and block handler.
- [func startDeviceMotionUpdates(to: OperationQueue, withHandler: CMDeviceMotionHandler)](cmmotionmanager/startdevicemotionupdates(to:withhandler:).md)
  Starts device-motion updates on an operation queue and using a specified block handler.
- [func startDeviceMotionUpdates(using: CMAttitudeReferenceFrame)](cmmotionmanager/startdevicemotionupdates(using:).md)
  Starts device-motion updates using a reference frame but without a block handler.
- [func startDeviceMotionUpdates()](cmmotionmanager/startdevicemotionupdates.md)
  Starts device-motion updates without a block handler.
- [func stopDeviceMotionUpdates()](cmmotionmanager/stopdevicemotionupdates.md)
  Stops device-motion updates.
- [var deviceMotion: CMDeviceMotion?](cmmotionmanager/devicemotion.md)
  The latest sample of device-motion data.
- [typealias CMDeviceMotionHandler](cmdevicemotionhandler.md)
  The type of block callback for handling device-motion data.
### Managing Accelerometer Updates
- [var accelerometerUpdateInterval: TimeInterval](cmmotionmanager/accelerometerupdateinterval.md)
  The interval, in seconds, for providing accelerometer updates to the block handler.
- [func startAccelerometerUpdates(to: OperationQueue, withHandler: CMAccelerometerHandler)](cmmotionmanager/startaccelerometerupdates(to:withhandler:).md)
  Starts accelerometer updates on an operation queue and with a specified handler.
- [func startAccelerometerUpdates()](cmmotionmanager/startaccelerometerupdates.md)
  Starts accelerometer updates without a handler.
- [func stopAccelerometerUpdates()](cmmotionmanager/stopaccelerometerupdates.md)
  Stops accelerometer updates.
- [var accelerometerData: CMAccelerometerData?](cmmotionmanager/accelerometerdata.md)
  The latest sample of accelerometer data.
- [typealias CMAccelerometerHandler](cmaccelerometerhandler.md)
  The type of block callback for handling accelerometer data.
### Managing Gyroscope Updates
- [var gyroUpdateInterval: TimeInterval](cmmotionmanager/gyroupdateinterval.md)
  The interval, in seconds, for providing gyroscope updates to the block handler.
- [func startGyroUpdates(to: OperationQueue, withHandler: CMGyroHandler)](cmmotionmanager/startgyroupdates(to:withhandler:).md)
  Starts gyroscope updates on an operation queue and with a specified handler.
- [func startGyroUpdates()](cmmotionmanager/startgyroupdates.md)
  Starts gyroscope updates without a handler.
- [func stopGyroUpdates()](cmmotionmanager/stopgyroupdates.md)
  Stops gyroscope updates.
- [var gyroData: CMGyroData?](cmmotionmanager/gyrodata.md)
  The latest sample of gyroscope data.
- [typealias CMGyroHandler](cmgyrohandler.md)
  The type of block callback for handling gyroscope data.
### Managing Magnetometer Updates
- [var magnetometerUpdateInterval: TimeInterval](cmmotionmanager/magnetometerupdateinterval.md)
  The interval, in seconds, at which the system delivers magnetometer data to the block handler.
- [func startMagnetometerUpdates(to: OperationQueue, withHandler: CMMagnetometerHandler)](cmmotionmanager/startmagnetometerupdates(to:withhandler:).md)
  Starts magnetometer updates on an operation queue and with a specified handler.
- [func startMagnetometerUpdates()](cmmotionmanager/startmagnetometerupdates.md)
  Starts magnetometer updates without a block handler.
- [func stopMagnetometerUpdates()](cmmotionmanager/stopmagnetometerupdates.md)
  Stops magnetometer updates.
- [var magnetometerData: CMMagnetometerData?](cmmotionmanager/magnetometerdata.md)
  The latest sample of magnetometer data.
- [typealias CMMagnetometerHandler](cmmagnetometerhandler.md)
  The type of block callback for handling magnetometer data.
### Accessing Attitude Reference Frames
- [var attitudeReferenceFrame: CMAttitudeReferenceFrame](cmmotionmanager/attitudereferenceframe.md)
  Returns either the reference frame currently being used or the default attitude reference frame.
- [class func availableAttitudeReferenceFrames() -> CMAttitudeReferenceFrame](cmmotionmanager/availableattitudereferenceframes.md)
  Returns a bitmask of the available reference frames for reporting the attitude of the current device.
### Understanding Errors
- [let CMErrorDomain: String](cmerrordomain.md)
  The error domain for Core Motion.
- [struct CMError](cmerror.md)
  Defines motion errors.

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

- [Core Motion updates](../Updates/CoreMotion.md)
  Learn about important changes to Core Motion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager)*