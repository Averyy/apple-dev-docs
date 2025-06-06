# sensorReader(_:fetching:didFetchResult:)

**Framework**: SensorKit  
**Kind**: method

Provides the delegate with a fetch result.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
optional func sensorReader(_ reader: SRSensorReader, fetching fetchRequest: SRFetchRequest, didFetchResult result: SRFetchResult<AnyObject>) -> Bool
```

#### Discussion

The framework expects the app to know the result’s type based on the reader’s sensor. To see a list of result types per sensor, see [`Sample types`](srfetchresult/sample#Sample-types.md).

When a fetch produces multiple results, the framework invokes this callback once for each result.

To reuse a fetch result within the scope of this function, create a copy of `fetchResult` rather than assigning a strong reference to it.

## Parameters

- `reader`: The sensor reader for which the fetch provides results.
- `fetchRequest`: The completed fetch request.
- `result`: The fetch request’s result.

## See Also

- [func sensorReader(SRSensorReader, didCompleteFetch: SRFetchRequest)](srsensorreaderdelegate/sensorreader(_:didcompletefetch:).md)
  Provides the delegate with a completed fetch request.
- [func sensorReader(SRSensorReader, fetching: SRFetchRequest, failedWithError: any Error)](srsensorreaderdelegate/sensorreader(_:fetching:failedwitherror:).md)
  Provides the delegate with a fetch failure reason.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:fetching:didfetchresult:))*