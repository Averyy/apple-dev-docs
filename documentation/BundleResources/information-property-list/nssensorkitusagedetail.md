# NSSensorKitUsageDetail

**Framework**: Bundle Resources  
**Kind**: dictionary  
**Role**: Property List Key

A dictionary that includes keys for the specific information your app collects.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Details

- **Name**: `NSSensorKitUsageDetail`
- **Type**: dictionary

## Discussion

When your app attempts to read sensor information for the first time on a user’s device, the system presents a sheet that describes the information your app collects. You specify which information by defining an `Info.plist` key in this dictionary for each sensor your app uses, such as [`SRSensorUsageAmbientLightSensor`](./nssensorkitusagedetail/srsensorusageambientlightsensor.md). Users approve or deny your app’s ability to read private sensor information based on the description you provide for these properties.

For more information, see [Configuring your project for sensor reading](../../SensorKit/configuring-your-project-for-sensor-reading.md).

## Topics

### Device Activity
- [SRSensorUsageDeviceUsage](./nssensorkitusagedetail/srsensorusagedeviceusage.md)
  A collection of properties that explain your app’s need to observe how frequently a user’s device activates.
- [SRSensorUsageKeyboardMetrics](./nssensorkitusagedetail/srsensorusagekeyboardmetrics.md)
  A collection of properties that explain your app’s need to observe the user’s keyboard activity.
- [SRSensorUsageWristDetection](./nssensorkitusagedetail/srsensorusagewristdetection.md)
  A collection of properties that explain your app’s need to observe how the user wears their watch.
### App Activity
- [SRSensorUsageMessageUsage](./nssensorkitusagedetail/srsensorusagemessageusage.md)
  A collection of properties that explain your app’s need to observe the user’s activity in Messages.
- [SRSensorUsagePhoneUsage](./nssensorkitusagedetail/srsensorusagephoneusage.md)
  A collection of properties that explain your app’s need to observe the user’s phone activity.
### User Activity
- [SRSensorUsageECG](./nssensorkitusagedetail/srsensorusageecg.md)
  A collection of properties that explains your app’s need to observe the person’s electrocardiogram sensor data.
- [SRSensorUsageElevation](./nssensorkitusagedetail/srsensorusageelevation.md)
  A collection of properties that explains your app’s need to observe the device’s elevation data.
- [SRSensorUsageFacialMetrics](./nssensorkitusagedetail/srsensorusagefacialmetrics.md)
  A collection of properties that explains your app’s need to observe the user’s facial expressions.
- [SRSensorUsageHeartRate](./nssensorkitusagedetail/srsensorusageheartrate.md)
  A collection of properties that explains your app’s need to observe the user’s heart rate.
- [SRSensorUsageMediaEvents](./nssensorkitusagedetail/srsensorusagemediaevents.md)
  A collection of properties that explains your app’s need to observe the user’s interactions with media, such as images and videos, in messaging apps.
- [SRSensorUsageMotion](./nssensorkitusagedetail/srsensorusagemotion.md)
  A collection of properties that explain your app’s need to observe motion data.
- [SRSensorUsageOdometer](./nssensorkitusagedetail/srsensorusageodometer.md)
  A collection of properties that explains your app’s need to observe the user’s odometer data.
- [SRSensorUsagePedometer](./nssensorkitusagedetail/srsensorusagepedometer.md)
  A collection of properties that explain your app’s need to observe steps information.
- [SRSensorUsagePPG](./nssensorkitusagedetail/srsensorusageppg.md)
  A collection of properties that explains your app’s need to observe the person’s photoplethysmogram sensor data.
- [SRSensorUsageSpeechMetrics](./nssensorkitusagedetail/srsensorusagespeechmetrics.md)
  A collection of properties that explain your app’s need to analyze the user’s speech.
- [SRSensorUsageVisits](./nssensorkitusagedetail/srsensorusagevisits.md)
  A collection of properties that explain your app’s need to observe the locations that the user frequents.
- [SRSensorUsageWristTemperature](./nssensorkitusagedetail/srsensorusagewristtemperature.md)
  A collection of properties that explains your app’s need to observe the user’s wrist temperature while the user sleeps.
### Environment
- [SRSensorUsageAmbientLightSensor](./nssensorkitusagedetail/srsensorusageambientlightsensor.md)
  A collection of properties that explain your app’s need to observe light levels in the user’s environment.

## See Also

### Sensors
- [NSSensorKitUsageDescription](./nssensorkitusagedescription.md)
  A short description of the purpose of your app’s research study.
- [NSSensorKitPrivacyPolicyURL](./nssensorkitprivacypolicyurl.md)
  A hyperlink to a webpage that displays the privacy policy for your app’s research study.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nssensorkitusagedetail)*