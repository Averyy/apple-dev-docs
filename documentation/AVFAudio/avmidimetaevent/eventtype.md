# AVMIDIMetaEvent.EventType

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

Constants that represent the types of meta events.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum EventType
```

```c
enum AVMIDIMetaEventType : NSInteger;
```

## Topics

### Creating an event type
- [init?(rawValue: Int)](./eventtype/init%28rawvalue%29.md)
### Identifying meta event types
- [AVMIDIMetaEvent.EventType.copyright](./eventtype/copyright.md)
  An event type that represents a copyright.
- [AVMIDIMetaEvent.EventType.cuePoint](./eventtype/cuepoint.md)
  An event type that represents a cue point.
- [AVMIDIMetaEvent.EventType.endOfTrack](./eventtype/endoftrack.md)
  An event type that represents the end of the track.
- [AVMIDIMetaEvent.EventType.instrument](./eventtype/instrument.md)
  An event type that represents an instrument.
- [AVMIDIMetaEvent.EventType.keySignature](./eventtype/keysignature.md)
  An event type that represents a key signature.
- [AVMIDIMetaEvent.EventType.lyric](./eventtype/lyric.md)
  An event type that represents a lyric.
- [AVMIDIMetaEvent.EventType.marker](./eventtype/marker.md)
  An event type that represents a marker.
- [AVMIDIMetaEvent.EventType.midiChannel](./eventtype/midichannel.md)
  An event type that represents a MIDI channel.
- [AVMIDIMetaEvent.EventType.midiPort](./eventtype/midiport.md)
  An event type that represents a MIDI port.
- [AVMIDIMetaEvent.EventType.proprietaryEvent](./eventtype/proprietaryevent.md)
  An event type that represents a proprietary event.
- [AVMIDIMetaEvent.EventType.sequenceNumber](./eventtype/sequencenumber.md)
  An event type that represents a sequence number.
- [AVMIDIMetaEvent.EventType.smpteOffset](./eventtype/smpteoffset.md)
  An event type that represents a SMPTE time offset.
- [AVMIDIMetaEvent.EventType.tempo](./eventtype/tempo.md)
  An event type that represents a tempo.
- [AVMIDIMetaEvent.EventType.text](./eventtype/text.md)
  An event type that represents text.
- [AVMIDIMetaEvent.EventType.timeSignature](./eventtype/timesignature.md)
  An event type that represents a time signature.
- [AVMIDIMetaEvent.EventType.trackName](./eventtype/trackname.md)
  An event type that represents a track name.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the meta event type
- [var type: AVMIDIMetaEvent.EventType](./type.md)
  The type of meta event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmidimetaevent/eventtype)*