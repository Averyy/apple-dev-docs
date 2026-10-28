# sensorReader(_:fetching:didFetchResult:)

**Framework**: SensorKit  
**Kind**: method  
**Role**: Instance Method

Provides the delegate with a fetch result.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0

> **Deprecated**: Use SRReader<Sensor> class

## Declaration

```swift
optional func sensorReader(_ reader: SRSensorReader, fetching fetchRequest: SRFetchRequest, didFetchResult result: SRFetchResult<AnyObject>) -> Bool
```

```objc
- (BOOL) sensorReader:(SRSensorReader *) reader fetchingRequest:(SRFetchRequest *) fetchRequest didFetchResult:(SRFetchResult *) result;
```

## Discussion

The framework expects the app to know the result’s type based on the reader’s sensor. To see a list of result types per sensor, see [Sample types](../srfetchresult/sample.md#Sample-types).

When a fetch produces multiple results, the framework invokes this callback once for each result.

To reuse a fetch result within the scope of this function, create a copy of `fetchResult` rather than assigning a strong reference to it.

## Parameters

- `reader`: The sensor reader for which the fetch provides results.
- `fetchRequest`: The completed fetch request.
- `result`: The fetch request’s result.

## See Also

### Reading Recorded Data
- [func sensorReader(SRSensorReader, didCompleteFetch: SRFetchRequest)](./sensorreader%28_,didcompletefetch%29.md)
  Provides the delegate with a completed fetch request.
- [func sensorReader(SRSensorReader, fetching: SRFetchRequest, failedWithError: any Error)](./sensorreader%28_,fetching,failedwitherror%29.md)
  Provides the delegate with a fetch failure reason.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:fetching:didfetchresult:))*