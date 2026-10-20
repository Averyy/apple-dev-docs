# HKElectrocardiogramQuery.Result

**Framework**: HealthKit  
**Kind**: enum  
**Role**: Enumeration

Partial results for an electrocardiogram query.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS
- watchOS 7.0+

## Declaration

```swift
enum Result
```

#### Overview

The query returns a [`HKElectrocardiogramQuery.Result.measurement(_:)`](./result/measurement%28_%29.md) result for each voltage measurement, followed by a [`HKElectrocardiogramQuery.Result.done`](./result/done.md) result.

## Topics

### Results
- [case measurement(HKElectrocardiogram.VoltageMeasurement)](./result/measurement%28_%29.md)
  A single voltage measurement.
- [HKElectrocardiogramQuery.Result.done](./result/done.md)
  The query has finished returning voltage measurements.
- [HKElectrocardiogramQuery.Result.error(_:)](./result/error%28_%29.md)
  An error occurred while accessing the voltage measurements.

## See Also

### Accessing the Results
- [init(electrocardiogram: HKElectrocardiogram, dataHandler: (HKElectrocardiogramQuery, HKElectrocardiogram.VoltageMeasurement?, Bool, (any Error)?) -> Void)](./init%28electrocardiogram,datahandler%29.md)
  Creates a new electrocardiogram query object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkelectrocardiogramquery/result)*