# init(contentsOf:fileTypeHint:)

**Framework**: AVFAudio  
**Kind**: init

Creates a player to play audio from a file of a particular type.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(contentsOf url: URL, fileTypeHint utiString: String?) throws
```

#### Return Value

A new audio player instance, or [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0) if there is an error.

#### Discussion

The audio data must be in a format that Core Audio supports. Passing a file type hint helps the system parse the data if it can’t determine the file type or if the data is corrupt. See [`AVFileType`](https://developer.apple.com/documentation/AVFoundation/AVFileType) for supported values.

## Parameters

- `url`: A URL that identifies the local audio file to play.
- `utiString`: The uniform type identifier (UTI) string of the file format.

## See Also

- [init(contentsOf: URL) throws](avaudioplayer/init(contentsof:).md)
  Creates a player to play audio from a file.
- [init(data: Data) throws](avaudioplayer/init(data:).md)
  Creates a player to play in-memory audio data.
- [init(data: Data, fileTypeHint: String?) throws](avaudioplayer/init(data:filetypehint:).md)
  Creates a player to play in-memory audio data of a particular type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayer/init(contentsof:filetypehint:))*