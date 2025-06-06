# JournalingSuggestion.GenericMedia

**Framework**: Journaling Suggestions  
**Kind**: struct

A suggestion describing now playable media that a person listened to.

**Availability**:
- iOS 18.0+

## Declaration

```swift
struct GenericMedia
```

## Mentions

- [Presenting the suggestions picker and processing a selection](presenting-the-suggestions-picker-and-processing-a-selection.md)

#### Overview

The system provides an instance of this structure to your app when a person chooses a media suggestion in the [`JournalingSuggestionsPicker`](journalingsuggestionspicker.md). To exclude the Now Playing item from content suggestions, refer to [`mpnowplayinginfopropertyexcludefromsuggestions`](https://developer.apple.comhttps://developer.apple.com/documentation/mediaplayer/mpnowplayinginfopropertyexcludefromsuggestions).

## Topics

### Accessing media data
- [var album: String?](journalingsuggestion/genericmedia/album.md)
  The name of the album that contains the media item.
- [var appIcon: URL?](journalingsuggestion/genericmedia/appicon.md)
  The URL to an image on disk for the Now Playing app that played the media item.
- [var artist: String?](journalingsuggestion/genericmedia/artist.md)
  The performing artists for a media item.
- [var date: Date?](journalingsuggestion/genericmedia/date.md)
  The media item’s playback date.
- [var title: String?](journalingsuggestion/genericmedia/title.md)
  The title or name of a media item.
### Type Aliases
- [JournalingSuggestion.GenericMedia.JournalingSuggestionContent](journalingsuggestion/genericmedia/journalingsuggestioncontent.md)
  Represents a generic content type for journaling suggestions.

## Relationships

### Conforms To
- [JournalingSuggestionAsset](journalingsuggestionasset.md)

## See Also

- [JournalingSuggestion.Contact](journalingsuggestion/contact.md)
  A suggestion for a connection a person makes with someone else.
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

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestion/genericmedia)*