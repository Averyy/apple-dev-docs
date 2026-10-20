# Clock Utilities

**Framework**: Audio Toolbox  
**Role**: API Collection

Manage time-related information associated with audio playback.

## Topics

### Creating a Clock
- [func CAClockNew(UInt32, UnsafeMutablePointer<CAClockRef?>) -> OSStatus](./caclocknew%28_,_%29.md)
- [func CAClockDispose(CAClockRef) -> OSStatus](./caclockdispose%28_%29.md)
- [typealias CAClockRef](./caclockref.md)
### Starting and Stopping the Clock
- [func CAClockStart(CAClockRef) -> OSStatus](./caclockstart%28_%29.md)
- [func CAClockStop(CAClockRef) -> OSStatus](./caclockstop%28_%29.md)
- [func CAClockArm(CAClockRef) -> OSStatus](./caclockarm%28_%29.md)
- [func CAClockDisarm(CAClockRef) -> OSStatus](./caclockdisarm%28_%29.md)
### Adding and Removing Listeners
- [func CAClockAddListener(CAClockRef, CAClockListenerProc, UnsafeMutableRawPointer) -> OSStatus](./caclockaddlistener%28_,_,_%29.md)
- [func CAClockRemoveListener(CAClockRef, CAClockListenerProc, UnsafeMutableRawPointer) -> OSStatus](./caclockremovelistener%28_,_,_%29.md)
- [typealias CAClockListenerProc](./caclocklistenerproc.md)
- [enum CAClockMessage](./caclockmessage.md)
### Accessing the Current Time
- [func CAClockGetCurrentTime(CAClockRef, CAClockTimeFormat, UnsafeMutablePointer<CAClockTime>) -> OSStatus](./caclockgetcurrenttime%28_,_,_%29.md)
- [func CAClockSetCurrentTime(CAClockRef, UnsafePointer<CAClockTime>) -> OSStatus](./caclocksetcurrenttime%28_,_%29.md)
- [func CAClockGetStartTime(CAClockRef, CAClockTimeFormat, UnsafeMutablePointer<CAClockTime>) -> OSStatus](./caclockgetstarttime%28_,_,_%29.md)
- [struct CAClockTime](./caclocktime.md)
- [enum CAClockTimeFormat](./caclocktimeformat.md)
- [typealias CAClockSamples](./caclocksamples.md)
### Accessing Tempo Information
- [func CAClockGetCurrentTempo(CAClockRef, UnsafeMutablePointer<CAClockTempo>, UnsafeMutablePointer<CAClockTime>?) -> OSStatus](./caclockgetcurrenttempo%28_,_,_%29.md)
- [func CAClockSetCurrentTempo(CAClockRef, CAClockTempo, UnsafePointer<CAClockTime>?) -> OSStatus](./caclocksetcurrenttempo%28_,_,_%29.md)
- [func CAClockGetPlayRate(CAClockRef, UnsafeMutablePointer<Float64>) -> OSStatus](./caclockgetplayrate%28_,_%29.md)
- [func CAClockSetPlayRate(CAClockRef, Float64) -> OSStatus](./caclocksetplayrate%28_,_%29.md)
- [typealias CAClockTempo](./caclocktempo.md)
- [struct CATempoMapEntry](./catempomapentry.md)
### Accessing Clock Properties
- [func CAClockGetProperty(CAClockRef, CAClockPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./caclockgetproperty%28_,_,_,_%29.md)
- [func CAClockGetPropertyInfo(CAClockRef, CAClockPropertyID, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](./caclockgetpropertyinfo%28_,_,_,_%29.md)
- [func CAClockSetProperty(CAClockRef, CAClockPropertyID, UInt32, UnsafeRawPointer) -> OSStatus](./caclocksetproperty%28_,_,_,_%29.md)
- [enum CAClockPropertyID](./caclockpropertyid.md)
- [enum CAClockSyncMode](./caclocksyncmode.md)
### Parsing MIDI Data
- [func CAClockParseMIDI(CAClockRef, UnsafePointer<MIDIPacketList>) -> OSStatus](./caclockparsemidi%28_,_%29.md)
### Converting Time Values
- [func CAClockBarBeatTimeToBeats(CAClockRef, UnsafePointer<CABarBeatTime>, UnsafeMutablePointer<CAClockBeats>) -> OSStatus](./caclockbarbeattimetobeats%28_,_,_%29.md)
- [func CAClockBeatsToBarBeatTime(CAClockRef, CAClockBeats, UInt16, UnsafeMutablePointer<CABarBeatTime>) -> OSStatus](./caclockbeatstobarbeattime%28_,_,_,_%29.md)
- [func CAClockSMPTETimeToSeconds(CAClockRef, UnsafePointer<SMPTETime>, UnsafeMutablePointer<CAClockSeconds>) -> OSStatus](./caclocksmptetimetoseconds%28_,_,_%29.md)
- [func CAClockSecondsToSMPTETime(CAClockRef, CAClockSeconds, UInt16, UnsafeMutablePointer<SMPTETime>) -> OSStatus](./caclocksecondstosmptetime%28_,_,_,_%29.md)
- [func CAClockTranslateTime(CAClockRef, UnsafePointer<CAClockTime>, CAClockTimeFormat, UnsafeMutablePointer<CAClockTime>) -> OSStatus](./caclocktranslatetime%28_,_,_,_%29.md)
- [enum CAClockTimebase](./caclocktimebase.md)
- [typealias CAClockSeconds](./caclockseconds.md)
- [typealias CAClockBeats](./caclockbeats.md)
- [typealias CAClockSMPTEFormat](./caclocksmpteformat.md)
- [struct CABarBeatTime](./cabarbeattime.md)
- [struct CAMeterTrackEntry](./cametertrackentry.md)
### Getting Clock-Related Errors
- [Clock Errors](./api-1513526-clock-errors.md)

## See Also

### Utilities
- [Analyzing audio performance with Instruments](./analyzing-audio-performance-with-instruments.md)
  Ensure a smooth and immersive audio experience in your apps using Audio System Trace.
- [Audio Converter Services](./audio-converter-services.md)
  Convert between linear PCM audio formats, and between linear PCM and compressed formats.
- [Audio Session Support](./audio-session-support.md)
  Describe the properties that you associate with audio sessions and audio routes.
- [Audio Toolbox Debugging](./audio-toolbox-debugging.md)
  Obtain the internal state of Core Audio objects during the development and debugging of your code.
- [Workgroup Management](./workgroup-management.md)
  Coordinate the activity of custom real-time audio threads with those of the system and other processes.
- [Audio Codec](./audio-codec.md)
  Translate audio data from one format to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/clock-utilities)*