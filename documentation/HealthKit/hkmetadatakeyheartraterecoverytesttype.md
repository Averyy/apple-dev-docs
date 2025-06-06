# HKMetadataKeyHeartRateRecoveryTestType

**Framework**: HealthKit  
**Kind**: var

The type of test that the source used to calculate a person’s heart-rate recovery.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
let HKMetadataKeyHeartRateRecoveryTestType: String
```

#### Discussion

Use this metadata key to identify the type of test that the [`HKSource`](hksource.md) used to calculate the value for a [`heartRateRecoveryOneMinute`](hkquantitytypeidentifier/heartraterecoveryoneminute.md) sample.

## Topics

### Heart rate recovery tests
- [enum HKHeartRateRecoveryTestType](hkheartraterecoverytesttype.md)
  The test that measured a person’s heart-rate recovery.

## See Also

- [let HKMetadataKeyBodyTemperatureSensorLocation: String](hkmetadatakeybodytemperaturesensorlocation.md)
  The location where a specific body temperature reading was taken.
- [let HKMetadataKeyHeartRateSensorLocation: String](hkmetadatakeyheartratesensorlocation.md)
  The location where a specific heart rate reading was taken.
- [let HKMetadataKeyHeartRateMotionContext: String](hkmetadatakeyheartratemotioncontext.md)
  The user’s activity level when the heart rate sample was measured.
- [let HKPredicateKeyPathAverageHeartRate: String](hkpredicatekeypathaverageheartrate.md)
  The key path for the sample’s average heart rate.
- [let HKMetadataKeyHeartRateRecoveryActivityDuration: String](hkmetadatakeyheartraterecoveryactivityduration.md)
- [let HKMetadataKeyHeartRateRecoveryActivityType: String](hkmetadatakeyheartraterecoveryactivitytype.md)
- [let HKMetadataKeyHeartRateRecoveryMaxObservedRecoveryHeartRate: String](hkmetadatakeyheartraterecoverymaxobservedrecoveryheartrate.md)
- [let HKMetadataKeyVO2MaxTestType: String](hkmetadatakeyvo2maxtesttype.md)
  The method used to calculate the user’s VO2 max rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmetadatakeyheartraterecoverytesttype)*