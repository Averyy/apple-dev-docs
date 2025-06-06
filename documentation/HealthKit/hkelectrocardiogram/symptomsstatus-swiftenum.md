# HKElectrocardiogram.SymptomsStatus

**Framework**: HealthKit  
**Kind**: enum

Values indicating whether the user entered a symptom when they recorded the ECG.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
enum SymptomsStatus
```

## Topics

### Status
- [HKElectrocardiogram.SymptomsStatus.none](hkelectrocardiogram/symptomsstatus-swift.enum/none.md)
  The user didn’t experience any symptoms during the duration of the electrocardiogram reading.
- [HKElectrocardiogram.SymptomsStatus.present](hkelectrocardiogram/symptomsstatus-swift.enum/present.md)
  The user added a symptom when they recorded the ECG.
- [HKElectrocardiogram.SymptomsStatus.notSet](hkelectrocardiogram/symptomsstatus-swift.enum/notset.md)
  The user didn’t specify whether or not they experienced symptoms.
### Initializers
- [init?(rawValue: Int)](hkelectrocardiogram/symptomsstatus-swift.enum/init(rawvalue:).md)

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
- [HKElectrocardiogram.Classification](hkelectrocardiogram/classification-swift.enum.md)
  Classifications returned by Apple Watch’s ECG algorithm.
- [var averageHeartRate: HKQuantity?](hkelectrocardiogram/averageheartrate.md)
  The user’s average heart rate during the ECG.
- [var symptomsStatus: HKElectrocardiogram.SymptomsStatus](hkelectrocardiogram/symptomsstatus-swift.property.md)
  A value that indicates whether the user entered a symptom when they recorded the ECG.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkelectrocardiogram/symptomsstatus-swift.enum)*