# SensorKit

**Framework**: Sensorkit  
**Kind**: module

Retrieve data and derived metrics from sensors on an iPhone, or paired Apple Watch.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

#### Overview

As the system gathers information using various sensors on a device, SensorKit enables an app to access select raw data, or metrics that the system processes from a sensor, such as:

- Steps information
- Accelerometer or rotation-rate data
- The configuration of a watch on the user’s wrist
- Ambient light in the physical environment
- Details about a user’s routine commute or travel

See [`SRSensor`](srsensor.md) for the complete list.

> **Note**:  This framework ignores calls from Mac apps that you build with Mac Catalyst, and from compatible iPad and iPhone apps running in visionOS.

## Topics

### Essentials
- [SensorKit updates](../Updates/SensorKit.md)
  Learn about important changes to SensorKit.
### Setup
- [Configuring your project for sensor reading](configuring-your-project-for-sensor-reading.md)
  Add metadata to your app to attain system and user permission to access sensor data.
- [class SRSensorReader](srsensorreader.md)
  An object that establishes user authorization and records data for a particular sensor.
### Authorization
- [com.apple.developer.sensorkit.reader.allow](../BundleResources/Entitlements/com.apple.developer.sensorkit.reader.allow.md)
  The necessary entitlement to access sensor data that’s required by your app’s preapproved research study.
### Querying data
- [class SRFetchRequest](srfetchrequest.md)
  An object that defines the criteria for a sample query.
- [class SRFetchResult](srfetchresult.md)
  Recorded data that a sensor reader fetches.
### Interpreting data
- [class SRAmbientLightSample](srambientlightsample.md)
  The amount of ambient light in the user’s environment.
- [class SRDeviceUsageReport](srdeviceusagereport.md)
  The frequency and relative duration that the user uses their device, particular Apple apps, or websites.
- [class SRKeyboardMetrics](srkeyboardmetrics.md)
  The configuration of a device’s keyboard and its usage patterns.
- [class SRMediaEvent](srmediaevent.md)
  A user interaction with a media object, such as an image or a video.
- [class SRMessagesUsageReport](srmessagesusagereport.md)
  An object that describes the user’s Messages app activity over a period of time.
- [class SRPhoneUsageReport](srphoneusagereport.md)
  An object that describes the user’s phone activity over a period of time.
- [class SRVisit](srvisit.md)
  The user’s progress in their daily travel routine.
- [class SRWristDetection](srwristdetection.md)
  The configuration of a watch on the wearer’s wrist.
### Deleting samples
- [class SRDeletionRecord](srdeletionrecord.md)
  An object that describes the reason the framework deletes samples.
### Analyzing speech
- [class SRSpeechMetrics](srspeechmetrics.md)
  An object that represents metrics about a range of speech.
- [class SRSpeechExpression](srspeechexpression.md)
  An object that represents the metrics and voice analytics for a range of speech.
### Analyzing faces
- [class SRFaceMetrics](srfacemetrics.md)
  An object that represents metrics about the user’s face.
- [var SR_ARKIT_SUPPORTED: Int32](sr_arkit_supported.md)
  A flag that indicates whether the ARKit framework is available in the SDK for the SensorKit framework.
### Recording wrist temperatures
- [class SRWristTemperatureSession](srwristtemperaturesession.md)
  An object that represents wrist temperatures that a device records during a period of time.
- [class SRWristTemperature](srwristtemperature.md)
  The temperature of the user’s wrist while the user sleeps.
### Recording ectrocardiogram data
- [class SRElectrocardiogramSample](srelectrocardiogramsample.md)
  The sample electrocardiogram sensor data.
### Recording photoplethysmogram data
- [class SRPhotoplethysmogramSample](srphotoplethysmogramsample.md)
  The sample photoplethysmogram (PPG) sensor data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/SensorKit)*