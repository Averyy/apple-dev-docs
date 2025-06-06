# Clock Utilities

**Framework**: Audio Toolbox

Manage time-related information associated with audio playback.

## Topics

### Creating a Clock
- [func CAClockNew(UInt32, UnsafeMutablePointer<CAClockRef?>) -> OSStatus](caclocknew(_:_:).md)
- [func CAClockDispose(CAClockRef) -> OSStatus](caclockdispose(_:).md)
- [typealias CAClockRef](caclockref.md)
### Starting and Stopping the Clock
- [func CAClockStart(CAClockRef) -> OSStatus](caclockstart(_:).md)
- [func CAClockStop(CAClockRef) -> OSStatus](caclockstop(_:).md)
- [func CAClockArm(CAClockRef) -> OSStatus](caclockarm(_:).md)
- [func CAClockDisarm(CAClockRef) -> OSStatus](caclockdisarm(_:).md)
### Adding and Removing Listeners
- [func CAClockAddListener(CAClockRef, CAClockListenerProc, UnsafeMutableRawPointer) -> OSStatus](caclockaddlistener(_:_:_:).md)
- [func CAClockRemoveListener(CAClockRef, CAClockListenerProc, UnsafeMutableRawPointer) -> OSStatus](caclockremovelistener(_:_:_:).md)
- [typealias CAClockListenerProc](caclocklistenerproc.md)
- [enum CAClockMessage](caclockmessage.md)
### Accessing the Current Time
- [func CAClockGetCurrentTime(CAClockRef, CAClockTimeFormat, UnsafeMutablePointer<CAClockTime>) -> OSStatus](caclockgetcurrenttime(_:_:_:).md)
- [func CAClockSetCurrentTime(CAClockRef, UnsafePointer<CAClockTime>) -> OSStatus](caclocksetcurrenttime(_:_:).md)
- [func CAClockGetStartTime(CAClockRef, CAClockTimeFormat, UnsafeMutablePointer<CAClockTime>) -> OSStatus](caclockgetstarttime(_:_:_:).md)
- [struct CAClockTime](caclocktime.md)
- [enum CAClockTimeFormat](caclocktimeformat.md)
- [typealias CAClockSamples](caclocksamples.md)
### Accessing Tempo Information
- [func CAClockGetCurrentTempo(CAClockRef, UnsafeMutablePointer<CAClockTempo>, UnsafeMutablePointer<CAClockTime>?) -> OSStatus](caclockgetcurrenttempo(_:_:_:).md)
- [func CAClockSetCurrentTempo(CAClockRef, CAClockTempo, UnsafePointer<CAClockTime>?) -> OSStatus](caclocksetcurrenttempo(_:_:_:).md)
- [func CAClockGetPlayRate(CAClockRef, UnsafeMutablePointer<Float64>) -> OSStatus](caclockgetplayrate(_:_:).md)
- [func CAClockSetPlayRate(CAClockRef, Float64) -> OSStatus](caclocksetplayrate(_:_:).md)
- [typealias CAClockTempo](caclocktempo.md)
- [struct CATempoMapEntry](catempomapentry.md)
### Accessing Clock Properties
- [func CAClockGetProperty(CAClockRef, CAClockPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](caclockgetproperty(_:_:_:_:).md)
- [func CAClockGetPropertyInfo(CAClockRef, CAClockPropertyID, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](caclockgetpropertyinfo(_:_:_:_:).md)
- [func CAClockSetProperty(CAClockRef, CAClockPropertyID, UInt32, UnsafeRawPointer) -> OSStatus](caclocksetproperty(_:_:_:_:).md)
- [enum CAClockPropertyID](caclockpropertyid.md)
- [enum CAClockSyncMode](caclocksyncmode.md)
### Parsing MIDI Data
- [func CAClockParseMIDI(CAClockRef, UnsafePointer<MIDIPacketList>) -> OSStatus](caclockparsemidi(_:_:).md)
### Converting Time Values
- [func CAClockBarBeatTimeToBeats(CAClockRef, UnsafePointer<CABarBeatTime>, UnsafeMutablePointer<CAClockBeats>) -> OSStatus](caclockbarbeattimetobeats(_:_:_:).md)
- [func CAClockBeatsToBarBeatTime(CAClockRef, CAClockBeats, UInt16, UnsafeMutablePointer<CABarBeatTime>) -> OSStatus](caclockbeatstobarbeattime(_:_:_:_:).md)
- [func CAClockSMPTETimeToSeconds(CAClockRef, UnsafePointer<SMPTETime>, UnsafeMutablePointer<CAClockSeconds>) -> OSStatus](caclocksmptetimetoseconds(_:_:_:).md)
- [func CAClockSecondsToSMPTETime(CAClockRef, CAClockSeconds, UInt16, UnsafeMutablePointer<SMPTETime>) -> OSStatus](caclocksecondstosmptetime(_:_:_:_:).md)
- [func CAClockTranslateTime(CAClockRef, UnsafePointer<CAClockTime>, CAClockTimeFormat, UnsafeMutablePointer<CAClockTime>) -> OSStatus](caclocktranslatetime(_:_:_:_:).md)
- [enum CAClockTimebase](caclocktimebase.md)
- [typealias CAClockSeconds](caclockseconds.md)
- [typealias CAClockBeats](caclockbeats.md)
- [typealias CAClockSMPTEFormat](caclocksmpteformat.md)
- [struct CABarBeatTime](cabarbeattime.md)
- [struct CAMeterTrackEntry](cametertrackentry.md)
### Getting Clock-Related Errors
- [Clock Errors](1513526-clock-errors.md)

## See Also

- [Analyzing audio performance with Instruments](analyzing-audio-performance-with-instruments.md)
  Ensure a smooth and immersive audio experience in your apps using Audio System Trace.
- [Audio Converter Services](audio-converter-services.md)
  Convert between linear PCM audio formats, and between linear PCM and compressed formats.
- [Audio Session Support](audio-session-support.md)
  Describe the properties that you associate with audio sessions and audio routes.
- [Audio Toolbox Debugging](audio-toolbox-debugging.md)
  Obtain the internal state of Core Audio objects during the development and debugging of your code.
- [Workgroup Management](workgroup-management.md)
  Coordinate the activity of custom real-time audio threads with those of the system and other processes.
- [Audio Codec](audio-codec.md)
  Translate audio data from one format to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/clock-utilities)*