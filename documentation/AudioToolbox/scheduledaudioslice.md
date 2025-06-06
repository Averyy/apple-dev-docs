# ScheduledAudioSlice

**Framework**: Audio Toolbox  
**Kind**: struct

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct ScheduledAudioSlice
```

## Topics

### Initializers
- [init(mTimeStamp: AudioTimeStamp, mCompletionProc: ScheduledAudioSliceCompletionProc?, mCompletionProcUserData: UnsafeMutableRawPointer, mFlags: AUScheduledAudioSliceFlags, mReserved: UInt32, mReserved2: UnsafeMutableRawPointer?, mNumberFrames: UInt32, mBufferList: UnsafeMutablePointer<AudioBufferList>)](scheduledaudioslice/init(mtimestamp:mcompletionproc:mcompletionprocuserdata:mflags:mreserved:mreserved2:mnumberframes:mbufferlist:).md)
### Instance Properties
- [var mBufferList: UnsafeMutablePointer<AudioBufferList>](scheduledaudioslice/mbufferlist.md)
- [var mCompletionProc: ScheduledAudioSliceCompletionProc?](scheduledaudioslice/mcompletionproc.md)
- [var mCompletionProcUserData: UnsafeMutableRawPointer](scheduledaudioslice/mcompletionprocuserdata.md)
- [var mFlags: AUScheduledAudioSliceFlags](scheduledaudioslice/mflags.md)
- [var mNumberFrames: UInt32](scheduledaudioslice/mnumberframes.md)
- [var mReserved: UInt32](scheduledaudioslice/mreserved.md)
- [var mReserved2: UnsafeMutableRawPointer?](scheduledaudioslice/mreserved2.md)
- [var mTimeStamp: AudioTimeStamp](scheduledaudioslice/mtimestamp.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct ScheduledAudioFileRegion](scheduledaudiofileregion.md)
- [typealias ScheduledAudioFileRegionCompletionProc](scheduledaudiofileregioncompletionproc.md)
- [typealias ScheduledAudioSliceCompletionProc](scheduledaudioslicecompletionproc.md)
- [typealias MIDIChannelNumber](midichannelnumber.md)
  MIDI Channel, 0~15 (channels 1 through 16, respectively).
- [typealias AUAudioObjectID](auaudioobjectid.md)
- [typealias AUMIDICIProfileChangedBlock](aumidiciprofilechangedblock.md)
- [typealias AUAudioChannelCount](auaudiochannelcount.md)
  A number of audio channels.
- [typealias AUAudioFrameCount](auaudioframecount.md)
  A number of audio sample frames.
- [typealias AUAudioUnitStatus](auaudiounitstatus.md)
  A result code returned from an audio unit’s render function.
- [typealias AUEventListenerProc](aueventlistenerproc.md)
- [typealias AUEventListenerRef](aueventlistenerref.md)
- [typealias AUEventSampleTime](aueventsampletime.md)
  Expresses time as a sample count.
- [typealias AUImplementorValueObserver](auimplementorvalueobserver.md)
  A block called to notify the audio unit implementation of changes to a parameter value.
- [typealias AUImplementorValueProvider](auimplementorvalueprovider.md)
  A block called to fetch a parameter’s current value from the audio unit implementation.
- [typealias AUInputHandler](auinputhandler.md)
  A block to notify the host of an I/O unit that an input is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/scheduledaudioslice)*