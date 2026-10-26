# AVMusicSequenceLoadOptions

**Framework**: AVFAudio  
**Kind**: struct  
**Role**: Structure

A structure that defines whether data on different MIDI channels map to multiple tracks, or whether the framework preserves the tracks as they are.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct AVMusicSequenceLoadOptions
```

```c
enum AVMusicSequenceLoadOptions : NSUInteger;
```

## Topics

### Creating a load option
- [init(rawValue: UInt)](./avmusicsequenceloadoptions/init%28rawvalue%29.md)
  Creates a new instance with the raw value you specify.
- [AVMusicSequenceLoadSMF_PreserveTracks](./avmusicsequenceloadoptions/avmusicsequenceloadsmf_preservetracks.md)
  An option that preserves the tracks as they are.
### Getting standard load options
- [static var smf_ChannelsToTracks: AVMusicSequenceLoadOptions](./avmusicsequenceloadoptions/smf_channelstotracks.md)
  An option that represents data on different MIDI channels mapped to multiple tracks.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Managing sequence load options
- [func load(from: Data, options: AVMusicSequenceLoadOptions) throws](./avaudiosequencer/load%28from,options%29-8o58w.md)
  Parses the data and adds its events to the sequence.
- [func load(from: URL, options: AVMusicSequenceLoadOptions) throws](./avaudiosequencer/load%28from,options%29-9kb6m.md)
  Loads the file the URL references and adds the events to the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmusicsequenceloadoptions)*