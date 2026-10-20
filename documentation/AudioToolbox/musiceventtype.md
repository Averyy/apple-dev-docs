# MusicEventType

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

MIDI and other music event types, used by music event iterator functions.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
typealias MusicEventType = UInt32
```

```c
typedef UInt32 MusicEventType;
```

## Topics

### Constants
- [var kMusicEventType_NULL: UInt32](./kmusiceventtype_null.md)
  A null music event.
- [var kMusicEventType_ExtendedNote: UInt32](./kmusiceventtype_extendednote.md)
  A non-MIDI music event with variable number of parameters.
- [var kMusicEventType_ExtendedTempo: UInt32](./kmusiceventtype_extendedtempo.md)
  An event that signals a change in tempo, in beats-per-minute.
- [var kMusicEventType_User: UInt32](./kmusiceventtype_user.md)
  User-defined data.
- [var kMusicEventType_Meta: UInt32](./kmusiceventtype_meta.md)
  A standard MIDI file metaevent.
- [var kMusicEventType_MIDINoteMessage: UInt32](./kmusiceventtype_midinotemessage.md)
  A MIDI note-on message, including duration.
- [var kMusicEventType_MIDIChannelMessage: UInt32](./kmusiceventtype_midichannelmessage.md)
  A MIDI channel message, other than note control.
- [var kMusicEventType_MIDIRawData: UInt32](./kmusiceventtype_midirawdata.md)
  MIDI system-exclusive data.
- [var kMusicEventType_Parameter: UInt32](./kmusiceventtype_parameter.md)
  An audio unit parameter event.
- [var kMusicEventType_AUPreset: UInt32](./kmusiceventtype_aupreset.md)
  An event containing an audio unit user preset dictionary.

## See Also

### Iterating Over Music Events
- [func NewMusicEventIterator(MusicTrack, UnsafeMutablePointer<MusicEventIterator?>) -> OSStatus](./newmusiceventiterator%28_,_%29.md)
  Creates a new music event iterator.
- [func DisposeMusicEventIterator(MusicEventIterator) -> OSStatus](./disposemusiceventiterator%28_%29.md)
  Disposes of a music event iterator.
- [func MusicEventIteratorNextEvent(MusicEventIterator) -> OSStatus](./musiceventiteratornextevent%28_%29.md)
  Positions a music event iterator at the next event on a music track.
- [func MusicEventIteratorSeek(MusicEventIterator, MusicTimeStamp) -> OSStatus](./musiceventiteratorseek%28_,_%29.md)
  Positions a music event iterator at a specified timestamp, in beats.
- [func MusicEventIteratorDeleteEvent(MusicEventIterator) -> OSStatus](./musiceventiteratordeleteevent%28_%29.md)
  Deletes the event at a music event iterator’s current position.
- [func MusicEventIteratorGetEventInfo(MusicEventIterator, UnsafeMutablePointer<MusicTimeStamp>, UnsafeMutablePointer<MusicEventType>, UnsafeMutablePointer<UnsafeRawPointer?>, UnsafeMutablePointer<UInt32>) -> OSStatus](./musiceventiteratorgeteventinfo%28_,_,_,_,_%29.md)
  Gets information about the event at a music event iterator’s current position.
- [func MusicEventIteratorHasCurrentEvent(MusicEventIterator, UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](./musiceventiteratorhascurrentevent%28_,_%29.md)
  Indicates whether or not a music track contains an event at the music event iterator’s current position.
- [func MusicEventIteratorHasNextEvent(MusicEventIterator, UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](./musiceventiteratorhasnextevent%28_,_%29.md)
  Indicates whether or not a music track contains an event beyond the music event iterator’s current position.
- [func MusicEventIteratorHasPreviousEvent(MusicEventIterator, UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](./musiceventiteratorhaspreviousevent%28_,_%29.md)
  Indicates whether or not a music track contains an event before the music event iterator’s current position.
- [func MusicEventIteratorPreviousEvent(MusicEventIterator) -> OSStatus](./musiceventiteratorpreviousevent%28_%29.md)
  Positions a music event iterator at the previous event on a music track.
- [func MusicEventIteratorSetEventInfo(MusicEventIterator, MusicEventType, UnsafeRawPointer) -> OSStatus](./musiceventiteratorseteventinfo%28_,_,_%29.md)
  Sets information for the event at a music event iterator’s current position.
- [func MusicEventIteratorSetEventTime(MusicEventIterator, MusicTimeStamp) -> OSStatus](./musiceventiteratorseteventtime%28_,_%29.md)
  Sets the timestamp for the event at a music event iterator’s current position.
- [typealias MusicEventIterator](./musiceventiterator.md)
  A music event iterator sequentially handles events on a music track.
- [struct ExtendedNoteOnEvent](./extendednoteonevent.md)
  Describes a note-on event with extended parameters.
- [struct ExtendedTempoEvent](./extendedtempoevent.md)
  Describes a music track tempo in beats-per-minute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/musiceventtype)*