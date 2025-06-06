# NSSensorKitUsageDetail

**Framework**: Bundle Resources  
**Kind**: dictionary

A dictionary that includes keys for the specific information your app collects.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

#### Discussion

When your app attempts to read sensor information for the first time on a user’s device, the system presents a sheet that describes the information your app collects. You specify which information by defining an `Info.plist` key in this dictionary for each sensor your app uses, such as [`SRSensorUsageAmbientLightSensor`](information-property-list/nssensorkitusagedetail/srsensorusageambientlightsensor.md). Users approve or deny your app’s ability to read private sensor information based on the description you provide for these properties.

For more information, see [`Configuring your project for sensor reading`](https://developer.apple.com/documentation/SensorKit/configuring-your-project-for-sensor-reading).

## Topics

### Device Activity
- [SRSensorUsageDeviceUsage](information-property-list/nssensorkitusagedetail/srsensorusagedeviceusage.md)
  A collection of properties that explain your app’s need to observe how frequently a user’s device activates.
- [SRSensorUsageKeyboardMetrics](information-property-list/nssensorkitusagedetail/srsensorusagekeyboardmetrics.md)
  A collection of properties that explain your app’s need to observe the user’s keyboard activity.
- [SRSensorUsageWristDetection](information-property-list/nssensorkitusagedetail/srsensorusagewristdetection.md)
  A collection of properties that explain your app’s need to observe how the user wears their watch.
### App Activity
- [SRSensorUsageMessageUsage](information-property-list/nssensorkitusagedetail/srsensorusagemessageusage.md)
  A collection of properties that explain your app’s need to observe the user’s activity in Messages.
- [SRSensorUsagePhoneUsage](information-property-list/nssensorkitusagedetail/srsensorusagephoneusage.md)
  A collection of properties that explain your app’s need to observe the user’s phone activity.
### User Activity
- [SRSensorUsageECG](information-property-list/nssensorkitusagedetail/srsensorusageecg.md)
  A collection of properties that explains your app’s need to observe the person’s electrocardiogram sensor data.
- [SRSensorUsageElevation](information-property-list/nssensorkitusagedetail/srsensorusageelevation.md)
  A collection of properties that explains your app’s need to observe the device’s elevation data.
- [SRSensorUsageFacialMetrics](information-property-list/nssensorkitusagedetail/srsensorusagefacialmetrics.md)
  A collection of properties that explains your app’s need to observe the user’s facial expressions.
- [SRSensorUsageHeartRate](information-property-list/nssensorkitusagedetail/srsensorusageheartrate.md)
  A collection of properties that explains your app’s need to observe the user’s heart rate.
- [SRSensorUsageMediaEvents](information-property-list/nssensorkitusagedetail/srsensorusagemediaevents.md)
  A collection of properties that explains your app’s need to observe the user’s interactions with media, such as images and videos, in messaging apps.
- [SRSensorUsageMotion](information-property-list/nssensorkitusagedetail/srsensorusagemotion.md)
  A collection of properties that explain your app’s need to observe motion data.
- [SRSensorUsageOdometer](information-property-list/nssensorkitusagedetail/srsensorusageodometer.md)
  A collection of properties that explains your app’s need to observe the user’s odometer data.
- [SRSensorUsagePedometer](information-property-list/nssensorkitusagedetail/srsensorusagepedometer.md)
  A collection of properties that explain your app’s need to observe steps information.
- [SRSensorUsagePPG](information-property-list/nssensorkitusagedetail/srsensorusageppg.md)
  A collection of properties that explains your app’s need to observe the person’s photoplethysmogram sensor data.
- [SRSensorUsageSpeechMetrics](information-property-list/nssensorkitusagedetail/srsensorusagespeechmetrics.md)
  A collection of properties that explain your app’s need to analyze the user’s speech.
- [SRSensorUsageVisits](information-property-list/nssensorkitusagedetail/srsensorusagevisits.md)
  A collection of properties that explain your app’s need to observe the locations that the user frequents.
- [SRSensorUsageWristTemperature](information-property-list/nssensorkitusagedetail/srsensorusagewristtemperature.md)
  A collection of properties that explains your app’s need to observe the user’s wrist temperature while the user sleeps.
### Environment
- [SRSensorUsageAmbientLightSensor](information-property-list/nssensorkitusagedetail/srsensorusageambientlightsensor.md)
  A collection of properties that explain your app’s need to observe light levels in the user’s environment.

## See Also

- [NSSensorKitUsageDescription](information-property-list/nssensorkitusagedescription.md)
  A short description of the purpose of your app’s research study.
- [NSSensorKitPrivacyPolicyURL](information-property-list/nssensorkitprivacypolicyurl.md)
  A hyperlink to a webpage that displays the privacy policy for your app’s research study.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nssensorkitusagedetail)*