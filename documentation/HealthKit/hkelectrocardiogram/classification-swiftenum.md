# HKElectrocardiogram.Classification

**Framework**: HealthKit  
**Kind**: enum

Classifications returned by Apple Watch’s ECG algorithm.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
enum Classification
```

## Topics

### Classifications
- [HKElectrocardiogram.Classification.sinusRhythm](hkelectrocardiogram/classification-swift.enum/sinusrhythm.md)
  The sample exhibits no signs of atrial fibrillation.
- [HKElectrocardiogram.Classification.atrialFibrillation](hkelectrocardiogram/classification-swift.enum/atrialfibrillation.md)
  The sample exhibits signs of atrial fibrillation.
- [HKElectrocardiogram.Classification.inconclusiveHighHeartRate](hkelectrocardiogram/classification-swift.enum/inconclusivehighheartrate.md)
  An unclassifiable sample caused by a rapid heart rate.
- [HKElectrocardiogram.Classification.inconclusiveLowHeartRate](hkelectrocardiogram/classification-swift.enum/inconclusivelowheartrate.md)
  An unclassifiable sample caused by a heart rate below 50 bpm.
- [HKElectrocardiogram.Classification.inconclusivePoorReading](hkelectrocardiogram/classification-swift.enum/inconclusivepoorreading.md)
  An unclassifiable sample caused by an unclear signal.
- [HKElectrocardiogram.Classification.inconclusiveOther](hkelectrocardiogram/classification-swift.enum/inconclusiveother.md)
  An unclassifiable sample caused by an unknown issue.
- [HKElectrocardiogram.Classification.unrecognized](hkelectrocardiogram/classification-swift.enum/unrecognized.md)
  A sample classification that this version of HealthKit doesn’t recognize.
- [HKElectrocardiogram.Classification.notSet](hkelectrocardiogram/classification-swift.enum/notset.md)
  A sample that doesn’t have an assigned classification.
### Initializers
- [init?(rawValue: Int)](hkelectrocardiogram/classification-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var classification: HKElectrocardiogram.Classification](hkelectrocardiogram/classification-swift.property.md)
  The ECG’s classification.
- [var averageHeartRate: HKQuantity?](hkelectrocardiogram/averageheartrate.md)
  The user’s average heart rate during the ECG.
- [var symptomsStatus: HKElectrocardiogram.SymptomsStatus](hkelectrocardiogram/symptomsstatus-swift.property.md)
  A value that indicates whether the user entered a symptom when they recorded the ECG.
- [HKElectrocardiogram.SymptomsStatus](hkelectrocardiogram/symptomsstatus-swift.enum.md)
  Values indicating whether the user entered a symptom when they recorded the ECG.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkelectrocardiogram/classification-swift.enum)*