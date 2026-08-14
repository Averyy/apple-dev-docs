# AVMusicSequenceLoadOptions

**Framework**: AVFAudio  
**Kind**: struct

A structure that defines whether data on different MIDI channels map to multiple tracks, or whether the framework preserves the tracks as they are.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct AVMusicSequenceLoadOptions
```

## Topics

### Getting Standard Load Options
- [static var smf_ChannelsToTracks: AVMusicSequenceLoadOptions](avmusicsequenceloadoptions/smf_channelstotracks.md)
  An option that represents data on different MIDI channels mapped to multiple tracks.
### Creating a Load Option
- [init(rawValue: UInt)](avmusicsequenceloadoptions/init(rawvalue:).md)
  Creates a new instance with the raw value you specify.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [func load(from: Data, options: AVMusicSequenceLoadOptions) throws](avaudiosequencer/load(from:options:)-8o58w.md)
  Parses the data and adds its events to the sequence.
- [func load(from: URL, options: AVMusicSequenceLoadOptions) throws](avaudiosequencer/load(from:options:)-9kb6m.md)
  Loads the file the URL references and adds the events to the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmusicsequenceloadoptions)*