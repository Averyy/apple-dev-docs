# allowsRecalibrationForEstimates

**Framework**: HealthKit  
**Kind**: property

A Boolean value that indicates whether HealthKit supports recalibrating the prediction algorithm used to produce estimates for this sample type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var allowsRecalibrationForEstimates: Bool { get }
```

#### Discussion

To recalibrate the data for this sample type, call the [`HKHealthStore`](hkhealthstore.md) class’s [`recalibrateEstimates(sampleType:date:completion:)`](hkhealthstore/recalibrateestimates(sampletype:date:completion:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksampletype/allowsrecalibrationforestimates)*