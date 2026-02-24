# init(sensitivityPoints:start:end:metadata:)

**Framework**: HealthKit  
**Kind**: init

Creates a new audiogram sample.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
convenience init(sensitivityPoints: [HKAudiogramSensitivityPoint], start startDate: Date, end endDate: Date, metadata: [String : Any]?)
```

## Parameters

- `sensitivityPoints`: An array of sensitivity points.
- `startDate`: The start date for the sample. This date must be equal to or earlier than the end date; otherwise, this method throws an exception ([`invalidArgumentException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/invalidArgumentException)).
- `endDate`: The end date for the sample. This date must be equal to or later than the start date; otherwise, this method throws an exception ([`invalidArgumentException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/invalidArgumentException)).
- `metadata`: The metadata dictionary contains extra information describing this sample. The dictionary’s keys are strings. The values may be strings, numbers, or dates. For a complete list of predefined metadata keys, see [`Metadata Keys`](metadata-keys.md). Using predefined keys helps facilitate sharing data between apps; however, you are also encouraged to create your own, custom keys as needed to extend the HealthKit quantity sample’s capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkaudiogramsample/init(sensitivitypoints:start:end:metadata:))*