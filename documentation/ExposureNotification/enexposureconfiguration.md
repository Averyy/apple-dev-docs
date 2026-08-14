# ENExposureConfiguration

**Framework**: Exposure Notification  
**Kind**: class

The object that contains parameters for configuring exposure notification risk scoring behavior.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
class ENExposureConfiguration
```

## Mentions

- [Supporting Exposure Notifications in iOS 12.5](supporting-exposure-notifications-in-ios-12-5.md)

#### Overview

> ❗ **Important**:  This class is available in iOS 12.5, and in iOS 13.5 and later.

The ExposureNotification framework defines an Exposure Risk Value (ERV) to allow Health Authorities to define when to alert a user that they may have been exposed to someone diagnosed with COVID-19. The app uses the ERV to calculate the user’s Meaningful Exposure Minutes (MEMs) value. Health Authorities have flexibility in calculating this value by setting weights and values related to Bluetooth attenuations, infectiousness of the affected individual, and diagnosis report type. They can also determine what threshold will result in a notification.

> ❗ **Important**:  While the ERV is measured in MEMs, the system actually calculates and returns a number of seconds, rounded to the nearest minute. For example, if a person has an ERV of 2 MEMs, the app returns a value of 120 (seconds). Convert ERVs to minutes before displaying it to the user by dividing the returned value by 60.

The calculation method described in this document is available starting with iOS 14. To adopt this method of risk assessment, set the `ENAPIVersion` key to the integer value 2 in the app’s `Info.plist` file. For more information on the V1 calculation used in earlier versions of iOS, see [`Exposure Risk Value Calculation in ExposureNotification Version 1`](exposure-risk-value-calculation-in-exposurenotification-version-1.md).

The following diagram shows how to calculate an ERV:

![A diagram showing how to calculate the exposure ERV.](/images/com.apple.exposurenotification/media-3670910@2x.png)

The class defines three sets of weights that give priority to the components of the ERV: minutes-at-attenuation, infectiousness, and report type.

The weighted minutes-at-attenuation assigns priority to the amount of time that the user is near beacons at different Bluetooth attenuations. Assign values between 0–250 percent to weights that represent Immediate, Near, Medium, and Other distances.

![A diagram showing the weighted minutes-at-attenuation calculation.](/images/com.apple.exposurenotification/media-3670915@2x.png)

The infectiousness weight modifies the ERV based on the affected userʼs infectiousness level for the day of exposure relative to the day of symptom onset. To set the infectiousness level for when there is no symptom onset date provided, use [`ENDaysSinceOnsetOfSymptomsUnknown`](endayssinceonsetofsymptomsunknown.md). A user’s infectiousness level can be [`ENInfectiousness.high`](eninfectiousness/high.md), [`ENInfectiousness.standard`](eninfectiousness/standard.md), or [`ENInfectiousness.none`](eninfectiousness/none.md). Assign both [`infectiousnessHighWeight`](enexposureconfiguration/infectiousnesshighweight.md) and [`infectiousnessStandardWeight`](enexposureconfiguration/infectiousnessstandardweight.md) a value between 0 percent and 250 percent.

![A diagram showing a user’s infectiousness over the course of days.](/images/com.apple.exposurenotification/media-3671401@2x.png)

The weighted report type assigns priority to the method of diagnosis. Assign values ranging from 0–250 percent to weights that represent a confirmed test diagnosis, clinical diagnosis, self- reported diagnoisis, and recursive diagnosis.

![A table showing the weighted report types and their ranges.](/images/com.apple.exposurenotification/media-3670917@2x.png)

In addition to setting the weights, you can perform additional filtering by setting [`daysSinceLastExposureThreshold`](enexposureconfiguration/dayssincelastexposurethreshold.md) to limit the number of days to consider when calculating the risk level.

##### Calculating an Example Exposure Risk Value

The following diagrams illustrate calculating an ERV using a real-world scenario.

The weighted minutes-at-attenuation shows 5 minutes of immediate exposure with a 150 percent weight, 10 minutes of near exposure with a 100 percent weight, 10 minutes of medium exposure with a 50 percent weight, and 5 minutes of other exposure with a 0 percent weight.

![A diagram showing the weighted minutes-at-attention example.](/images/com.apple.exposurenotification/media-3670907@2x.png)

The weighted infectiousness indicates days –14 to –6 from the current day with no infectiousness, days –5 to –3 with 100 percent of standard infectiousness, days –2 to +5 with 200 percent high infectiousness, days +6 to +10 with 100 percent standard infectiousness, and days +11 to +14 with no infectiousness.

![A diagram showing an example of infectiousness weights over the course of 29 days.](/images/com.apple.exposurenotification/media-3671402@2x.png)

Here are the weighted report types for all three tests:

![A table showing the weighted report types in the example.](/images/com.apple.exposurenotification/media-3670914@2x.png)

The result of the calculation shows an ERV of 45 minutes:

![A diagram showing an example of calculating the ERV.](/images/com.apple.exposurenotification/media-3670911@2x.png)

> ❗ **Important**:  To prevent an ERV of 0, set any unused weight to 100 percent.

## Topics

### Configuring Duration
- [var attenuationDurationThresholds: [NSNumber]](enexposureconfiguration/attenuationdurationthresholds.md)
  The configurable signal-loss thresholds for calculating exposure risk.
- [var immediateDurationWeight: Double](enexposureconfiguration/immediatedurationweight.md)
  The weight assigned to a risk level indicating the duration of the user’s exposure at immediate distance.
- [var mediumDurationWeight: Double](enexposureconfiguration/mediumdurationweight.md)
  The weight assigned to a risk level indicating the duration of the user’s exposure at medium distance.
- [var nearDurationWeight: Double](enexposureconfiguration/neardurationweight.md)
  The weight assigned to a risk level indicating the duration of the user’s exposure at close distance.
- [var otherDurationWeight: Double](enexposureconfiguration/otherdurationweight.md)
  The weight assigned to a risk level indicating the duration of the user’s exposure at a large distance.
- [var daysSinceLastExposureThreshold: Int](enexposureconfiguration/dayssincelastexposurethreshold.md)
  The number of days to consider when calculating the risk level.
### Configuring Infectiousness
- [var infectiousnessForDaysSinceOnsetOfSymptoms: [NSNumber : NSNumber]?](enexposureconfiguration/infectiousnessfordayssinceonsetofsymptoms.md)
  The mapping between the days since onset of symptoms to the degree of infectiousness.
- [var infectiousnessHighWeight: Double](enexposureconfiguration/infectiousnesshighweight.md)
  The weight to apply for severe infectiousness.
- [var infectiousnessStandardWeight: Double](enexposureconfiguration/infectiousnessstandardweight.md)
  The weight to apply for mild infectiousness.
- [var ENDaysSinceOnsetOfSymptomsUnknown: Int](endayssinceonsetofsymptomsunknown.md)
  A value used when the number of days since onset of symptoms is unknown.
### Configuring Report Types
- [var reportTypeConfirmedClinicalDiagnosisWeight: Double](enexposureconfiguration/reporttypeconfirmedclinicaldiagnosisweight.md)
  The weight assigned to a risk level based on a confirmed clinical diagnosis.
- [var reportTypeConfirmedTestWeight: Double](enexposureconfiguration/reporttypeconfirmedtestweight.md)
  The weight assigned to a risk level based on a confirmed test.
- [var reportTypeRecursiveWeight: Double](enexposureconfiguration/reporttyperecursiveweight.md)
  The weight assigned to a risk level based on an exposure to someone exposed to someone else.
- [var reportTypeSelfReportedWeight: Double](enexposureconfiguration/reporttypeselfreportedweight.md)
  The weight assigned to a risk level based on a self-reported diagnoisis.
- [var reportTypeNoneMap: ENDiagnosisReportType](enexposureconfiguration/reporttypenonemap.md)
  The report type to map an unknown diagnosis to.
### Determining Exposure Risk Level in Version 1
- [Exposure Risk Value Calculation in ExposureNotification Version 1](exposure-risk-value-calculation-in-exposurenotification-version-1.md)
  Learn how to determine a user’s risk of exposure.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [Configuring Exposure Notifications](configuring-exposure-notifications.md)
  Define how Exposure Notifications work for a region by assigning server-based key-value pairs.
- [class ENExposureWindow](enexposurewindow.md)
  A set of scan events from observed beacons within a time span.
- [class ENScanInstance](enscaninstance.md)
  The aggregation of attenuations of beacons received during a scan.
- [Exposure Parameter Limits](exposure-parameter-limits.md)
  The limits for the parameters you use in exposure risk calculations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposureconfiguration)*