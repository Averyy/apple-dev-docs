# init(id:stationName:programName:type:duration:artwork:animatedArtwork:)

**Framework**: Now Playing  
**Kind**: init

Creates radio station content with static and animated artwork.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

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