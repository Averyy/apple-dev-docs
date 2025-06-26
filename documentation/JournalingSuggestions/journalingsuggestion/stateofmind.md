# JournalingSuggestion.StateOfMind

**Framework**: Journaling Suggestions  
**Kind**: struct

A suggestion that describes a state of mind reflection in the Health app.

**Availability**:
- iOS 18.0+

## Declaration

```swift
struct StateOfMind
```

## Mentions

- [Presenting the suggestions picker and processing a selection](presenting-the-suggestions-picker-and-processing-a-selection.md)

#### Overview

The system provides an instance of this structure to your app when a person chooses a state of mind suggestion in the [`JournalingSuggestionsPicker`](journalingsuggestionspicker.md).

## Topics

### Getting the state of mind data
- [var darkBackground: Gradient?](journalingsuggestion/stateofmind/darkbackground.md)
  The icon dark background color gradients.
- [var lightBackground: Gradient?](journalingsuggestion/stateofmind/lightbackground.md)
  The icon light background color gradients.
- [var icon: URL?](journalingsuggestion/stateofmind/icon.md)
  The URL to an image on disk that depicts the state of mind reflection valence image.
- [var state: HKStateOfMind](journalingsuggestion/stateofmind/state.md)
  The state of mind reflection as logged in the Health app.
### Type Aliases
- [JournalingSuggestion.StateOfMind.JournalingSuggestionContent](journalingsuggestion/stateofmind/journalingsuggestioncontent.md)
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
- [JournalingSuggestion.Song](journalingsuggestion/song.md)
  A suggestion for a song from a person’s music library.
- [JournalingSuggestion.Video](journalingsuggestion/video.md)
  A suggestion for a video from a person’s library.
- [JournalingSuggestion.Workout](journalingsuggestion/workout.md)
  A suggestion that describes a workout that a person completed.
- [JournalingSuggestion.WorkoutGroup](journalingsuggestion/workoutgroup.md)
  A suggestion that contains multiple workouts that a person chooses in the picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestion/stateofmind)*