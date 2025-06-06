# symptomsStatus

**Framework**: HealthKit  
**Kind**: property

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

#### Discussion

If the value is [`HKElectrocardiogram.SymptomsStatus.present`](hkelectrocardiogram/symptomsstatus-swift.enum/present.md), you can access the symptoms by querying for the [`HKCategorySample`](hkcategorysample.md) samples associated with the electrocardiogram sample. Use [`predicateForObjectsAssociated(electrocardiogram:)`](hkquery/predicateforobjectsassociated(electrocardiogram:).md) to create the predicate for the associated symptoms.

## See Also

- [var classification: HKElectrocardiogram.Classification](hkelectrocardiogram/classification-swift.property.md)
  The ECG’s classification.
- [HKElectrocardiogram.Classification](hkelectrocardiogram/classification-swift.enum.md)
  Classifications returned by Apple Watch’s ECG algorithm.
- [var averageHeartRate: HKQuantity?](hkelectrocardiogram/averageheartrate.md)
  The user’s average heart rate during the ECG.
- [HKElectrocardiogram.SymptomsStatus](hkelectrocardiogram/symptomsstatus-swift.enum.md)
  Values indicating whether the user entered a symptom when they recorded the ECG.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkelectrocardiogram/symptomsstatus-swift.property)*