# HKElectrocardiogram.Classification.unrecognized

**Framework**: HealthKit  
**Kind**: case

A sample classification that this version of HealthKit doesn’t recognize.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
case unrecognized
```

#### Discussion

For example, if the Apple Watch recording the sample is running a newer version of watchOS, it may support classification types that aren’t included in this version. You can check the version of the algorithm used to classify the ECG by reading the value of the sample’s [`HKMetadataKeyAppleECGAlgorithmVersion`](hkmetadatakeyappleecgalgorithmversion.md) metadata key.

## See Also

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
- [HKElectrocardiogram.Classification.notSet](hkelectrocardiogram/classification-swift.enum/notset.md)
  A sample that doesn’t have an assigned classification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkelectrocardiogram/classification-swift.enum/unrecognized)*