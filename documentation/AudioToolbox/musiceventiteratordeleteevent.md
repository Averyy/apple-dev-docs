# MusicEventIteratorDeleteEvent(_:)

**Framework**: Audio Toolbox  
**Kind**: func

Deletes the event at a music event iterator’s current position.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func MusicEventIteratorDeleteEvent(_ inIterator: MusicEventIterator) -> OSStatus
```

#### Return Value

A result code.

#### Discussion

After calling this function, the music event iterator points to the event that follows the deleted event—if there is such an event. If the event you deleted was the final event, the iterator is then positioned immediately beyond the final event of the music track.

## Parameters

- `inIterator`: The music event iterator whose current event you want to delete.

## See Also

- [func NewMusicEventIterator(MusicTrack, UnsafeMutablePointer<MusicEventIterator?>) -> OSStatus](newmusiceventiterator(_:_:).md)
  Creates a new music event iterator.
- [func DisposeMusicEventIterator(MusicEventIterator) -> OSStatus](disposemusiceventiterator(_:).md)
  Disposes of a music event iterator.
- [func MusicEventIteratorNextEvent(MusicEventIterator) -> OSStatus](musiceventiteratornextevent(_:).md)
  Positions a music event iterator at the next event on a music track.
- [func MusicEventIteratorSeek(MusicEventIterator, MusicTimeStamp) -> OSStatus](musiceventiteratorseek(_:_:).md)
  Positions a music event iterator at a specified timestamp, in beats.
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
- [func MusicEventIteratorSetEventInfo(MusicEventIterator, MusicEventType, UnsafeRawPointer) -> OSStatus](musiceventiteratorseteventinfo(_:_:_:).md)
  Sets information for the event at a music event iterator’s current position.
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

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/musiceventiteratordeleteevent(_:))*