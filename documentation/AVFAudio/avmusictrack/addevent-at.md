# addEvent(_:at:)

**Framework**: AVFAudio  
**Kind**: method

Adds a music event to a track at the time you specify.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func addEvent(_ event: AVMusicEvent, at beat: AVMusicTimeStamp)
```

#### Discussion

The system copies event contents into the track, so you can add the same event at different timestamps. You can’t add all [`AVMusicEvent`](avmusicevent.md) subclasses to a track.

- You can only add [`AVExtendedTempoEvent`](avextendedtempoevent.md) and [`AVMIDIMetaEvent`](avmidimetaevent.md) with certain [`AVMIDIMetaEvent.EventType`](avmidimetaevent/eventtype.md) to a sequencer’s tempo track.
- You can add [`AVParameterEvent`](avparameterevent.md) to automation tracks.
- You can’t add other event subclasses to tempo or automation tracks.

## Parameters

- `event`: The event to add.
- `beat`: The time to add the event at.

## See Also

- [func moveEvents(in: AVBeatRange, by: AVMusicTimeStamp)](avmusictrack/moveevents(in:by:).md)
  Moves the beat location of all events in the given beat range by the amount you specify.
- [func clearEvents(in: AVBeatRange)](avmusictrack/clearevents(in:).md)
  Removes all events in the given beat range from the music track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmusictrack/addevent(_:at:))*