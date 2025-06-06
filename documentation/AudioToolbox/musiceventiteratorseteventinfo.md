# MusicEventIteratorSetEventInfo(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Sets information for the event at a music event iterator’s current position.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func MusicEventIteratorSetEventInfo(_ inIterator: MusicEventIterator, _ inEventType: MusicEventType, _ inEventData: UnsafeRawPointer) -> OSStatus
```

#### Return Value

A result code.

#### Discussion

Use this function to set the music event type and event data for the event that a music event iterator is positioned at. This function doesn’t allow you to change an event’s timestamp; to do that, call the [`MusicEventIteratorSetEventTime(_:_:)`](musiceventiteratorseteventtime(_:_:).md) function.

## Parameters

- `inIterator`: The music event iterator whose current event you want to set.
- `inEventType`: The type of music event that you are specifying. For possible event types, see  .
- `inEventData`: The event data that you are specifying. The size and type of the data must be appropriate for the music event type you specify in the   parameter.

## See Also

- [func NewMusicEventIterator(MusicTrack, UnsafeMutablePointer<MusicEventIterator?>) -> OSStatus](newmusiceventiterator(_:_:).md)
  Creates a new music event iterator.
- [func DisposeMusicEventIterator(MusicEventIterator) -> OSStatus](disposemusiceventiterator(_:).md)
  Disposes of a music event iterator.
- [func MusicEventIteratorNextEvent(MusicEventIterator) -> OSStatus](musiceventiteratornextevent(_:).md)
  Positions a music event iterator at the next event on a music track.
- [func MusicEventIteratorSeek(MusicEventIterator, MusicTimeStamp) -> OSStatus](musiceventiteratorseek(_:_:).md)
  Positions a music event iterator at a specified timestamp, in beats.
- [func MusicEventIteratorDeleteEvent(MusicEventIterator) -> OSStatus](musiceventiteratordeleteevent(_:).md)
  Deletes the event at a music event iterator’s current position.
- [func MusicEventIteratorGetEventInfo(MusicEventIterator, UnsafeMutablePointer<MusicTimeStamp>, UnsafeMutablePointer<MusicEventType>, UnsafeMutablePointer<UnsafeRawPointer?>, UnsafeMutablePointer<UInt32>) -> OSStatus](musiceventiteratorgeteventinfo(_:_:_:_:_:).md)
  Gets information about the event at a music event iterator’s current position.
- [func MusicEventIteratorHasCurrentEvent(MusicEventIterator, UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](musiceventiteratorhascurrentevent(_:_:).md)
  Indicates whether or not a music track contains an event at the music event iterator’s current position.
- [func MusicEventIteratorHasNextEvent(MusicEventIterator, UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](musiceventiteratorhasnextevent(_:_:).md)
  Indicates whether or not a music track contains an event beyond the music event iterator’s current position.
- [func MusicEventIteratorHasPreviousEvent(MusicEventIterator, UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](musiceventiteratorhaspreviousevent(_:_:).md)
  Indicates whether or not a music track contains an event before the music event iterator’s current position.
- [func MusicEventIteratorPreviousEvent(MusicEventIterator) -> OSStatus](musiceventiteratorpreviousevent(_:).md)
  Positions a music event iterator at the previous event on a music track.
- [func MusicEventIteratorSetEventTime(MusicEventIterator, MusicTimeStamp) -> OSStatus](musiceventiteratorseteventtime(_:_:).md)
  Sets the timestamp for the event at a music event iterator’s current position.
- [typealias MusicEventIterator](musiceventiterator.md)
  A music event iterator sequentially handles events on a music track.
- [typealias MusicEventType](musiceventtype.md)
  MIDI and other music event types, used by music event iterator functions.
- [struct ExtendedNoteOnEvent](extendednoteonevent.md)
  Describes a note-on event with extended parameters.
- [struct ExtendedTempoEvent](extendedtempoevent.md)
  Describes a music track tempo in beats-per-minute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/musiceventiteratorseteventinfo(_:_:_:))*