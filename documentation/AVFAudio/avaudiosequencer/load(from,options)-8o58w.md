# load(from:options:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Parses the data and adds its events to the sequence.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func load(from data: Data, options: AVMusicSequenceLoadOptions = []) throws
```

```objc
- (BOOL) loadFromData:(NSData *) data options:(AVMusicSequenceLoadOptions) options error:(NSError **) outError;
```

## Parameters

- `data`: The data to load from.
- `options`: Determines how the contents map to the tracks inside the sequence.

## See Also

### Managing sequence load options
- [func load(from: URL, options: AVMusicSequenceLoadOptions) throws](./load%28from,options%29-9kb6m.md)
  Loads the file the URL references and adds the events to the sequence.
- [struct AVMusicSequenceLoadOptions](../avmusicsequenceloadoptions.md)
  A structure that defines whether data on different MIDI channels map to multiple tracks, or whether the framework preserves the tracks as they are.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosequencer/load(from:options:)-8o58w)*