# JournalingSuggestion.Workout

**Framework**: Journaling Suggestions  
**Kind**: struct

A suggestion that describes a workout that a person completed.

**Availability**:
- iOS 17.2+

## Declaration

```swift
struct Workout
```

## Mentions

- [Presenting the suggestions picker and processing a selection](presenting-the-suggestions-picker-and-processing-a-selection.md)

#### Overview

The system provides an instance of this structure to your app when a person chooses a workout suggestion in the [`JournalingSuggestionsPicker`](journalingsuggestionspicker.md).

## Topics

### Accessing workout summary information
- [var icon: URL?](journalingsuggestion/workout/icon.md)
  The URL to an image on disc that represents the type of workout.
- [var route: [CLLocation]?](journalingsuggestion/workout/route.md)
  The geographic path that a person travels over the course of the workout.
### Inspecting workout details
- [var details: JournalingSuggestion.Workout.Details?](journalingsuggestion/workout/details-swift.property.md)
  A structure that contains the workout specifics.
- [JournalingSuggestion.Workout.Details](journalingsuggestion/workout/details-swift.struct.md)
  Information about a workout that a person completes.
### Type Aliases
- [JournalingSuggestion.Workout.JournalingSuggestionContent](journalingsuggestion/workout/journalingsuggestioncontent.md)
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
- [JournalingSuggestion.WorkoutGroup](journalingsuggestion/workoutgroup.md)
  A suggestion that contains multiple workouts that a person chooses in the picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestion/workout)*