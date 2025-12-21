# init(electrocardiogram:dataHandler:)

**Framework**: HealthKit  
**Kind**: init

Creates a new electrocardiogram query object.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
init(electrocardiogram: HKElectrocardiogram, dataHandler: @escaping (HKElectrocardiogramQuery, HKElectrocardiogram.VoltageMeasurement?, Bool, (any Error)?) -> Void)
```

#### Discussion

When you run the query, it calls the data handler once for each voltage measurement, passing the voltage data. On the last voltage measurement, it sets the `done` parameter to [`true`](https://developer.apple.com/documentation/Swift/true). If an error occurs, it stops collecting voltage data and calls the data handler; it sets the `voltageMeasurement` parameter to `nil`, and passes in an [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) object that describes the error.

## Parameters

- `electrocardiogram`: The electrocardiogram sample whose voltages you want to access.
- `dataHandler`: A block that the query calls repeatedly to return the voltage data. The handler takes the following parameters:

## See Also

- [HKElectrocardiogramQuery.Result](hkelectrocardiogramquery/result.md)
  Partial results for an electrocardiogram query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkelectrocardiogramquery/init(electrocardiogram:datahandler:))*