# AVMusicTrack

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

A collection of music events that you can offset, set to a muted state, modify independently from other track events, and send to a specified destination.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVMusicTrack
```

```objc
@interface AVMusicTrack : NSObject
```

## Topics

### Configuring music track properties
- [var isMuted: Bool](./avmusictrack/ismuted.md)
  A Boolean value that indicates whether the track is in a muted state.
- [var isSoloed: Bool](./avmusictrack/issoloed.md)
  A Boolean value that indicates whether the track is in a soloed state.
- [var offsetTime: AVMusicTimeStamp](./avmusictrack/offsettime.md)
  The offset of the track’s start time, in beats.
- [var timeResolution: Int](./avmusictrack/timeresolution.md)
  The time resolution value for the sequence, in ticks (pulses) per quarter note.
- [var usesAutomatedParameters: Bool](./avmusictrack/usesautomatedparameters.md)
  A Boolean value that indicates whether the track is an automation track.
### Configuring the track duration
- [var lengthInBeats: AVMusicTimeStamp](./avmusictrack/lengthinbeats.md)
  The total duration of the track, in beats.
- [var lengthInSeconds: TimeInterval](./avmusictrack/lengthinseconds.md)
  The total duration of the track, in seconds.
### Configuring the track destinations
- [var destinationAudioUnit: AVAudioUnit?](./avmusictrack/destinationaudiounit.md)
  The audio unit that receives the track’s events.
- [var destinationMIDIEndpoint: MIDIEndpointRef](./avmusictrack/destinationmidiendpoint.md)
  The MIDI endpoint you specify as the track’s target.
### Configuring the looping state
- [var isLoopingEnabled: Bool](./avmusictrack/isloopingenabled.md)
  A Boolean value that indicates whether the track is in a looping state.
- [var loopRange: AVBeatRange](./avmusictrack/looprange.md)
  The timestamp range for the loop, in beats.
- [var numberOfLoops: Int](./avmusictrack/numberofloops.md)
  The number of times the track’s loop repeats.
### Adding and clearing events
- [func addEvent(AVMusicEvent, at: AVMusicTimeStamp)](./avmusictrack/addevent%28_,at%29.md)
  Adds a music event to a track at the time you specify.
- [func moveEvents(in: AVBeatRange, by: AVMusicTimeStamp)](./avmusictrack/moveevents%28in,by%29.md)
  Moves the beat location of all events in the given beat range by the amount you specify.
- [func clearEvents(in: AVBeatRange)](./avmusictrack/clearevents%28in%29.md)
  Removes all events in the given beat range from the music track.
### Cutting and copying events
- [func cutEvents(in: AVBeatRange)](./avmusictrack/cutevents%28in%29.md)
  Splices all events in the beat range from the music track.
- [func copyEvents(in: AVBeatRange, from: AVMusicTrack, insertAt: AVMusicTimeStamp)](./avmusictrack/copyevents%28in,from,insertat%29.md)
  Copies the events from the source track and splices them into the current music track.
- [func copyAndMergeEvents(in: AVBeatRange, from: AVMusicTrack, mergeAt: AVMusicTimeStamp)](./avmusictrack/copyandmergeevents%28in,from,mergeat%29.md)
  Copies the events from the source track and merges them into the current music track.
### Iterating over events
- [func enumerateEvents(in: AVBeatRange, using: (AVMusicEvent, UnsafeMutablePointer<AVMusicTimeStamp>, UnsafeMutablePointer<ObjCBool>) -> Void)](./avmusictrack/enumerateevents%28in,using%29.md)
  Iterates through the music events within the track.
- [typealias AVMusicEventEnumerationBlock](./avmusiceventenumerationblock.md)
  A type you use to enumerate and remove music events, if necessary.
### Getting the end-of-track time
- [var AVMusicTimeStampEndOfTrack: Double](./avmusictimestampendoftrack.md)
  A timestamp you use to access all events in a music track through a beat range.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Handling music tracks
- [func createAndAppendTrack() -> AVMusicTrack](./avaudiosequencer/createandappendtrack%28%29.md)
  Creates a new music track and appends it to the sequencer’s list.
- [func reverseEvents()](./avaudiosequencer/reverseevents%28%29.md)
  Reverses the order of all events in all music tracks, including the tempo track.
- [func removeTrack(AVMusicTrack) -> Bool](./avaudiosequencer/removetrack%28_%29.md)
  Removes the music track from the sequencer.
- [enum AVMusicTrackLoopCount](./avmusictrackloopcount.md)
  Options that define the number of times a track loops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmusictrack)*