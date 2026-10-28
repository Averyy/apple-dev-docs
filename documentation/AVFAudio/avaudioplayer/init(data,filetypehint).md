# init(data:fileTypeHint:)

**Framework**: AVFAudio  
**Kind**: init  
**Role**: Initializer

Creates a player to play in-memory audio data of a particular type.

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
init(data: Data, fileTypeHint utiString: String?) throws
```

```objc
- (instancetype) initWithData:(NSData *) data fileTypeHint:(NSString *) utiString error:(NSError **) outError;
```

## Return Value

A new audio player instance, or [`nil`](../../ObjectiveC/nil-227m0.md) if an error occurs.

## Discussion

The audio data must be in a format that Core Audio supports. Passing a file type hint helps the system parse the data if it can’t determine the file type or if the data is corrupt. See [`AVFileType`](../../AVFoundation/avfiletype.md) for supported values.

## Parameters

- `data`: A buffer with the audio data to play.
- `utiString`: The uniform type identifier (UTI) string of the file format.

## See Also

### Creating an audio player
- [init(contentsOf: URL) throws](./init%28contentsof%29.md)
  Creates a player to play audio from a file.
- [init(contentsOf: URL, fileTypeHint: String?) throws](./init%28contentsof,filetypehint%29.md)
  Creates a player to play audio from a file of a particular type.
- [init(data: Data) throws](./init%28data%29.md)
  Creates a player to play in-memory audio data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayer/init(data:filetypehint:))*