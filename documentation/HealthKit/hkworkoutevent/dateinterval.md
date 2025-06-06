# dateInterval

**Framework**: HealthKit  
**Kind**: property

The time and duration of the event.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var dateInterval: DateInterval { get }
```

#### Discussion

Most event types support only date intervals with a zero-length duration. These intervals indicate a single point in time, represented by the interval’s [`startDate`](https://developer.apple.com/documentation/foundation/nsdateinterval/1641656-startdate) property. Only [`HKWorkoutEventType.lap`](hkworkouteventtype/lap.md) and [`HKWorkoutEventType.segment`](hkworkouteventtype/segment.md) event types support intervals with nonzero durations.

## See Also

- [var type: HKWorkoutEventType](hkworkoutevent/type.md)
  The type of workout event.
- [var metadata: [String : Any]?](hkworkoutevent/metadata.md)
  The metadata associated with the workout event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutevent/dateinterval)*