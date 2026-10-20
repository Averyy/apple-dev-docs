# sensorReader(_:fetching:failedWithError:)

**Framework**: SensorKit  
**Kind**: method  
**Role**: Instance Method

Provides the delegate with a fetch failure reason.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0

> **Deprecated**: Use SRReader<Sensor> class

## Declaration

```swift
optional func sensorReader(_ reader: SRSensorReader, fetching fetchRequest: SRFetchRequest, failedWithError error: any Error)
```

```objc
- (void) sensorReader:(SRSensorReader *) reader fetchingRequest:(SRFetchRequest *) fetchRequest failedWithError:(NSError *) error;
```

## Parameters

- `reader`: The sensor reader for which the fetch failed.
- `fetchRequest`: The original fetch request.
- `error`: An object that describes the cause of failure.

## See Also

### Reading Recorded Data
- [func sensorReader(SRSensorReader, fetching: SRFetchRequest, didFetchResult: SRFetchResult<AnyObject>) -> Bool](./sensorreader%28_,fetching,didfetchresult%29.md)
  Provides the delegate with a fetch result.
- [func sensorReader(SRSensorReader, didCompleteFetch: SRFetchRequest)](./sensorreader%28_,didcompletefetch%29.md)
  Provides the delegate with a completed fetch request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:fetching:failedwitherror:))*