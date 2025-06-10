# HKElectrocardiogram.SymptomsStatus.present

**Framework**: HealthKit  
**Kind**: case

The user added a symptom when they recorded the ECG.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
case present
```

#### Discussion

To access the symptoms, query for the [`HKCategorySample`](hkcategorysample.md) samples associated with the electrocardiogram sample.

## See Also

- [HKElectrocardiogram.SymptomsStatus.none](hkelectrocardiogram/symptomsstatus-swift.enum/none.md)
  The user didn’t enter a symptom when they recorded the ECG.
- [HKElectrocardiogram.SymptomsStatus.notSet](hkelectrocardiogram/symptomsstatus-swift.enum/notset.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkelectrocardiogram/symptomsstatus-swift.enum/present)*