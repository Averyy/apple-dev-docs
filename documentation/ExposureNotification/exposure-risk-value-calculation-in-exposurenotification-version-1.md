# Exposure Risk Value Calculation in ExposureNotification Version 1

**Framework**: Exposure Notification

Learn how to determine a user’s risk of exposure.

#### Overview

The ExposureNotification framework uses an Exposure Risk Value to assist the user in determining whether they may have been exposed to the coronavirus. Health authorities have flexibility in calculating this value by setting weights and values in a configuration object.

To adopt this method of risk assessment, set the `ENAPIVersion` key to the integer value `1` in the app’s `Info.plist`.

The following diagram illustrates the data structure and formula used to calculate the Exposure Risk Value.

![A diagram that shows how the Exposure Risk Value is calculated.](https://docs-assets.developer.apple.com/published/f0dc0bbf69a650930047281f99a54461/media-3667011%402x.png)

The following parameters are used to calculate a risk for each exposure incident:

The [`totalRiskScore`](enexposureinfo/totalriskscore.md) is calculated using the following formula:

```swift
totalRiskScore = transmissionRiskValue * durationRiskValue *
daysSinceLastExposureRiskValue * attenuationRiskValue
```

Level values are in the range of 0-8. While the formula’s range can be up to 4096, the framework limits [`totalRiskScore`](enexposureinfo/totalriskscore.md) to the upper limit of [`ENRiskScore`](enriskscore.md), which has a maximum value of 255.

The following diagram illustrates an example of an Exposure Risk Value calculated for a person who was exposed to another person who was diagnosed positive.

![A diagram showing an example of calculating the risk score.](https://docs-assets.developer.apple.com/published/7e039cc5b66b62addecb0b41471bcf6d/media-3667010%402x.png)

For this example, the other user reported a positive diagnosis, the encounter between the two devices lasted 14 minutes, it happened 4 days ago, and the signal strength attenuation between their phones had a weighted average of 68. The `totalRiskScore` is limited and set to 255.

To exclude exposure incidents with a risk score below a certain amount, set  [`minimumRiskScoreFullRange`](enexposureconfiguration/minimumriskscorefullrange.md). The framework doesn’t use this property when calculating [`matchedKeyCount`](enexposuredetectionsummary/matchedkeycount.md) or [`daysSinceLastExposureThreshold`](enexposureconfiguration/dayssincelastexposurethreshold.md).

## Topics

### Exposure Information
- [class ENExposureInfo](enexposureinfo.md)
  The incident information related to a potential exposure.
- [typealias ENRiskScore](enriskscore.md)
  A value signifying the risk of an exposure event.
- [typealias ENRiskLevel](enrisklevel.md)
  The user’s estimated risk of exposure.
- [typealias ENRiskLevelValue](enrisklevelvalue.md)
  The value associated with a particular risk level.
### Level Configuration
- [var attenuationDurationThresholds: [NSNumber]](enexposureconfiguration/attenuationdurationthresholds.md)
  The configurable signal-loss thresholds for calculating exposure risk.
- [var attenuationLevelValues: [NSNumber]](enexposureconfiguration/attenuationlevelvalues.md)
  The level values for attenuation.
- [var daysSinceLastExposureLevelValues: [NSNumber]](enexposureconfiguration/dayssincelastexposurelevelvalues.md)
  The level values for days since last exposure.
- [var durationLevelValues: [NSNumber]](enexposureconfiguration/durationlevelvalues.md)
  The level values for duration.
- [var transmissionRiskLevelValues: [NSNumber]](enexposureconfiguration/transmissionrisklevelvalues.md)
  The level values for transmission risk.
- [var metadata: [AnyHashable : Any]?](enexposureconfiguration/metadata.md)
  The metadata you use to configure the exposure calculations.
### Minimum Threshold Configuration
- [var minimumRiskScore: ENRiskScore](enexposureconfiguration/minimumriskscore.md)
  The value that is the user’s minimum risk score.
- [var minimumRiskScoreFullRange: Double](enexposureconfiguration/minimumriskscorefullrange.md)
  The value that is the user’s full-range minimum risk score.
### Weight Configuration
- [var attenuationWeight: Double](enexposureconfiguration/attenuationweight.md)
  The weight assigned to a score for the Bluetooth signal strength.
- [var daysSinceLastExposureWeight: Double](enexposureconfiguration/dayssincelastexposureweight.md)
  The weight assigned to a score for the days since the user’s exposure.
- [var durationWeight: Double](enexposureconfiguration/durationweight.md)
  The weight assigned to a score for the duration of the user’s exposure.
- [var transmissionRiskWeight: Double](enexposureconfiguration/transmissionriskweight.md)
  The weight assigned to a score for the affected user’s estimated risk of transmission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/exposure-risk-value-calculation-in-exposurenotification-version-1)*