# JournalingSuggestion.Workout.Details

**Framework**: Journaling Suggestions  
**Kind**: struct

Information about a workout that a person completes.

**Availability**:
- iOS 17.2+

## Declaration

```swift
struct Details
```

#### Overview

Each [`JournalingSuggestion.Workout`](journalingsuggestion/workout.md) contains an instance of this structure with its [`details`](journalingsuggestion/workout/details-swift.property.md) property.

## Topics

### Instance Properties
- [var activeEnergyBurned: HKQuantity?](journalingsuggestion/workout/details-swift.struct/activeenergyburned.md)
  The energy that a person burns during the workout.
- [var activityType: HKWorkoutActivityType](journalingsuggestion/workout/details-swift.struct/activitytype.md)
  The type of workout.
- [var averageHeartRate: HKQuantity?](journalingsuggestion/workout/details-swift.struct/averageheartrate.md)
  The average heart rate that a person experiences during the workout.
- [var date: DateInterval?](journalingsuggestion/workout/details-swift.struct/date.md)
  The range of time in which the workout takes place.
- [var distance: HKQuantity?](journalingsuggestion/workout/details-swift.struct/distance.md)
  The distance that the workout spans.
- [var localizedName: String?](journalingsuggestion/workout/details-swift.struct/localizedname.md)
  Localized name of workout, like “Indoor Pickleball”.

## Relationships

### Conforms To
- [JournalingSuggestionAsset](journalingsuggestionasset.md)

## See Also

- [var details: JournalingSuggestion.Workout.Details?](journalingsuggestion/workout/details-swift.property.md)
  A structure that contains the workout specifics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestion/workout/details-swift.struct)*