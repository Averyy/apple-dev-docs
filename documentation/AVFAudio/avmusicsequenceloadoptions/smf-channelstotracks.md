# smf_ChannelsToTracks

**Framework**: AVFAudio  
**Kind**: property

An option that represents data on different MIDI channels mapped to multiple tracks.

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
static var smf_ChannelsToTracks: AVMusicSequenceLoadOptions { get }
```

#### Discussion

The MIDI sequence contains a tempo track, one track for each MIDI channel in the SMF, and one track (the last track) for `SysEx` and `MetaEvents`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmusicsequenceloadoptions/smf_channelstotracks)*