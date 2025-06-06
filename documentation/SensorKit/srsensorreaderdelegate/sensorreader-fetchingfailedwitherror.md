# sensorReader(_:fetching:failedWithError:)

**Framework**: SensorKit  
**Kind**: method

Provides the delegate with a fetch failure reason.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
optional func sensorReader(_ reader: SRSensorReader, fetching fetchRequest: SRFetchRequest, failedWithError error: any Error)
```

## Parameters

- `reader`: The sensor reader for which the fetch failed.
- `fetchRequest`: The original fetch request.
- `error`: An object that describes the cause of failure.

## See Also

- [func sensorReader(SRSensorReader, fetching: SRFetchRequest, didFetchResult: SRFetchResult<AnyObject>) -> Bool](srsensorreaderdelegate/sensorreader(_:fetching:didfetchresult:).md)
  Provides the delegate with a fetch result.
- [func sensorReader(SRSensorReader, didCompleteFetch: SRFetchRequest)](srsensorreaderdelegate/sensorreader(_:didcompletefetch:).md)
  Provides the delegate with a completed fetch request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:fetching:failedwitherror:))*