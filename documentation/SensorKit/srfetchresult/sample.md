# sample

**Framework**: SensorKit  
**Kind**: property

A recording that the sensor reader fetches.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@NSCopying
var sample: SampleType { get }
```

#### Discussion

The framework expects the app to know the result type based on the reader’s sensor.

##### Sample Types

This property’s type is a superclass from which the framework derives discrete sample types. Depending on the sensor associated with your app’s sensor reader, type cast the fetch result’s [`sample`](srfetchresult/sample.md) to the sensor’s associated sample type. The following list provides the sample type per sensor:

## See Also

- [var timestamp: SRAbsoluteTime](srfetchresult/timestamp.md)
  The time when the framework records the sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srfetchresult/sample)*