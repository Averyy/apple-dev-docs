# Stations.Attributes

**Framework**: Apple Music API  
**Kind**: dictionary

The attributes for a station resource.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object Stations.Attributes
```

## Properties

- `artwork` (Artwork) *(required)*: The radio station artwork.
- `durationInMillis` (integer): The duration of the stream. This value isn’t emitted for ‘live’ or programmed stations.
- `editorialNotes` (EditorialNotes): The notes about the station that appear in Apple Music.
- `episodeNumber` (string): The episode number of the station. This value appears when the station represents an episode of a show or other content.
- `contentRating` (string): The rating of the content possibly heard while playing the station. The possible values for this rating are `clean` and `explicit`. No value means no rating.
- `isLive` (boolean) *(required)*: Indicates whether the station is a livestream.
- `mediaKind` (string) *(required)*: The media kind for the station. It can have value `audio` or `video` depending on whether it has video stream or audio stream.
- `name` (string) *(required)*: The localized name of the station.
- `playParams` (PlayParameters): When present, this attribute indicates that the radio station or episode is available to play with an Apple Music subscription. The value map may be used to initiate playback of the station. Live radio stations and episodes initiate streaming playback. Track-based stations initiate playback of individual tracks.
- `stationProviderName` (string): The name of the entity that provided the station, when specified.
- `url` (string) *(required)*: The URL for sharing the station in Apple Music.

## See Also

- [object Stations.Relationships](stations/relationships-data.dictionary.md)
  The name of the relationship you want to fetch for this resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/stations/attributes-data.dictionary)*