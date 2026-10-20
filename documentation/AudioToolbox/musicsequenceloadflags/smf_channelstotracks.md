# smf_ChannelsToTracks

**Framework**: Audio Toolbox  
**Kind**: property

If this flag is set the resultant Sequence will contain a tempo track, 1 track for each MIDI Channel that is found in the SMF, 1 track for SysEx or MetaEvents - and this will be the last track in the sequence after the LoadSMFWithFlags calls.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
static var smf_ChannelsToTracks: MusicSequenceLoadFlags { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/musicsequenceloadflags/smf_channelstotracks)*