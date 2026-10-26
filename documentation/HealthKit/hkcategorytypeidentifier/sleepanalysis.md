# sleepAnalysis

**Framework**: HealthKit  
**Kind**: property  
**Role**: Type Property

A category sample type for sleep analysis information.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let sleepAnalysis: HKCategoryTypeIdentifier
```

```c
extern HKCategoryTypeIdentifier const HKCategoryTypeIdentifierSleepAnalysis;
```

## Mentions

- [Saving data to HealthKit](../saving-data-to-healthkit.md)

#### Discussion

These samples use values from the [`HKCategoryValueSleepAnalysis`](../hkcategoryvaluesleepanalysis.md) enum.

For best results when analyzing sleep samples, it’s recommended that you use [`HKMetadataKeyTimeZone`](../hkmetadatakeytimezone.md) to store time zone metadata with your sleep sample data.

## See Also

### Mindfulness and sleep
- [static let mindfulSession: HKCategoryTypeIdentifier](./mindfulsession.md)
  A category sample type for recording a mindful session.
- [static let appleSleepingWristTemperature: HKQuantityTypeIdentifier](../hkquantitytypeidentifier/applesleepingwristtemperature.md)
  A quantity sample type that records the wrist temperature during sleep.
- [enum HKAppleSleepingBreathingDisturbancesClassification](../hkapplesleepingbreathingdisturbancesclassification.md)
- [HKCategoryValueSleepAnalysisAsleepValues](../hkcategoryvaluesleepanalysisasleepvalues.md)
- [HKAppleSleepingBreathingDisturbancesClassificationForQuantity](../hkapplesleepingbreathingdisturbancesclassificationforquantity.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier/sleepanalysis)*