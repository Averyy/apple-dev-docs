# HKElectrocardiogram.Classification.inconclusivePoorReading

**Framework**: HealthKit  
**Kind**: case  
**Role**: Case

An unclassifiable sample caused by an unclear signal.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
case inconclusivePoorReading
```

```c
HKElectrocardiogramClassificationInconclusivePoorReading
```

## Discussion

Apple Watch reports a poor recording when circumstances cause the watch to collect insufficient or inaccurate data, such as when the user wears the watch too loosely on their wrist, or if the user’s arm isn’t resting on a firm surface. The user can make another attempt at measuring their ECG after fixing the issue.

## See Also

### Classifications
- [HKElectrocardiogram.Classification.sinusRhythm](./sinusrhythm.md)
  The sample exhibits no signs of atrial fibrillation.
- [HKElectrocardiogram.Classification.atrialFibrillation](./atrialfibrillation.md)
  The sample exhibits signs of atrial fibrillation.
- [HKElectrocardiogram.Classification.inconclusiveHighHeartRate](./inconclusivehighheartrate.md)
  An unclassifiable sample caused by a rapid heart rate.
- [HKElectrocardiogram.Classification.inconclusiveLowHeartRate](./inconclusivelowheartrate.md)
  An unclassifiable sample caused by a heart rate below 50 bpm.
- [HKElectrocardiogram.Classification.inconclusiveOther](./inconclusiveother.md)
  An unclassifiable sample caused by an unknown issue.
- [HKElectrocardiogram.Classification.unrecognized](./unrecognized.md)
  A sample classification that this version of HealthKit doesn’t recognize.
- [HKElectrocardiogram.Classification.notSet](./notset.md)
  A sample that doesn’t have an assigned classification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkelectrocardiogram/classification-swift.enum/inconclusivepoorreading)*