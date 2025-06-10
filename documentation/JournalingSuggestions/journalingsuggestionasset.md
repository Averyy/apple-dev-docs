# JournalingSuggestionAsset

**Framework**: Journaling Suggestions  
**Kind**: protocol

An interface for the content that the suggestions picker presents.

**Availability**:
- iOS 17.2+

## Declaration

```swift
protocol JournalingSuggestionAsset
```

## Mentions

- [Presenting the suggestions picker and processing a selection](presenting-the-suggestions-picker-and-processing-a-selection.md)

#### Overview

When a person makes a selection in a [`JournalingSuggestionsPicker`](journalingsuggestionspicker.md), the system invokes the picker’s `onCompletion` closure, and passes in the selected suggestion ([`JournalingSuggestion`](journalingsuggestion.md)). Each item in the suggestion’s [`items`](journalingsuggestion/items.md) array conforms to this protocol.

## Topics

### Associated Types
- [associatedtype JournalingSuggestionContent : JournalingSuggestionAsset = Self](journalingsuggestionasset/journalingsuggestioncontent.md)
  Represents a generic content type for journaling suggestions.

## Relationships

### Conforming Types
- [JournalingSuggestion.Contact](journalingsuggestion/contact.md)
- [JournalingSuggestion.EventPoster](journalingsuggestion/eventposter.md)
- [JournalingSuggestion.GenericMedia](journalingsuggestion/genericmedia.md)
- [JournalingSuggestion.LivePhoto](journalingsuggestion/livephoto.md)
- [JournalingSuggestion.Location](journalingsuggestion/location.md)
- [JournalingSuggestion.LocationGroup](journalingsuggestion/locationgroup.md)
- [JournalingSuggestion.MotionActivity](journalingsuggestion/motionactivity.md)
- [JournalingSuggestion.Photo](journalingsuggestion/photo.md)
- [JournalingSuggestion.Podcast](journalingsuggestion/podcast.md)
- [JournalingSuggestion.Reflection](journalingsuggestion/reflection.md)
- [JournalingSuggestion.Song](journalingsuggestion/song.md)
- [JournalingSuggestion.StateOfMind](journalingsuggestion/stateofmind.md)
- [JournalingSuggestion.Video](journalingsuggestion/video.md)
- [JournalingSuggestion.Workout](journalingsuggestion/workout.md)
- [JournalingSuggestion.Workout.Details](journalingsuggestion/workout/details-swift.struct.md)
- [JournalingSuggestion.WorkoutGroup](journalingsuggestion/workoutgroup.md)

## See Also

- [struct JournalingSuggestionsPicker](journalingsuggestionspicker.md)
  A view that lists different types of recent events in a person’s life.
- [struct JournalingSuggestion](journalingsuggestion.md)
  High-level information about a suggestion that a person chooses in the journaling suggestions picker.
- [class JournalingSuggestionsConfiguration](journalingsuggestionsconfiguration.md)
  The scheduled configuration settings for your app.
- [struct JournalingSuggestionPresentationToken](journalingsuggestionpresentationtoken.md)
  A token you use to modify the content of the presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionasset)*