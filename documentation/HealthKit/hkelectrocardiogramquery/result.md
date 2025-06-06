# HKElectrocardiogramQuery.Result

**Framework**: HealthKit  
**Kind**: enum

Partial results for an electrocardiogram query.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
enum Result
```

#### Overview

The query returns a [`HKElectrocardiogramQuery.Result.measurement(_:)`](hkelectrocardiogramquery/result/measurement(_:).md) result for each voltage measurement, followed by a [`HKElectrocardiogramQuery.Result.done`](hkelectrocardiogramquery/result/done.md) result.

## Topics

### Results
- [case measurement(HKElectrocardiogram.VoltageMeasurement)](hkelectrocardiogramquery/result/measurement(_:).md)
  A single voltage measurement.
- [HKElectrocardiogramQuery.Result.done](hkelectrocardiogramquery/result/done.md)
  The query has finished returning voltage measurements.
- [HKElectrocardiogramQuery.Result.error(_:)](hkelectrocardiogramquery/result/error(_:).md)
  An error occurred while accessing the voltage measurements.

## See Also

- [init(electrocardiogram: HKElectrocardiogram, dataHandler: (HKElectrocardiogramQuery, HKElectrocardiogram.VoltageMeasurement?, Bool, (any Error)?) -> Void)](hkelectrocardiogramquery/init(electrocardiogram:datahandler:).md)
  Creates a new electrocardiogram query object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkelectrocardiogramquery/result)*