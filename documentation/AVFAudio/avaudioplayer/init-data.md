# init(data:)

**Framework**: AVFAudio  
**Kind**: init

Creates a player to play in-memory audio data.

**Availability**:
- iOS 2.2+
- iPadOS 2.2+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
init(data: Data) throws
```

#### Return Value

A new audio player instance, or [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0) if an error occurs.

#### Discussion

The audio data must be in a format that Core Audio supports.

## Parameters

- `data`: A buffer with the audio data to play.

## See Also

- [init(contentsOf: URL) throws](avaudioplayer/init(contentsof:).md)
  Creates a player to play audio from a file.
- [init(contentsOf: URL, fileTypeHint: String?) throws](avaudioplayer/init(contentsof:filetypehint:).md)
  Creates a player to play audio from a file of a particular type.
- [init(data: Data, fileTypeHint: String?) throws](avaudioplayer/init(data:filetypehint:).md)
  Creates a player to play in-memory audio data of a particular type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayer/init(data:))*