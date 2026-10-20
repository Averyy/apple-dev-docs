# HKElectrocardiogram.Classification

**Framework**: HealthKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum HKElectrocardiogramClassification : NSInteger;
```

## Topics

### Classifications
- [HKElectrocardiogram.Classification.sinusRhythm](./classification-swift.enum/sinusrhythm.md)
  The sample exhibits no signs of atrial fibrillation.
- [HKElectrocardiogram.Classification.atrialFibrillation](./classification-swift.enum/atrialfibrillation.md)
  The sample exhibits signs of atrial fibrillation.
- [HKElectrocardiogram.Classification.inconclusiveHighHeartRate](./classification-swift.enum/inconclusivehighheartrate.md)
  An unclassifiable sample caused by a rapid heart rate.
- [HKElectrocardiogram.Classification.inconclusiveLowHeartRate](./classification-swift.enum/inconclusivelowheartrate.md)
  An unclassifiable sample caused by a heart rate below 50 bpm.
- [HKElectrocardiogram.Classification.inconclusivePoorReading](./classification-swift.enum/inconclusivepoorreading.md)
  An unclassifiable sample caused by an unclear signal.
- [HKElectrocardiogram.Classification.inconclusiveOther](./classification-swift.enum/inconclusiveother.md)
  An unclassifiable sample caused by an unknown issue.
- [HKElectrocardiogram.Classification.unrecognized](./classification-swift.enum/unrecognized.md)
  A sample classification that this version of HealthKit doesn’t recognize.
- [HKElectrocardiogram.Classification.notSet](./classification-swift.enum/notset.md)
  A sample that doesn’t have an assigned classification.
### Initializers
- [init?(rawValue: Int)](./classification-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing Overview Information
- [var classification: HKElectrocardiogram.Classification](./classification-swift.property.md)
  The ECG’s classification.
- [var averageHeartRate: HKQuantity?](./averageheartrate.md)
  The user’s average heart rate during the ECG.
- [var symptomsStatus: HKElectrocardiogram.SymptomsStatus](./symptomsstatus-swift.property.md)
  A value that indicates whether the user entered a symptom when they recorded the ECG.
- [HKElectrocardiogram.SymptomsStatus](./symptomsstatus-swift.enum.md)
  Values indicating whether the user entered a symptom when they recorded the ECG.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkelectrocardiogram/classification-swift.enum)*