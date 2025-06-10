# elapsedTime(at:)

**Framework**: HealthKit  
**Kind**: method

Calculates the duration of the workout at the specified time.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS ?+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func elapsedTime(at date: Date) -> TimeInterval
```

#### Discussion

The duration of a workout doesn’t include intervals between pause and resume events.

> **Note**:  The duration of a workout can decrease when you add past occurrences of pause events.

## Parameters

- `date`: The end date to use to calculate the duration.

## See Also

- [func beginCollection(withStart: Date, completion: (Bool, (any Error)?) -> Void)](hkworkoutbuilder/begincollection(withstart:completion:).md)
  Sets the workout’s start date and begins building the workout.
- [var startDate: Date?](hkworkoutbuilder/startdate.md)
  The workout’s start date and time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutbuilder/elapsedtime(at:))*