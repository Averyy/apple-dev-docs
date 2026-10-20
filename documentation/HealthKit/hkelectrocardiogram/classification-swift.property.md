# classification

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The ECG’s classification.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var classification: HKElectrocardiogram.Classification { get }
```

```objc
@property (nonatomic, assign, readonly) HKElectrocardiogramClassification classification;
```

## See Also

### Accessing Overview Information
- [HKElectrocardiogram.Classification](./classification-swift.enum.md)
  Classifications returned by Apple Watch’s ECG algorithm.
- [var averageHeartRate: HKQuantity?](./averageheartrate.md)
  The user’s average heart rate during the ECG.
- [var symptomsStatus: HKElectrocardiogram.SymptomsStatus](./symptomsstatus-swift.property.md)
  A value that indicates whether the user entered a symptom when they recorded the ECG.
- [HKElectrocardiogram.SymptomsStatus](./symptomsstatus-swift.enum.md)
  Values indicating whether the user entered a symptom when they recorded the ECG.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkelectrocardiogram/classification-swift.property)*