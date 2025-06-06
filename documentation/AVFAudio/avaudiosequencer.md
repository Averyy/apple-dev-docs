# AVAudioSequencer

**Framework**: AVFAudio  
**Kind**: class

An object that plays audio from a collection of MIDI events the system organizes into music tracks.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVAudioSequencer
```

## Topics

### Creating an Audio Sequencer
- [init()](avaudiosequencer/init.md)
  Creates an audio sequencer object.
- [init(audioEngine: AVAudioEngine)](avaudiosequencer/init(audioengine:).md)
  Creates an audio sequencer that the framework attaches to an audio engine instance.
### Writing to a MIDI File
- [func write(to: URL, smpteResolution: Int, replaceExisting: Bool) throws](avaudiosequencer/write(to:smpteresolution:replaceexisting:).md)
  Creates and writes a MIDI file from the events in the sequence.
### Handling Music Tracks
- [class AVMusicTrack](avmusictrack.md)
  A collection of music events that you can offset, set to a muted state, modify independently from other track events, and send to a specified destination.
- [func createAndAppendTrack() -> AVMusicTrack](avaudiosequencer/createandappendtrack.md)
  Creates a new music track and appends it to the sequencer’s list.
- [func reverseEvents()](avaudiosequencer/reverseevents.md)
  Reverses the order of all events in all music tracks, including the tempo track.
- [func removeTrack(AVMusicTrack) -> Bool](avaudiosequencer/removetrack(_:).md)
  Removes the music track from the sequencer.
- [enum AVMusicTrackLoopCount](avmusictrackloopcount.md)
  Options that define the number of times a track loops.
### Handling Music Events
- [class AVMusicEvent](avmusicevent.md)
  A base class for the events you associate with a music track.
- [class AVMusicUserEvent](avmusicuserevent.md)
  An object that represents a custom user message.
- [class AVParameterEvent](avparameterevent.md)
  An object that represents a parameter event on a music track’s destination.
- [class AVAUPresetEvent](avaupresetevent.md)
  An object that represents a preset load and change on the music track’s destination audio unit.
- [class AVExtendedTempoEvent](avextendedtempoevent.md)
  An object that represents a tempo change to a specific beats-per-minute value.
- [class AVExtendedNoteOnEvent](avextendednoteonevent.md)
  An object that represents a custom extension of a MIDI note on event.
### Handling MIDI Events
- [class AVMIDINoteEvent](avmidinoteevent.md)
  An object that represents MIDI note on or off messages.
- [class AVMIDIMetaEvent](avmidimetaevent.md)
  An object that represents MIDI meta event messages.
- [class AVMIDISysexEvent](avmidisysexevent.md)
  An object that represents a MIDI system exclusive message.
### Handling MIDI Channel Events
- [class AVMIDIChannelEvent](avmidichannelevent.md)
  A base class for all MIDI messages that operate on a single MIDI channel.
- [class AVMIDIChannelPressureEvent](avmidichannelpressureevent.md)
  An object that represents a MIDI channel pressure message.
- [class AVMIDIProgramChangeEvent](avmidiprogramchangeevent.md)
  An object that represents a MIDI program or patch change message.
- [class AVMIDIPolyPressureEvent](avmidipolypressureevent.md)
  An object that represents a MIDI poly or key pressure event.
- [class AVMIDIPitchBendEvent](avmidipitchbendevent.md)
  An object that represents a MIDI pitch bend message.
- [class AVMIDIControlChangeEvent](avmidicontrolchangeevent.md)
  An object that represents a MIDI control change message.
### Managing Sequence Load Options
- [func load(from: Data, options: AVMusicSequenceLoadOptions) throws](avaudiosequencer/load(from:options:)-8o58w.md)
  Parses the data and adds its events to the sequence.
- [func load(from: URL, options: AVMusicSequenceLoadOptions) throws](avaudiosequencer/load(from:options:)-9kb6m.md)
  Loads the file the URL references and adds the events to the sequence.
- [struct AVMusicSequenceLoadOptions](avmusicsequenceloadoptions.md)
  A structure that defines whether data on different MIDI channels map to multiple tracks, or whether the framework preserves the tracks as they are.
### Operating an Audio Sequencer
- [func prepareToPlay()](avaudiosequencer/preparetoplay.md)
  Gets ready to play the sequence by prerolling all events.
- [func start() throws](avaudiosequencer/start.md)
  Starts the sequencer’s player.
- [func stop()](avaudiosequencer/stop.md)
  Stops the sequencer’s player.
### Managing Time Stamps
- [typealias AVMusicTimeStamp](avmusictimestamp.md)
  A fractional number of beats.
- [func hostTime(forBeats: AVMusicTimeStamp, error: NSErrorPointer) -> UInt64](avaudiosequencer/hosttime(forbeats:error:).md)
  Gets the host time the sequence plays at the specified position.
- [func seconds(forBeats: AVMusicTimeStamp) -> TimeInterval](avaudiosequencer/seconds(forbeats:).md)
  Gets the time for the specified beat position (timestamp) in the track, in seconds.
### Handling Beat Range
- [func beats(forHostTime: UInt64, error: NSErrorPointer) -> AVMusicTimeStamp](avaudiosequencer/beats(forhosttime:error:).md)
  Gets the beat the system plays at the specified host time.
- [func beats(forSeconds: TimeInterval) -> AVMusicTimeStamp](avaudiosequencer/beats(forseconds:).md)
  Gets the beat position (timestamp) for the specified time in the track.
- [var AVMusicTimeStampEndOfTrack: Double](avmusictimestampendoftrack.md)
  A timestamp you use to access all events in a music track through a beat range.
- [typealias AVBeatRange](avbeatrange.md)
  A specific time range within a music track.
### Setting the User Callback
- [func setUserCallback(AVAudioSequencerUserCallback?)](avaudiosequencer/setusercallback(_:).md)
  Adds a callback that the sequencer calls each time it encounters a user event during playback.
- [typealias AVAudioSequencerUserCallback](avaudiosequencerusercallback.md)
  A callback the sequencer calls asynchronously during playback when it encounters a user event.
### Getting Sequence Properties
- [var isPlaying: Bool](avaudiosequencer/isplaying.md)
  A Boolean value that indicates whether the sequencer’s player is in a playing state.
- [var rate: Float](avaudiosequencer/rate.md)
  The playback rate of the sequencer’s player.
- [var tracks: [AVMusicTrack]](avaudiosequencer/tracks.md)
  An array that contains all the tracks in the sequence.
- [var currentPositionInBeats: TimeInterval](avaudiosequencer/currentpositioninbeats.md)
  The current playback position, in beats.
- [var currentPositionInSeconds: TimeInterval](avaudiosequencer/currentpositioninseconds.md)
  The current playback position, in seconds.
- [var tempoTrack: AVMusicTrack](avaudiosequencer/tempotrack.md)
  The track that contains tempo information about the sequence.
- [var userInfo: [String : Any]](avaudiosequencer/userinfo.md)
  A dictionary that contains metadata from a sequence.
- [AVAudioSequencer.InfoDictionaryKey](avaudiosequencer/infodictionarykey.md)
  Constants that defines metadata keys for a sequencer.
- [func data(withSMPTEResolution: Int, error: NSErrorPointer) -> Data](avaudiosequencer/data(withsmpteresolution:error:).md)
  Gets a data object that contains the events from the sequence.
- [var AVMusicTimeStampEndOfTrack: Double](avmusictimestampendoftrack.md)
  A timestamp you use to access all events in a music track through a beat range.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVAudioUnitSampler](avaudiounitsampler.md)
  An object that you configure with one or more instrument samples, based on Apple’s Sampler audio unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosequencer)*