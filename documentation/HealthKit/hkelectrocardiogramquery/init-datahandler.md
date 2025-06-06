# init(_:dataHandler:)

**Framework**: HealthKit  
**Kind**: init

Creates a new electrocardiogram query object.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
convenience init(_ ecg: HKElectrocardiogram, dataHandler: @escaping (HKElectrocardiogramQuery, HKElectrocardiogramQuery.Result) -> Void)
```

#### Discussion

When you run the query, it calls the data handler once for each voltage measurement, passing a [`HKElectrocardiogramQuery.Result.measurement(_:)`](hkelectrocardiogramquery/result/measurement(_:).md) instance that contains the voltage data. After it has sent all the voltage measurements, it calls the data handler one last time, passing [`HKElectrocardiogramQuery.Result.done`](hkelectrocardiogramquery/result/done.md). If an error occurs, it stops collecting voltage data and passes [`HKElectrocardiogramQuery.Result.error(_:)`](hkelectrocardiogramquery/result/error(_:).md) instead.

## Parameters

- `ecg`: The electrocardiogram sample whose voltages you want to access.
- `dataHandler`: A block that the query calls repeatedly to return the voltage data. The handler takes the following parameters:


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkelectrocardiogramquery/init(_:datahandler:))*