# date

**Framework**: HealthKit  
**Kind**: property

The time when the transition occurred.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var date: Date { get }
```

#### Discussion

For a pause event, this date indicates the start of the break. For a resume event, this date indicates the end of the break. You must use a date between the starting and ending dates of the workout that you intend to modify.

## See Also

- [convenience init(type: HKWorkoutEventType, date: Date)](hkworkoutevent/init(type:date:).md)
  Instantiates and returns a new workout event with the specified type and date.
- [convenience init(type: HKWorkoutEventType, date: Date, metadata: [String : Any])](hkworkoutevent/init(type:date:metadata:).md)
  Instantiates and returns a new workout event with the specified type, date, and metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutevent/date)*