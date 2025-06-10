# sr_sensorForDeletionRecordsFromSensor()

**Framework**: Foundation  
**Kind**: method

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func sr_sensorForDeletionRecordsFromSensor() -> SRSensor?
```

#### Return Value

May return nil if there is no deletion record available for this sensor

#### Discussion

This sensor stream should only be used for fetching. All other operations will be ignored. Deletion records share the recording and authorization state with their parent sensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/sr_sensorfordeletionrecordsfromsensor())*