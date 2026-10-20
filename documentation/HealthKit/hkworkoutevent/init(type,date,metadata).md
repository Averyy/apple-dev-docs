# init(type:date:metadata:)

**Framework**: HealthKit  
**Kind**: init  
**Role**: Initializer

Instantiates and returns a new workout event with the specified type, date, and metadata.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 13.0+
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 4.0

> **Deprecated**: Use [`init(type:dateInterval:metadata:)`](./init%28type,dateinterval,metadata%29.md) instead.

## Declaration

```swift
convenience init(type: HKWorkoutEventType, date: Date, metadata: [String : Any])
```

```objc
+ (instancetype) workoutEventWithType:(HKWorkoutEventType) type date:(NSDate *) date metadata:(NSDictionary<NSString *,id> *) metadata;
```

## Parameters

- `type`: The type of workout event. For a description of possible events, see [`HKWorkoutEventType`](../hkworkouteventtype.md).
- `date`: The time when the transition occurred. For a pause event, this date indicates the start of the break. For a resume event, this date indicates the end of the break. You must use a date between the starting and ending dates of the workout that you intend to modify.
- `metadata`: The metadata associated with the workout event.

## See Also

### Deprecated
- [convenience init(type: HKWorkoutEventType, date: Date)](./init%28type,date%29.md)
  Instantiates and returns a new workout event with the specified type and date.
- [var date: Date](./date.md)
  The time when the transition occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutevent/init(type:date:metadata:))*