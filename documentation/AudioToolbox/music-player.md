# Music Player

**Framework**: Audio Toolbox

Create and play a sequence of tracks, and manage aspects of playback in response to standard events.

## Topics

### Managing a Music Player
- [func NewMusicPlayer(UnsafeMutablePointer<MusicPlayer?>) -> OSStatus](newmusicplayer(_:).md)
  Creates a new music player.
- [func DisposeMusicPlayer(MusicPlayer) -> OSStatus](disposemusicplayer(_:).md)
  Disposes of a music player.
- [func MusicPlayerGetBeatsForHostTime(MusicPlayer, UInt64, UnsafeMutablePointer<MusicTimeStamp>) -> OSStatus](musicplayergetbeatsforhosttime(_:_:_:).md)
  Gets the beat number associated a specified host time.
- [func MusicPlayerGetHostTimeForBeats(MusicPlayer, MusicTimeStamp, UnsafeMutablePointer<UInt64>) -> OSStatus](musicplayergethosttimeforbeats(_:_:_:).md)
  Gets the host time associated with a specified beat.
- [func MusicPlayerGetPlayRateScalar(MusicPlayer, UnsafeMutablePointer<Float64>) -> OSStatus](musicplayergetplayratescalar(_:_:).md)
  Gets the playback rate multiplier for a music player.
- [func MusicPlayerGetSequence(MusicPlayer, UnsafeMutablePointer<MusicSequence?>) -> OSStatus](musicplayergetsequence(_:_:).md)
  Gets the music sequence associated with a music player.
- [func MusicPlayerGetTime(MusicPlayer, UnsafeMutablePointer<MusicTimeStamp>) -> OSStatus](musicplayergettime(_:_:).md)
  Gets the playback point for a music player, in beats.
- [func MusicPlayerIsPlaying(MusicPlayer, UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](musicplayerisplaying(_:_:).md)
  Indicates whether or not a music player is playing.
- [func MusicPlayerPreroll(MusicPlayer) -> OSStatus](musicplayerpreroll(_:).md)
  Prepares a music player to play.
- [func MusicPlayerSetPlayRateScalar(MusicPlayer, Float64) -> OSStatus](musicplayersetplayratescalar(_:_:).md)
  Sets a playback rate multiplier for a music player.
- [func MusicPlayerSetSequence(MusicPlayer, MusicSequence?) -> OSStatus](musicplayersetsequence(_:_:).md)
  Sets the music sequence for the music player to play.
- [func MusicPlayerSetTime(MusicPlayer, MusicTimeStamp) -> OSStatus](musicplayersettime(_:_:).md)
  Sets the playback point for a music player, in beats.
- [func MusicPlayerStart(MusicPlayer) -> OSStatus](musicplayerstart(_:).md)
  Starts playback of a music player.
- [func MusicPlayerStop(MusicPlayer) -> OSStatus](musicplayerstop(_:).md)
  Stops playback of a music player.
- [typealias MusicPlayer](musicplayer.md)
  A music player plays a music sequence (of type `MusicSequence`).
- [typealias MusicTimeStamp](musictimestamp.md)
  A timestamp for use by a music sequence.
- [var kMusicTimeStamp_EndOfTrack: Double](kmusictimestamp_endoftrack.md)
  Indicates a time immediately beyond the last music event in a music track. Use this value when selecting all music events starting at a designated time and extending to, and including, the last event in a track. Also use this value to position an iterator for moving backward through a track, from the end to the start. See also [`NewMusicEventIterator(_:_:)`](newmusiceventiterator(_:_:).md) and [`MusicEventIteratorSeek(_:_:)`](musiceventiteratorseek(_:_:).md).
### Iterating Over Music Events
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
- [struct MusicEventUserData](musiceventuserdata.md)
  Describes a user-defined event.
- [struct ParameterEvent](parameterevent.md)
  Describes an audio unit parameter automation event.
- [struct MusicDeviceNoteParams](musicdevicenoteparams.md)
- [struct MusicDeviceStdNoteParams](musicdevicestdnoteparams.md)
- [struct NoteParamsControlValue](noteparamscontrolvalue.md)
### Managing Music Sequences
- [func NewMusicSequence(UnsafeMutablePointer<MusicSequence?>) -> OSStatus](newmusicsequence(_:).md)
  Creates a new empty music sequence.
- [func DisposeMusicSequence(MusicSequence) -> OSStatus](disposemusicsequence(_:).md)
  Disposes of a music sequence.
- [func MusicSequenceBarBeatTimeToBeats(MusicSequence, UnsafePointer<CABarBeatTime>, UnsafeMutablePointer<MusicTimeStamp>) -> OSStatus](musicsequencebarbeattimetobeats(_:_:_:).md)
  Formats a music sequence’s bar-beat time to its beat time.
- [func MusicSequenceBeatsToBarBeatTime(MusicSequence, MusicTimeStamp, UInt32, UnsafeMutablePointer<CABarBeatTime>) -> OSStatus](musicsequencebeatstobarbeattime(_:_:_:_:).md)
  Formats a music sequence’s beat time to its bar-beat time.
- [func MusicSequenceDisposeTrack(MusicSequence, MusicTrack) -> OSStatus](musicsequencedisposetrack(_:_:).md)
  Removes a music track from a music sequence, and disposes of the track.
- [func MusicSequenceFileCreate(MusicSequence, CFURL, MusicSequenceFileTypeID, MusicSequenceFileFlags, Int16) -> OSStatus](musicsequencefilecreate(_:_:_:_:_:).md)
  Creates a MIDI file from the events in a music sequence.
- [func MusicSequenceFileCreateData(MusicSequence, MusicSequenceFileTypeID, MusicSequenceFileFlags, Int16, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus](musicsequencefilecreatedata(_:_:_:_:_:).md)
  Creates a data object containing the events from a music sequence.
- [func MusicSequenceFileLoad(MusicSequence, CFURL, MusicSequenceFileTypeID, MusicSequenceLoadFlags) -> OSStatus](musicsequencefileload(_:_:_:_:).md)
  Loads data into a music sequence from a URL reference.
- [func MusicSequenceFileLoadData(MusicSequence, CFData, MusicSequenceFileTypeID, MusicSequenceLoadFlags) -> OSStatus](musicsequencefileloaddata(_:_:_:_:).md)
  Load data into a music sequence from a data reference.
- [func MusicSequenceGetAUGraph(MusicSequence, UnsafeMutablePointer<AUGraph?>) -> OSStatus](musicsequencegetaugraph(_:_:).md)
  Gets the audio processing graph associated with a music sequence.
- [func MusicSequenceGetBeatsForSeconds(MusicSequence, Float64, UnsafeMutablePointer<MusicTimeStamp>) -> OSStatus](musicsequencegetbeatsforseconds(_:_:_:).md)
  Calculates the number of beats that correspond to a number of seconds.
- [func MusicSequenceGetIndTrack(MusicSequence, UInt32, UnsafeMutablePointer<MusicTrack?>) -> OSStatus](musicsequencegetindtrack(_:_:_:).md)
  Gets the music track at the specified track index.
- [func MusicSequenceGetInfoDictionary(MusicSequence) -> CFDictionary](musicsequencegetinfodictionary(_:).md)
  Returns a dictionary containing music sequence information.
- [func MusicSequenceGetSMPTEResolution(Int16, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<UInt8>)](musicsequencegetsmpteresolution(_:_:_:).md)
- [func MusicSequenceGetSecondsForBeats(MusicSequence, MusicTimeStamp, UnsafeMutablePointer<Float64>) -> OSStatus](musicsequencegetsecondsforbeats(_:_:_:).md)
  Calculates the number of seconds that correspond to a number of beats.
- [func MusicSequenceGetSequenceType(MusicSequence, UnsafeMutablePointer<MusicSequenceType>) -> OSStatus](musicsequencegetsequencetype(_:_:).md)
  Gets the sequence type for a music sequence.
- [func MusicSequenceGetTempoTrack(MusicSequence, UnsafeMutablePointer<MusicTrack?>) -> OSStatus](musicsequencegettempotrack(_:_:).md)
  Gets the tempo track for a music sequence.
- [func MusicSequenceGetTrackCount(MusicSequence, UnsafeMutablePointer<UInt32>) -> OSStatus](musicsequencegettrackcount(_:_:).md)
  Gets the number of music tracks owned by a music sequence.
- [func MusicSequenceGetTrackIndex(MusicSequence, MusicTrack, UnsafeMutablePointer<UInt32>) -> OSStatus](musicsequencegettrackindex(_:_:_:).md)
  Gets the index number for a specified music track.
- [func MusicSequenceNewTrack(MusicSequence, UnsafeMutablePointer<MusicTrack?>) -> OSStatus](musicsequencenewtrack(_:_:).md)
  Add a new, empty music track to a music sequence.
- [func MusicSequenceReverse(MusicSequence) -> OSStatus](musicsequencereverse(_:).md)
  Reverses the MIDI and tempo events in a music sequence, so the start becomes the end.
- [func MusicSequenceSetAUGraph(MusicSequence, AUGraph?) -> OSStatus](musicsequencesetaugraph(_:_:).md)
  Associates an audio processing graph with a music sequence.
- [func MusicSequenceSetMIDIEndpoint(MusicSequence, MIDIEndpointRef) -> OSStatus](musicsequencesetmidiendpoint(_:_:).md)
  Associates a specified MIDI endpoint with all music tracks in a music sequence.
- [func MusicSequenceSetSMPTEResolution(Int8, UInt8) -> Int16](musicsequencesetsmpteresolution(_:_:).md)
- [func MusicSequenceSetSequenceType(MusicSequence, MusicSequenceType) -> OSStatus](musicsequencesetsequencetype(_:_:).md)
  Sets the sequence type for a music sequence.
- [func MusicSequenceSetUserCallback(MusicSequence, MusicSequenceUserCallback?, UnsafeMutableRawPointer?) -> OSStatus](musicsequencesetusercallback(_:_:_:).md)
  Registers a user callback function with a music sequence.
- [typealias MusicSequence](musicsequence.md)
  A music sequence.
- [typealias MusicSequenceUserCallback](musicsequenceusercallback.md)
- [struct MusicSequenceFileFlags](musicsequencefileflags.md)
  Flags that configure the behavior of the [`MusicSequenceFileCreate(_:_:_:_:_:)`](musicsequencefilecreate(_:_:_:_:_:).md) and [`MusicSequenceFileCreateData(_:_:_:_:_:)`](musicsequencefilecreatedata(_:_:_:_:_:).md) functions.
- [struct MusicSequenceLoadFlags](musicsequenceloadflags.md)
  Flags used to configure the behavior of the [`MusicSequenceFileLoad(_:_:_:_:)`](musicsequencefileload(_:_:_:_:).md) and [`MusicSequenceFileLoadData(_:_:_:_:)`](musicsequencefileloaddata(_:_:_:_:).md) functions.
### Managing Music Tracks
- [func MusicTrackClear(MusicTrack, MusicTimeStamp, MusicTimeStamp) -> OSStatus](musictrackclear(_:_:_:).md)
  Removes a specified range of music track events.
- [func MusicTrackCopyInsert(MusicTrack, MusicTimeStamp, MusicTimeStamp, MusicTrack, MusicTimeStamp) -> OSStatus](musictrackcopyinsert(_:_:_:_:_:).md)
  Copies a range of events from one music track and inserts them into another music track.
- [func MusicTrackCut(MusicTrack, MusicTimeStamp, MusicTimeStamp) -> OSStatus](musictrackcut(_:_:_:).md)
  Removes a specified range of music track events, and shifts later events toward the start of the track to fill in the gap.
- [func MusicTrackGetDestMIDIEndpoint(MusicTrack, UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus](musictrackgetdestmidiendpoint(_:_:).md)
  Gets the MIDI endpoint that is the event target for a music track.
- [func MusicTrackGetDestNode(MusicTrack, UnsafeMutablePointer<AUNode>) -> OSStatus](musictrackgetdestnode(_:_:).md)
  Gets the audio unit node that is the event target for a music track.
- [func MusicTrackGetProperty(MusicTrack, UInt32, UnsafeMutableRawPointer, UnsafeMutablePointer<UInt32>) -> OSStatus](musictrackgetproperty(_:_:_:_:).md)
  Gets a music track property value.
- [func MusicTrackGetSequence(MusicTrack, UnsafeMutablePointer<MusicSequence?>) -> OSStatus](musictrackgetsequence(_:_:).md)
  Gets the music sequence that the music track is a member of.
- [func MusicTrackMerge(MusicTrack, MusicTimeStamp, MusicTimeStamp, MusicTrack, MusicTimeStamp) -> OSStatus](musictrackmerge(_:_:_:_:_:).md)
  Copies a range of events from one music track and merges them into another music track.
- [func MusicTrackMoveEvents(MusicTrack, MusicTimeStamp, MusicTimeStamp, MusicTimeStamp) -> OSStatus](musictrackmoveevents(_:_:_:_:).md)
  Shifts music track events forward or backward in time, in terms of beats.
- [func MusicTrackNewAUPresetEvent(MusicTrack, MusicTimeStamp, UnsafePointer<AUPresetEvent>) -> OSStatus](musictracknewaupresetevent(_:_:_:).md)
  Adds an event of type `AUPresetEvent` to a music track.
- [func MusicTrackNewExtendedNoteEvent(MusicTrack, MusicTimeStamp, UnsafePointer<ExtendedNoteOnEvent>) -> OSStatus](musictracknewextendednoteevent(_:_:_:).md)
  Adds an event of type `ExtendedNoteOnEvent` to a music track.
- [func MusicTrackNewExtendedTempoEvent(MusicTrack, MusicTimeStamp, Float64) -> OSStatus](musictracknewextendedtempoevent(_:_:_:).md)
  Adds a tempo to a music track.
- [func MusicTrackNewMIDIChannelEvent(MusicTrack, MusicTimeStamp, UnsafePointer<MIDIChannelMessage>) -> OSStatus](musictracknewmidichannelevent(_:_:_:).md)
  Adds an event of type `MIDIChannelMessage` to a music track.
- [func MusicTrackNewMIDINoteEvent(MusicTrack, MusicTimeStamp, UnsafePointer<MIDINoteMessage>) -> OSStatus](musictracknewmidinoteevent(_:_:_:).md)
  Adds an event of type `MIDINoteMessage` to a music track.
- [func MusicTrackNewMIDIRawDataEvent(MusicTrack, MusicTimeStamp, UnsafePointer<MIDIRawData>) -> OSStatus](musictracknewmidirawdataevent(_:_:_:).md)
  Adds an event of type `MIDIRawData` to a music track.
- [func MusicTrackNewMetaEvent(MusicTrack, MusicTimeStamp, UnsafePointer<MIDIMetaEvent>) -> OSStatus](musictracknewmetaevent(_:_:_:).md)
  Adds an event of type `MIDIMetaEvent` to a music track.
- [func MusicTrackNewParameterEvent(MusicTrack, MusicTimeStamp, UnsafePointer<ParameterEvent>) -> OSStatus](musictracknewparameterevent(_:_:_:).md)
  Adds an event of type `ParameterEvent` to a music track.
- [func MusicTrackNewUserEvent(MusicTrack, MusicTimeStamp, UnsafePointer<MusicEventUserData>) -> OSStatus](musictracknewuserevent(_:_:_:).md)
  Adds an event of type `MusicEventUserData` to a music track.
- [func MusicTrackSetDestMIDIEndpoint(MusicTrack, MIDIEndpointRef) -> OSStatus](musictracksetdestmidiendpoint(_:_:).md)
  Sets the music track’s event target to a MIDI endpoint.
- [func MusicTrackSetDestNode(MusicTrack, AUNode) -> OSStatus](musictracksetdestnode(_:_:).md)
  Sets the music track’s event target to an audio unit node.
- [func MusicTrackSetProperty(MusicTrack, UInt32, UnsafeMutableRawPointer, UInt32) -> OSStatus](musictracksetproperty(_:_:_:_:).md)
  Sets a music track property value.
- [typealias MusicTrack](musictrack.md)
  A music track consists of a series of music events, each timestamped using units of beats.
- [struct MusicTrackLoopInfo](musictrackloopinfo.md)
  Supports control of the looping behavior of a music track.
- [struct MIDIChannelMessage](midichannelmessage.md)
  Describes a MIDI channel message.
- [struct MIDIMetaEvent](midimetaevent.md)
  Describes a MIDI metaevent such as lyric text, time signature, and so on.
- [struct MIDINoteMessage](midinotemessage.md)
  Describes a MIDI note.
- [struct MIDIRawData](midirawdata.md)
  Describes a MIDI system-exclusive (SysEx) message.
### Interacting with Music Devices
- [func MusicDeviceMIDIEvent(MusicDeviceComponent, UInt32, UInt32, UInt32, UInt32) -> OSStatus](musicdevicemidievent(_:_:_:_:_:).md)
- [func MusicDeviceMIDIEventList(MusicDeviceComponent, UInt32, UnsafePointer<MIDIEventList>) -> OSStatus](musicdevicemidieventlist(_:_:_:).md)
- [func MusicDeviceStartNote(MusicDeviceComponent, MusicDeviceInstrumentID, MusicDeviceGroupID, UnsafeMutablePointer<NoteInstanceID>, UInt32, UnsafePointer<MusicDeviceNoteParams>) -> OSStatus](musicdevicestartnote(_:_:_:_:_:_:).md)
- [func MusicDeviceStopNote(MusicDeviceComponent, MusicDeviceGroupID, NoteInstanceID, UInt32) -> OSStatus](musicdevicestopnote(_:_:_:_:).md)
- [func MusicDeviceSysEx(MusicDeviceComponent, UnsafePointer<UInt8>, UInt32) -> OSStatus](musicdevicesysex(_:_:_:).md)
- [typealias MusicDeviceComponent](musicdevicecomponent.md)
- [typealias MusicDeviceGroupID](musicdevicegroupid.md)
- [typealias MusicDeviceInstrumentID](musicdeviceinstrumentid.md)
- [typealias MusicDeviceMIDIEventProc](musicdevicemidieventproc.md)
- [typealias MusicDeviceStartNoteProc](musicdevicestartnoteproc.md)
- [typealias MusicDeviceStopNoteProc](musicdevicestopnoteproc.md)
- [typealias MusicDeviceSysExProc](musicdevicesysexproc.md)
### Enumerations
- [Music Instrument Audio Unit Subtypes](1619498-music-instrument-audio-unit-subt.md)
- [Music Track Properties](1515456-music-track-properties.md)
  Properties for music tracks.
- [struct MusicSequenceFileFlags](musicsequencefileflags.md)
  Flags that configure the behavior of the [`MusicSequenceFileCreate(_:_:_:_:_:)`](musicsequencefilecreate(_:_:_:_:_:).md) and [`MusicSequenceFileCreateData(_:_:_:_:_:)`](musicsequencefilecreatedata(_:_:_:_:_:).md) functions.
- [enum MusicSequenceFileTypeID](musicsequencefiletypeid.md)
  The various types of files that can be parsed by a music sequence.
- [struct MusicSequenceLoadFlags](musicsequenceloadflags.md)
  Flags used to configure the behavior of the [`MusicSequenceFileLoad(_:_:_:_:)`](musicsequencefileload(_:_:_:_:).md) and [`MusicSequenceFileLoadData(_:_:_:_:)`](musicsequencefileloaddata(_:_:_:_:).md) functions.
- [enum MusicSequenceType](musicsequencetype.md)
  The various types of music sequences.
- [Music Extended Control Event Type](1515446-music-extended-control-event-typ.md)
- [Music Player Errors](1515472-music-player-errors.md)
- [Music Event Types](1515479-music-event-types.md)
- [Music Note Events](1473494-music-note-events.md)
- [Music Device Selectors](1473469-music-device-selectors.md)
- [Music Device Properties](1533931-music-device-properties.md)
- [Music Device Sample Frame Mask](1533978-music-device-sample-frame-mask.md)
- [Music Device Unit Properties](1533963-music-device-unit-properties.md)
- [Instrument Types](1534202-instrument-types.md)
- [Music Device Generic Properties](1533930-music-device-generic-properties.md)
- [Music Effect and Instrument Unit Properties](1533941-music-effect-and-instrument-unit.md)
- [DLS Music Device Properties](1534153-dls-music-device-properties.md)
- [DLS Music Device Parameters](1389667-dls-music-device-parameters.md)

## See Also

- [Audio Queue Services](audio-queue-services.md)
  Connect to audio hardware and manage the recording or playback process.
- [Audio Services](audio-services.md)
  Play short sounds or trigger a vibration effect on iOS devices with the appropriate hardware.
- [Anchoring sound to a window or volume](spatializing-sound-from-a-uiscene.md)
  Provide unique app experiences by attaching sounds to windows and volumes in 3D space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/music-player)*