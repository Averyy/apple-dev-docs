# init(id:stationName:programName:type:duration:artwork:animatedArtwork:)

**Framework**: Now Playing  
**Kind**: init

Creates radio station content with static and animated artwork.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
init(id: String, stationName: String, programName: String? = nil, type: MediaType = .audio, duration: MediaDuration? = .live, artwork: Artwork, animatedArtwork: AnimatedArtwork?)
```

## Parameters

- `id`: A unique identifier for this station.
- `stationName`: The display name of the station.
- `programName`: The current program or show, if available.
- `type`: The media type. Defaults to `.audio`.
- `duration`: The duration of the content. Defaults to `.live` for continuous broadcasts.
- `artwork`: Static artwork for the station.
- `animatedArtwork`: Animated artwork for the station, or `nil` when unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/radiocontent/init(id:stationname:programname:type:duration:artwork:animatedartwork:))*