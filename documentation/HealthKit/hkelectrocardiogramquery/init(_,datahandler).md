# init(_:dataHandler:)

**Framework**: HealthKit  
**Kind**: init  
**Role**: Initializer

Creates a new electrocardiogram query object.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS
- watchOS 7.0+

## Declaration

```swift
convenience init(_ ecg: HKElectrocardiogram, dataHandler: @escaping (HKElectrocardiogramQuery, HKElectrocardiogramQuery.Result) -> Void)
```

#### Discussion

When you run the query, it calls the data handler once for each voltage measurement, passing a [`HKElectrocardiogramQuery.Result.measurement(_:)`](./result/measurement%28_%29.md) instance that contains the voltage data. After it has sent all the voltage measurements, it calls the data handler one last time, passing [`HKElectrocardiogramQuery.Result.done`](./result/done.md). If an error occurs, it stops collecting voltage data and passes [`HKElectrocardiogramQuery.Result.error(_:)`](./result/error%28_%29.md) instead.

## Parameters

- `ecg`: The electrocardiogram sample whose voltages you want to access.
- `dataHandler`: A block that the query calls repeatedly to return the voltage data. The handler takes the following parameters:

  - **`query`**: The query that returned the results.
  - **result**: An enumeration that contains a result value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkelectrocardiogramquery/init(_:datahandler:))*