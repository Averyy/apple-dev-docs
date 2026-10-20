# numberOfTimesFallen

**Framework**: HealthKit  
**Kind**: property  
**Role**: Type Property

A quantity sample type that measures the number of times the user fell.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let numberOfTimesFallen: HKQuantityTypeIdentifier
```

```c
extern HKQuantityTypeIdentifier const HKQuantityTypeIdentifierNumberOfTimesFallen;
```

#### Discussion

These samples use count units (described in [`HKUnit`](../hkunit.md)) and measure cumulative values (described in [`HKQuantityAggregationStyle`](../hkquantityaggregationstyle.md)).

##### Detect and Respond to Falls

There are two approaches to detecting falls in your app. You can either query for [`numberOfTimesFallen`](./numberoftimesfallen.md) samples in HealthKit, or you can use Core Motion’s [`CMFallDetectionManager`](../../CoreMotion/cmfalldetectionmanager.md).

The Core Motion fall detection manager is particularly useful for apps that need to respond to falls in a timely manner so that the app can provide help to the person who fell.

The fall detection manager:

- Notifies the app in real time
- Notifies the app of all fall events
- Provides background runtime so that your app can respond to the fall

##### Detect and Monitor Falls Over Time

The HealthKit sample is particularly useful for apps that monitor falls over longer time periods, because there can be a delay between the fall event and HealthKit updating its samples.

HealthKit provides:

- Samples that are available on all devices that can access the person’s HealthKit data—not just the device that detected the fall
- Samples for falls where the person who fell confirmed the fall, or the system escalated the fall to emergency services. If the person who fell dismisses the fall alert, HealthKit doesn’t record the fall.

Both Core Motion and HealthKit need to authorize access to fall detection before they receive any notifications; however, Core Motion requires an additional entitlement from Apple. To apply for the entitlement, see [Fall Detection Entitlement Request](https://developer.apple.com/contact/request/fall-detection-api).

## See Also

### Lab and test results
- [static let bloodAlcoholContent: HKQuantityTypeIdentifier](./bloodalcoholcontent.md)
  A quantity sample type that measures the user’s blood alcohol content.
- [static let bloodGlucose: HKQuantityTypeIdentifier](./bloodglucose.md)
  A quantity sample type that measures the user’s blood glucose level.
- [static let electrodermalActivity: HKQuantityTypeIdentifier](./electrodermalactivity.md)
  A quantity sample type that measures electrodermal activity.
- [static let forcedExpiratoryVolume1: HKQuantityTypeIdentifier](./forcedexpiratoryvolume1.md)
  A quantity sample type that measures the amount of air that can be forcibly exhaled from the lungs during the first second of a forced exhalation.
- [static let forcedVitalCapacity: HKQuantityTypeIdentifier](./forcedvitalcapacity.md)
  A quantity sample type that measures the amount of air that can be forcibly exhaled from the lungs after taking the deepest breath possible.
- [static let inhalerUsage: HKQuantityTypeIdentifier](./inhalerusage.md)
  A quantity sample type that measures the number of puffs the user takes from their inhaler.
- [static let insulinDelivery: HKQuantityTypeIdentifier](./insulindelivery.md)
  A quantity sample that measures the amount of insulin delivered.
- [static let peakExpiratoryFlowRate: HKQuantityTypeIdentifier](./peakexpiratoryflowrate.md)
  A quantity sample type that measures the user’s maximum flow rate generated during a forceful exhalation.
- [static let peripheralPerfusionIndex: HKQuantityTypeIdentifier](./peripheralperfusionindex.md)
  A quantity sample type that measures the user’s peripheral perfusion index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/numberoftimesfallen)*