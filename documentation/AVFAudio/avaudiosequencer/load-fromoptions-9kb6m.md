# load(from:options:)

**Framework**: AVFAudio  
**Kind**: method

Loads the file the URL references and adds the events to the sequence.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func load(from fileURL: URL, options: AVMusicSequenceLoadOptions = []) throws
```

## Parameters

- `fileURL`: The URL to the file.
- `options`: Determines how the contents map to the tracks inside the sequence.

## See Also

- [func load(from: Data, options: AVMusicSequenceLoadOptions) throws](avaudiosequencer/load(from:options:)-8o58w.md)
  Parses the data and adds its events to the sequence.
- [struct AVMusicSequenceLoadOptions](avmusicsequenceloadoptions.md)
  A structure that defines whether data on different MIDI channels map to multiple tracks, or whether the framework preserves the tracks as they are.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosequencer/load(from:options:)-9kb6m)*