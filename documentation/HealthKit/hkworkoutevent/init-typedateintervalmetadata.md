# init(type:dateInterval:metadata:)

**Framework**: HealthKit  
**Kind**: init

Instantiates and returns a new workout event with the specified type, date interval, and metadata.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
convenience init(type: HKWorkoutEventType, dateInterval: DateInterval, metadata: [String : Any]?)
```

#### Return Value

A new workout event.

## Parameters

- `type`: The type of workout event. For a description of possible events, see [`HKWorkoutEventType`](hkworkouteventtype.md).
- `dateInterval`: Most event types support only date intervals with a zero-length duration. These intervals indicate a single point in time, represented by the interval’s [`startDate`](https://developer.apple.com/documentation/foundation/nsdateinterval/startdate) property. Only [`HKWorkoutEventType.lap`](hkworkouteventtype/lap.md) and [`HKWorkoutEventType.segment`](hkworkouteventtype/segment.md) event types support intervals with nonzero durations.
- `metadata`: The metadata associated with the workout event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutevent/init(type:dateinterval:metadata:))*