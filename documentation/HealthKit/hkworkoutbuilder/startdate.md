# startDate

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The workout’s start date and time.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var startDate: Date? { get }
```

```objc
@property (copy, readonly, nullable) NSDate * startDate;
```

## See Also

### Starting the workout
- [func beginCollection(withStart: Date, completion: (Bool, (any Error)?) -> Void)](./begincollection%28withstart,completion%29.md)
  Sets the workout’s start date and begins building the workout.
- [func elapsedTime(at: Date) -> TimeInterval](./elapsedtime%28at%29.md)
  Calculates the duration of the workout at the specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutbuilder/startdate)*