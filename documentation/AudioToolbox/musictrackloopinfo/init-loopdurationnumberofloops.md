# init(loopDuration:numberOfLoops:)

**Framework**: Audio Toolbox  
**Kind**: init

Initializes the music track loop information.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
init(loopDuration: MusicTimeStamp, numberOfLoops: Int32)
```

## Parameters

- `loopDuration`: The point in a music track, measured in beats from the end of the music track, at which to begin playback during looped playback. To explicitly turn off looping, specify a loopDuration of  .
- `numberOfLoops`: The number of times to play the designated portion of the music track. To loop forever, set numberOfLoops to  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/musictrackloopinfo/init(loopduration:numberofloops:))*