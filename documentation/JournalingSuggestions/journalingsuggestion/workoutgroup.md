# JournalingSuggestion.WorkoutGroup

**Framework**: Journaling Suggestions  
**Kind**: struct

A suggestion that contains multiple workouts that a person chooses in the picker.

**Availability**:
- iOS 17.2+

## Declaration

```swift
struct WorkoutGroup
```

#### Overview

The system provides an instance of this structure to your app when a person chooses multiple workout suggestions in the [`JournalingSuggestionsPicker`](journalingsuggestionspicker.md).

## Topics

### Accessing workout summary information
- [var icon: URL?](journalingsuggestion/workoutgroup/icon.md)
  The URL to an image on disc that represents the types of completed workout.
- [var duration: TimeInterval?](journalingsuggestion/workoutgroup/duration.md)
  The amount of time the workouts span.
- [var activeEnergyBurned: HKQuantity?](journalingsuggestion/workoutgroup/activeenergyburned.md)
  The total energy that the person burns over the workouts.
- [var averageHeartRate: HKQuantity?](journalingsuggestion/workoutgroup/averageheartrate.md)
  The average heart rate that the person experiences during the workouts.
### Accessing individual workouts
- [var workouts: [JournalingSuggestion.Workout]](journalingsuggestion/workoutgroup/workouts.md)
  An array of workout suggestions that a person chooses in the picker.
### Type Aliases
- [JournalingSuggestion.WorkoutGroup.JournalingSuggestionContent](journalingsuggestion/workoutgroup/journalingsuggestioncontent.md)
  Represents a generic content type for journaling suggestions.

## Relationships

### Conforms To
- [JournalingSuggestionAsset](journalingsuggestionasset.md)

## See Also

- [JournalingSuggestion.Contact](journalingsuggestion/contact.md)
  A suggestion for a connection a person makes with someone else.
- [JournalingSuggestion.EventPoster](journalingsuggestion/eventposter.md)
  A suggestion for a poster image of an event.
- [JournalingSuggestion.GenericMedia](journalingsuggestion/genericmedia.md)
  A suggestion describing now playable media that a person listened to.
- [JournalingSuggestion.LivePhoto](journalingsuggestion/livephoto.md)
  A suggestion for a Live Photo from a person’s library.
- [JournalingSuggestion.Location](journalingsuggestion/location.md)
  A suggestion that represents a location that a person visits.
- [JournalingSuggestion.LocationGroup](journalingsuggestion/locationgroup.md)
  A suggestion that contains multiple visited locations that a person chooses in the picker.
- [JournalingSuggestion.MotionActivity](journalingsuggestion/motionactivity.md)
  A suggestion that describes motion activity, including the number of steps a person takes.
- [JournalingSuggestion.Photo](journalingsuggestion/photo.md)
  A suggestion for a photo from a person’s library.
- [JournalingSuggestion.Podcast](journalingsuggestion/podcast.md)
  A suggestion that describes a podcast episode a person listened to.
- [JournalingSuggestion.Reflection](journalingsuggestion/reflection.md)
  A suggestion for a reflection prompt.
- [JournalingSuggestion.StateOfMind](journalingsuggestion/stateofmind.md)
  A suggestion that describes a state of mind reflection in the Health app.
- [JournalingSuggestion.Song](journalingsuggestion/song.md)
  A suggestion for a song from a person’s music library.
- [JournalingSuggestion.Video](journalingsuggestion/video.md)
  A suggestion for a video from a person’s library.
- [JournalingSuggestion.Workout](journalingsuggestion/workout.md)
  A suggestion that describes a workout that a person completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestion/workoutgroup)*