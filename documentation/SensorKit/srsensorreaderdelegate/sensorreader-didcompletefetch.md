# sensorReader(_:didCompleteFetch:)

**Framework**: SensorKit  
**Kind**: method

Provides the delegate with a completed fetch request.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
optional func sensorReader(_ reader: SRSensorReader, didCompleteFetch fetchRequest: SRFetchRequest)
```

## Parameters

- `reader`: The reader that completed the fetch request.
- `fetchRequest`: The completed fetch request.

## See Also

- [func sensorReader(SRSensorReader, fetching: SRFetchRequest, didFetchResult: SRFetchResult<AnyObject>) -> Bool](srsensorreaderdelegate/sensorreader(_:fetching:didfetchresult:).md)
  Provides the delegate with a fetch result.
- [func sensorReader(SRSensorReader, fetching: SRFetchRequest, failedWithError: any Error)](srsensorreaderdelegate/sensorreader(_:fetching:failedwitherror:).md)
  Provides the delegate with a fetch failure reason.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:didcompletefetch:))*