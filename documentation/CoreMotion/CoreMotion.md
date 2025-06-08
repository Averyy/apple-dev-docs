# Core Motion

**Framework**: Core Motion  
**Kind**: module

Process accelerometer, gyroscope, pedometer, and environment-related events.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 2.0+

#### Overview

Core Motion reports motion- and environment-related data from the available onboard hardware of iOS, iPadOS, watchOS, and visionOS devices. This hardware includes the device’s accelerometers and gyroscopes, and, when available, the pedometer, magnetometer, and barometer. Use this data in your app as input for user interactions, fitness tracking, health-related matters, and more. For example, a game might use accelerometer and gyroscope input to control onscreen game behavior.

The services of this framework provide access to motion data either as raw or processed values, and many services provide both types of values. Raw values reflect the unmodified data from the hardware, while processed values eliminate forms of bias that might adversely affect your usage of the data. For example, a processed accelerometer value reflects only the acceleration caused by the user and not the acceleration caused by gravity.

Not all services are available on all devices, and some services might be unavailable even on devices with the required hardware. For example, many Core Motion services are available to visionOS apps, but those services aren’t available to compatible iPad and iPhone apps running in visionOS. Before you try to use any motion-related services, check the availability of those services using a [`CMMotionManager`](cmmotionmanager.md) object.

> ❗ **Important**:  An iOS app must include usage description keys in its `Info.plist` file for the types of data it needs. If these keys aren’t present, the app crashes when you try to access the corresponding service. To access motion and fitness data, include [`NSMotionUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSMotionUsageDescription). To access the fall-detection service, include [`NSFallDetectionUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSFallDetectionUsageDescription).

## Topics

### Essentials
- [Core Motion updates](../Updates/CoreMotion.md)
  Learn about important changes to Core Motion.
- [class CMMotionManager](cmmotionmanager.md)
  The object for starting and managing motion services.
### Device motion
- [Getting processed device-motion data](getting-processed-device-motion-data.md)
  Retrieve motion data that the system processed to remove environmental bias, such as the effects of gravity.
- [class CMDeviceMotion](cmdevicemotion.md)
  Encapsulated measurements of the attitude, rotation rate, and acceleration of a device.
- [class CMAttitude](cmattitude.md)
  The device’s orientation relative to a known frame of reference at a point in time.
- [struct CMAttitudeReferenceFrame](cmattitudereferenceframe.md)
  Constants that indicate the frame of reference for attitude-related motion data.
- [class CMHeadphoneMotionManager](cmheadphonemotionmanager.md)
  An object that starts and manages headphone motion services.
### Accelerometers
- [Getting raw accelerometer events](getting-raw-accelerometer-events.md)
  Retrieve data from the onboard accelerometers.
- [class CMAccelerometerData](cmaccelerometerdata.md)
  A data sample from the device’s three accelerometers.
- [class CMRecordedAccelerometerData](cmrecordedaccelerometerdata.md)
  A single piece of accelerometer data that was recorded by the device.
- [class CMSensorRecorder](cmsensorrecorder.md)
  An object that gathers and retrieves accelerometer data from a device.
- [class CMSensorDataList](cmsensordatalist.md)
  A list of the accelerometer data recorded by the system.
### Gyroscopes
- [Getting raw gyroscope events](getting-raw-gyroscope-events.md)
  Retrieve data from the onboard gyroscopes.
- [class CMGyroData](cmgyrodata.md)
  A single measurement of the device’s rotation rate.
### Magnetometer
- [class CMMagnetometerData](cmmagnetometerdata.md)
  Measurements of the Earth’s magnetic field relative to the device.
### Altitude data
- [class CMAltimeter](cmaltimeter.md)
  An object that initiates the delivery of altitude-related changes.
- [class CMAbsoluteAltitudeData](cmabsolutealtitudedata.md)
  Data that records a change in absolute altitude.
- [class CMAltitudeData](cmaltitudedata.md)
  Data for a recorded change in altitude.
### Ambient pressure
- [class CMRecordedPressureData](cmrecordedpressuredata.md)
  A recorded measurement of pressure data.
- [class CMAmbientPressureData](cmambientpressuredata.md)
  A measurement of the ambient pressure and temperature.
### Water submersion
- [Accessing submersion data](accessing-submersion-data.md)
  Use a water-submersion manager to receive water pressure, temperature, and depth data on Apple Watch Ultra.
- [class CMWaterSubmersionManager](cmwatersubmersionmanager.md)
  An object for managing the collection of pressure and temperature data during submersion.
- [protocol CMWaterSubmersionManagerDelegate](cmwatersubmersionmanagerdelegate.md)
  A delegate that receives updates about ambient pressure, water pressure, water temperature, and submersion events.
- [class CMWaterSubmersionEvent](cmwatersubmersionevent.md)
  An event indicating that the device’s submersion state has changed.
- [class CMWaterSubmersionMeasurement](cmwatersubmersionmeasurement.md)
  An update that contains data about the pressure and depth.
- [class CMWaterTemperature](cmwatertemperature.md)
  An update that contains data about the water temperature.
### Activity
- [class CMMotionActivityManager](cmmotionactivitymanager.md)
  An object that manages access to the motion data stored by the device.
- [class CMHeadphoneActivityManager](cmheadphoneactivitymanager.md)
  An object that starts and manages headphone activity services.
- [class CMMotionActivity](cmmotionactivity.md)
  The data for a single motion update event.
- [Getting motion-activity data from headphones](getting-motion-activity-data-from-headphones.md)
  Configure your app to listen for motion-activity changes from headphones.
### Pedometer and fitness
- [class CMPedometer](cmpedometer.md)
  An object for fetching the system-generated live walking data.
- [class CMPedometerData](cmpedometerdata.md)
  Information about the distance traveled by a user on foot.
- [class CMPedometerEvent](cmpedometerevent.md)
  A change in the user’s pedestrian activity.
- [class CMStepCounter](cmstepcounter.md)
  The number of steps the user has taken with the device.
- [class CMOdometerData](cmodometerdata.md)
  A class that represents odometer data for workouts.
- [class CMHighFrequencyHeartRateData](cmhighfrequencyheartratedata.md)
  A class that represents heart rate data collected at 1 Hz.
### Movement disorder
- [Getting movement disorder symptom data](getting-movement-disorder-symptom-data.md)
  Retrieve data from the Apple Watch’s movement disorder manager.
- [Adhering to the movement disorder data collection requirements](adhering-to-the-movement-disorder-data-collection-requirements.md)
  Ensure that your users understand and have control over the data your app collects.
- [Movement disorder algorithm changelog](movement-disorder-algorithm-changelog.md)
  A chronological log of notable changes to the movement disorder algorithm.
- [class CMMovementDisorderManager](cmmovementdisordermanager.md)
  A manager for recording and querying movement disorder data.
- [class CMTremorResult](cmtremorresult.md)
  A result object that contains data about the presence and strength of tremors during a one-minute interval.
- [class CMDyskineticSymptomResult](cmdyskineticsymptomresult.md)
  A result object that contains data about the likely presence of dyskinetic symptoms during a one-minute interval.
### Fall detection
- [class CMFallDetectionManager](cmfalldetectionmanager.md)
  An object for managing fall detection events.
- [protocol CMFallDetectionDelegate](cmfalldetectiondelegate.md)
  A delegate that receives information about fall detection events and authorization status changes.
- [class CMFallDetectionEvent](cmfalldetectionevent.md)
  An object that contains data about a fall detection event.
- [NSFallDetectionUsageDescription](../BundleResources/Information-Property-List/NSFallDetectionUsageDescription.md)
  A message to the user that explains the app’s request for permission to access fall detection event data.
### Historical data
- [class CMBatchedSensorManager](cmbatchedsensormanager.md)
### Common data
- [class CMLogItem](cmlogitem.md)
  The base class for all motion-related data objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/CoreMotion)*