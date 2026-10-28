# init(data:)

**Framework**: AVFAudio  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithData:(NSData *) data error:(NSError **) outError;
```

## Return Value

A new audio player instance, or [`nil`](../../ObjectiveC/nil-227m0.md) if an error occurs.

## Discussion

The audio data must be in a format that Core Audio supports.

## Parameters

- `data`: A buffer with the audio data to play.

## See Also

### Creating an audio player
- [init(contentsOf: URL) throws](./init%28contentsof%29.md)
  Creates a player to play audio from a file.
- [init(contentsOf: URL, fileTypeHint: String?) throws](./init%28contentsof,filetypehint%29.md)
  Creates a player to play audio from a file of a particular type.
- [init(data: Data, fileTypeHint: String?) throws](./init%28data,filetypehint%29.md)
  Creates a player to play in-memory audio data of a particular type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayer/init(data:))*