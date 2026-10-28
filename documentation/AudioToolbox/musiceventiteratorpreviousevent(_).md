# MusicEventIteratorPreviousEvent(_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Positions a music event iterator at the previous event on a music track.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func MusicEventIteratorPreviousEvent(_ inIterator: MusicEventIterator) -> OSStatus
```

```c
extern OSStatus MusicEventIteratorPreviousEvent(MusicEventIterator inIterator);
```

## Return Value

A result code.

## Discussion

Use this function to decrement a music event iterator, moving it backward through a music track’s events.

If an iterator is at the first event of a track when you call this function, the iterator position remains unchanged and this function returns an error.

The following code snippet illustrates how to use a music event iterator to proceed backward along a music track, from the end:

```objc
// Points iterator just beyond the final event on its music track
MusicEventIteratorSeek (myIterator, kMusicTimeStamp_EndOfTrack);
 
bool hasPreviousEvent;
MusicEventIteratorHasPreviousEvent (myIterator, &hasPreviousEvent);
while (hasPreviousEvent) {
    MusicEventIteratorPreviousEvent (myIterator);
        // do work here
    MusicEventIteratorHasPreviousEvent (myIterator, &hasPreviousEvent);
}
```

## Parameters

- `inIterator`: The music event iterator to reposition.

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
- [func MusicEventIteratorSetEventInfo(MusicEventIterator, MusicEventType, UnsafeRawPointer) -> OSStatus](./musiceventiteratorseteventinfo%28_,_,_%29.md)
  Sets information for the event at a music event iterator’s current position.
- [func MusicEventIteratorSetEventTime(MusicEventIterator, MusicTimeStamp) -> OSStatus](./musiceventiteratorseteventtime%28_,_%29.md)
  Sets the timestamp for the event at a music event iterator’s current position.
- [typealias MusicEventIterator](./musiceventiterator.md)
  A music event iterator sequentially handles events on a music track.
- [typealias MusicEventType](./musiceventtype.md)
  MIDI and other music event types, used by music event iterator functions.
- [struct ExtendedNoteOnEvent](./extendednoteonevent.md)
  Describes a note-on event with extended parameters.
- [struct ExtendedTempoEvent](./extendedtempoevent.md)
  Describes a music track tempo in beats-per-minute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/musiceventiteratorpreviousevent(_:))*