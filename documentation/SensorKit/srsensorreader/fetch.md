# fetch(_:)

**Framework**: SensorKit  
**Kind**: method

Fetches the samples that a fetch request specifies.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func fetch(_ request: SRFetchRequest)
```

#### Discussion

An app calls this function to access data for the caller’s sensor.

Upon success, the framework delivers results in the form of  via the delegate’s [`sensorReader(_:fetching:didFetchResult:)`](srsensorreaderdelegate/sensorreader(_:fetching:didfetchresult:).md) callback. The framework invokes the delegate multiple times if this function results in multiple samples.

The framework returns sensor data only for the argument fetch-object’s device, and that’s dated only within the argument fetch-object’s time window. Within that window, this function returns only the data that the framework recorded (see [`startRecording()`](srsensorreader/startrecording().md)), and that the framework hasn’t deleted (see [`SRDeletionRecord`](srdeletionrecord.md)).

## Parameters

- `request`: An object that describes the device from which to retrieve samples, and samaple age of interest.

## See Also

- [func fetchDevices()](srsensorreader/fetchdevices.md)
  Acquires device information for all devices that store data for this reader’s sensor.
- [class SRDevice](srdevice.md)
  A representation of a device that provides sample data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensorreader/fetch(_:))*