# JournalingSuggestion

**Framework**: Journaling Suggestions  
**Kind**: struct

High-level information about a suggestion that a person chooses in the journaling suggestions picker.

**Availability**:
- iOS 17.2+

## Declaration

```swift
struct JournalingSuggestion
```

#### Overview

When a person chooses a particular suggestion in the [`JournalingSuggestionsPicker`](journalingsuggestionspicker.md), the system provides your app with more information about the event by passing an instance of this structure to your picker’s `onCompletion` handler.

## Topics

### Inspecting suggestion details
- [let date: DateInterval?](journalingsuggestion/date.md)
  The range of time in which the suggested event takes place.
- [let title: String](journalingsuggestion/title.md)
  The title for the suggestion.
### Accessing suggestion data by type
- [let items: [JournalingSuggestion.ItemContent]](journalingsuggestion/items.md)
  The individual items that compose the suggestion’s content.
- [JournalingSuggestion.ItemContent](journalingsuggestion/itemcontent.md)
  A container for the information about a specific suggestion.
- [func content<Content>(forType: Content.Type) async -> [Content]](journalingsuggestion/content(fortype:).md)
  Searches a suggestion’s items for information of the given type.
### Interacting with suggestion types
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
### Instance Properties
- [var hashValue: Int](journalingsuggestion/hashvalue.md)
  The hash value.
### Default Implementations
- [Equatable Implementations](journalingsuggestion/equatable-implementations.md)
- [Hashable Implementations](journalingsuggestion/hashable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [struct JournalingSuggestionsPicker](journalingsuggestionspicker.md)
  A view that lists different types of recent events in a person’s life.
- [protocol JournalingSuggestionAsset](journalingsuggestionasset.md)
  An interface for the content that the suggestions picker presents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestion)*