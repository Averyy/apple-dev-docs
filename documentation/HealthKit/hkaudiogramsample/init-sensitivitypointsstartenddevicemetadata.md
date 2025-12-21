# init(sensitivityPoints:start:end:device:metadata:)

**Framework**: HealthKit  
**Kind**: init

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- Mac Catalyst 18.1+
- macOS 15.1+
- visionOS 2.1+
- watchOS 11.1+

## Declaration

```swift
convenience init(sensitivityPoints: [HKAudiogramSensitivityPoint], start startDate: Date, end endDate: Date, device: HKDevice?, metadata: [String : Any]?)
```

#### Return Value

A new instance of an audiogram sample.

#### Discussion

Creates a new audiogram sample with the specified attributes.

## Parameters

- `sensitivityPoints`: Sensitivity data associated with the sample, with a maximum limit of 30 points. Frequencies must be unique, and ordered ascending.
- `startDate`: The start date of the hearing test.
- `endDate`: The end date of the hearing test.
- `device`: The device that generated the sample data.
- `metadata`: Optional metadata associated with the sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkaudiogramsample/init(sensitivitypoints:start:end:device:metadata:))*