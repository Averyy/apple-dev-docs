# JournalingSuggestion.MotionActivity

**Framework**: Journaling Suggestions  
**Kind**: struct

A suggestion that describes motion activity, including the number of steps a person takes.

**Availability**:
- iOS 17.2+

## Declaration

```swift
struct MotionActivity
```

## Mentions

- [Presenting the suggestions picker and processing a selection](presenting-the-suggestions-picker-and-processing-a-selection.md)

#### Overview

The system provides an instance of this structure to your app when a person chooses a motion suggestion in the [`JournalingSuggestionsPicker`](journalingsuggestionspicker.md).

## Topics

### Accessing motion summary information
- [var icon: URL?](journalingsuggestion/motionactivity/icon.md)
  The URL to an image on disk that depicts the motion activity.
- [var date: DateInterval?](journalingsuggestion/motionactivity/date.md)
  The range of time in which the motion activity takes place.
### Inspecting motion details
- [var steps: Int](journalingsuggestion/motionactivity/steps.md)
  The number of steps a person takes.
- [JournalingSuggestion.MotionActivity.MovementType](journalingsuggestion/motionactivity/movementtype-swift.struct.md)
  The movement activity type that the phone records when it detects motion.
- [var movementType: JournalingSuggestion.MotionActivity.MovementType?](journalingsuggestion/motionactivity/movementtype-swift.property.md)
  The specific type of movement associated with the activity.

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
- [JournalingSuggestion.WorkoutGroup](journalingsuggestion/workoutgroup.md)
  A suggestion that contains multiple workouts that a person chooses in the picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestion/motionactivity)*