# sr_sensorForDeletionRecordsFromSensor()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 14.0+ - Deprecated in 27.0
- iPadOS 14.0+ - Deprecated in 27.0
- Mac Catalyst 14.0+ - Deprecated in 27.0

> **Deprecated**: Use deletionRecords(matching request: SRFetchRequest) of SRReader<Sensor> class

## Declaration

```swift
func sr_sensorForDeletionRecordsFromSensor() -> SRSensor?
```

```objc
- (SRSensor) sr_sensorForDeletionRecordsFromSensor;
```

#### Return Value

May return nil if there is no deletion record available for this sensor

#### Discussion

Returns a sensor stream that contains deletion records of the sensor

This sensor stream should only be used for fetching. All other operations will be ignored. Deletion records share the recording and authorization state with their parent sensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/sr_sensorfordeletionrecordsfromsensor())*