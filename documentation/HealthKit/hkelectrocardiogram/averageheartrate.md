# averageHeartRate

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The user’s average heart rate during the ECG.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@NSCopying
var averageHeartRate: HKQuantity? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) HKQuantity * averageHeartRate;
```

## See Also

### Accessing Overview Information
- [var classification: HKElectrocardiogram.Classification](./classification-swift.property.md)
  The ECG’s classification.
- [HKElectrocardiogram.Classification](./classification-swift.enum.md)
  Classifications returned by Apple Watch’s ECG algorithm.
- [var symptomsStatus: HKElectrocardiogram.SymptomsStatus](./symptomsstatus-swift.property.md)
  A value that indicates whether the user entered a symptom when they recorded the ECG.
- [HKElectrocardiogram.SymptomsStatus](./symptomsstatus-swift.enum.md)
  Values indicating whether the user entered a symptom when they recorded the ECG.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkelectrocardiogram/averageheartrate)*