# dateInterval

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, readonly) NSDateInterval * dateInterval;
```

## Discussion

Most event types support only date intervals with a zero-length duration. These intervals indicate a single point in time, represented by the interval’s [`startDate`](../../Foundation/nsdateinterval/startdate.md) property. Only [`HKWorkoutEventType.lap`](../hkworkouteventtype/lap.md) and [`HKWorkoutEventType.segment`](../hkworkouteventtype/segment.md) event types support intervals with nonzero durations.

## See Also

### Getting property data
- [var type: HKWorkoutEventType](./type.md)
  The type of workout event.
- [var metadata: [String : Any]?](./metadata.md)
  The metadata associated with the workout event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutevent/dateinterval)*