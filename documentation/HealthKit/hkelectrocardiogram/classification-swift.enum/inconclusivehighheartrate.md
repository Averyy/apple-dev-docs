# HKElectrocardiogram.Classification.inconclusiveHighHeartRate

**Framework**: HealthKit  
**Kind**: case  
**Role**: Case

An unclassifiable sample caused by a rapid heart rate.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
case inconclusiveHighHeartRate
```

```c
HKElectrocardiogramClassificationInconclusiveHighHeartRate
```

#### Discussion

The [`HKAppleECGAlgorithmVersion.version1`](../../hkappleecgalgorithmversion/version1.md) algorithm can categorize heart rates below 120 BPM. [`HKAppleECGAlgorithmVersion.version2`](../../hkappleecgalgorithmversion/version2.md) can categorize heart rates up to 150 BPM.

## See Also

### Classifications
- [HKElectrocardiogram.Classification.sinusRhythm](./sinusrhythm.md)
  The sample exhibits no signs of atrial fibrillation.
- [HKElectrocardiogram.Classification.atrialFibrillation](./atrialfibrillation.md)
  The sample exhibits signs of atrial fibrillation.
- [HKElectrocardiogram.Classification.inconclusiveLowHeartRate](./inconclusivelowheartrate.md)
  An unclassifiable sample caused by a heart rate below 50 bpm.
- [HKElectrocardiogram.Classification.inconclusivePoorReading](./inconclusivepoorreading.md)
  An unclassifiable sample caused by an unclear signal.
- [HKElectrocardiogram.Classification.inconclusiveOther](./inconclusiveother.md)
  An unclassifiable sample caused by an unknown issue.
- [HKElectrocardiogram.Classification.unrecognized](./unrecognized.md)
  A sample classification that this version of HealthKit doesn’t recognize.
- [HKElectrocardiogram.Classification.notSet](./notset.md)
  A sample that doesn’t have an assigned classification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkelectrocardiogram/classification-swift.enum/inconclusivehighheartrate)*