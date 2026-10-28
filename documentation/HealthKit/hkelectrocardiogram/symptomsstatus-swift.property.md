# symptomsStatus

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

A value that indicates whether the user entered a symptom when they recorded the ECG.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var symptomsStatus: HKElectrocardiogram.SymptomsStatus { get }
```

```objc
@property (nonatomic, assign, readonly) HKElectrocardiogramSymptomsStatus symptomsStatus;
```

## Discussion

If the value is [`HKElectrocardiogram.SymptomsStatus.present`](./symptomsstatus-swift.enum/present.md), you can access the symptoms by querying for the [`HKCategorySample`](../hkcategorysample.md) samples associated with the electrocardiogram sample. Use [`predicateForObjectsAssociated(electrocardiogram:)`](../hkquery/predicateforobjectsassociated%28electrocardiogram%29.md) to create the predicate for the associated symptoms.

## See Also

### Accessing Overview Information
- [var classification: HKElectrocardiogram.Classification](./classification-swift.property.md)
  The ECG’s classification.
- [HKElectrocardiogram.Classification](./classification-swift.enum.md)
  Classifications returned by Apple Watch’s ECG algorithm.
- [var averageHeartRate: HKQuantity?](./averageheartrate.md)
  The user’s average heart rate during the ECG.
- [HKElectrocardiogram.SymptomsStatus](./symptomsstatus-swift.enum.md)
  Values indicating whether the user entered a symptom when they recorded the ECG.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkelectrocardiogram/symptomsstatus-swift.property)*