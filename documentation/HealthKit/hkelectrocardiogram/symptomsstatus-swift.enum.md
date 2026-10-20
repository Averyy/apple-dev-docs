# HKElectrocardiogram.SymptomsStatus

**Framework**: HealthKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum HKElectrocardiogramSymptomsStatus : NSInteger;
```

## Topics

### Status
- [HKElectrocardiogram.SymptomsStatus.none](./symptomsstatus-swift.enum/none.md)
  The user didn’t experience any symptoms during the duration of the electrocardiogram reading.
- [HKElectrocardiogram.SymptomsStatus.present](./symptomsstatus-swift.enum/present.md)
  The user added a symptom when they recorded the ECG.
- [HKElectrocardiogram.SymptomsStatus.notSet](./symptomsstatus-swift.enum/notset.md)
  The user didn’t specify whether or not they experienced symptoms.
### Initializers
- [init?(rawValue: Int)](./symptomsstatus-swift.enum/init%28rawvalue%29.md)

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
- [HKElectrocardiogram.Classification](./classification-swift.enum.md)
  Classifications returned by Apple Watch’s ECG algorithm.
- [var averageHeartRate: HKQuantity?](./averageheartrate.md)
  The user’s average heart rate during the ECG.
- [var symptomsStatus: HKElectrocardiogram.SymptomsStatus](./symptomsstatus-swift.property.md)
  A value that indicates whether the user entered a symptom when they recorded the ECG.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkelectrocardiogram/symptomsstatus-swift.enum)*