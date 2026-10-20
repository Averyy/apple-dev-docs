# sensorReader(_:didCompleteFetch:)

**Framework**: SensorKit  
**Kind**: method  
**Role**: Instance Method

Provides the delegate with a completed fetch request.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0

> **Deprecated**: Use SRReader<Sensor> class

## Declaration

```swift
optional func sensorReader(_ reader: SRSensorReader, didCompleteFetch fetchRequest: SRFetchRequest)
```

```objc
- (void) sensorReader:(SRSensorReader *) reader didCompleteFetch:(SRFetchRequest *) fetchRequest;
```

## Parameters

- `reader`: The reader that completed the fetch request.
- `fetchRequest`: The completed fetch request.

## See Also

### Reading Recorded Data
- [func sensorReader(SRSensorReader, fetching: SRFetchRequest, didFetchResult: SRFetchResult<AnyObject>) -> Bool](./sensorreader%28_,fetching,didfetchresult%29.md)
  Provides the delegate with a fetch result.
- [func sensorReader(SRSensorReader, fetching: SRFetchRequest, failedWithError: any Error)](./sensorreader%28_,fetching,failedwitherror%29.md)
  Provides the delegate with a fetch failure reason.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:didcompletefetch:))*