# JournalingSuggestion.EventPoster

**Framework**: Journaling Suggestions  
**Kind**: struct

A suggestion for a poster image of an event.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct EventPoster
```

## Mentions

- [Presenting the suggestions picker and processing a selection](presenting-the-suggestions-picker-and-processing-a-selection.md)

#### Overview

The system provides a `EventPoster` value to your app when a person chooses a suggestion with a event poster

## Topics

### Identifying an event
- [var title: AttributedString](journalingsuggestion/eventposter/title.md)
  The title of the event.
- [var placeName: String?](journalingsuggestion/eventposter/placename.md)
  Location displayed name on the poster.
- [var image: URL?](journalingsuggestion/eventposter/image.md)
  A poster image URL.
### Reviewing event dates
- [var eventEnd: Date?](journalingsuggestion/eventposter/eventend.md)
  The end date of the event.
- [var eventStart: Date?](journalingsuggestion/eventposter/eventstart.md)
  The start date of the event.
### Distinguishing the organizer
- [var isHost: Bool?](journalingsuggestion/eventposter/ishost.md)
  Boolean whether the user is the host of the event.

## Relationships

### Conforms To
- [JournalingSuggestionAsset](journalingsuggestionasset.md)

## See Also

- [JournalingSuggestion.Contact](journalingsuggestion/contact.md)
  A suggestion for a connection a person makes with someone else.
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
- [JournalingSuggestion.WorkoutGroup](journalingsuggestion/workoutgroup.md)
  A suggestion that contains multiple workouts that a person chooses in the picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestion/eventposter)*