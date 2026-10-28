# NewMusicEventIterator(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Creates a new music event iterator.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func NewMusicEventIterator(_ inTrack: MusicTrack, _ outIterator: UnsafeMutablePointer<MusicEventIterator?>) -> OSStatus
```

```c
extern OSStatus NewMusicEventIterator(MusicTrack inTrack, MusicEventIterator*outIterator);
```

## Return Value

A result code.

## Discussion

A newly-created music event iterator points at the first event on the music track specified in the `inTrack` parameter.

If you edit a music track after associating it with a music event iterator, you must discard iterator and create a new one. Perform the following steps after editing the track:

1. Obtain the current position using the [`MusicEventIteratorGetEventInfo(_:_:_:_:_:)`](./musiceventiteratorgeteventinfo%28_,_,_,_,_%29.md) function, and save the position.
2. Dispose of the music event iterator.
3. Create a new iterator.
4. Seek to the desired position using the [`MusicEventIteratorSeek(_:_:)`](./musiceventiteratorseek%28_,_%29.md) function.

## Parameters

- `inTrack`: The music track to iterate over.
- `outIterator`: On output, the newly created music event iterator.

## See Also

### Iterating Over Music Events
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
- [typealias MusicEventType](./musiceventtype.md)
  MIDI and other music event types, used by music event iterator functions.
- [struct ExtendedNoteOnEvent](./extendednoteonevent.md)
  Describes a note-on event with extended parameters.
- [struct ExtendedTempoEvent](./extendedtempoevent.md)
  Describes a music track tempo in beats-per-minute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/newmusiceventiterator(_:_:))*