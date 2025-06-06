# init(type:date:)

**Framework**: HealthKit  
**Kind**: init

Instantiates and returns a new workout event with the specified type and date.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init(type: HKWorkoutEventType, date: Date)
```

#### Return Value

A new workout event.

## Parameters

- `type`: The type of workout event. For a description of possible events, see  .
- `date`: The time when the transition occurred. For a pause event, this date indicates the start of the break. For a resume event, this date indicates the end of the break. You must use a date between the starting and ending dates of the workout that you intend to modify.

## See Also

- [convenience init(type: HKWorkoutEventType, date: Date, metadata: [String : Any])](hkworkoutevent/init(type:date:metadata:).md)
  Instantiates and returns a new workout event with the specified type, date, and metadata.
- [var date: Date](hkworkoutevent/date.md)
  The time when the transition occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutevent/init(type:date:))*