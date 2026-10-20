# date

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The time when the transition occurred.

**Availability**:
- iOS 8.0+ - Deprecated in 11.0
- iPadOS 8.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 13.0+
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 4.0

> **Deprecated**: Use [`dateInterval`](./dateinterval.md) instead.

## Declaration

```swift
var date: Date { get }
```

```objc
@property (copy, readonly) NSDate * date;
```

#### Discussion

For a pause event, this date indicates the start of the break. For a resume event, this date indicates the end of the break. You must use a date between the starting and ending dates of the workout that you intend to modify.

## See Also

### Deprecated
- [convenience init(type: HKWorkoutEventType, date: Date)](./init%28type,date%29.md)
  Instantiates and returns a new workout event with the specified type and date.
- [convenience init(type: HKWorkoutEventType, date: Date, metadata: [String : Any])](./init%28type,date,metadata%29.md)
  Instantiates and returns a new workout event with the specified type, date, and metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutevent/date)*