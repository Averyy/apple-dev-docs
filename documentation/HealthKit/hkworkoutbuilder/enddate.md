# endDate

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The workout’s end date and time.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var endDate: Date? { get }
```

```objc
@property (copy, readonly, nullable) NSDate * endDate;
```

## See Also

### Ending the workout
- [func endCollection(withEnd: Date, completion: (Bool, (any Error)?) -> Void)](./endcollection%28withend,completion%29.md)
  Stops the collection of data, sets the workout’s end date, and deactivates the workout builder.
- [func finishWorkout(completion: (HKWorkout?, (any Error)?) -> Void)](./finishworkout%28completion%29.md)
  Creates the workout, using the samples and events added to the builder, and saves it to the HealthKit store.
- [func discardWorkout()](./discardworkout%28%29.md)
  Stops the collection of data and discards the current results without saving the workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutbuilder/enddate)*