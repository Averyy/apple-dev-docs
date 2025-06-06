# ScheduledAudioFileRegion

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
struct ScheduledAudioFileRegion
```

## Topics

### Initializers
- [init(mTimeStamp: AudioTimeStamp, mCompletionProc: ScheduledAudioFileRegionCompletionProc?, mCompletionProcUserData: UnsafeMutableRawPointer?, mAudioFile: OpaquePointer, mLoopCount: UInt32, mStartFrame: Int64, mFramesToPlay: UInt32)](scheduledaudiofileregion/init(mtimestamp:mcompletionproc:mcompletionprocuserdata:maudiofile:mloopcount:mstartframe:mframestoplay:).md)
### Instance Properties
- [var mAudioFile: OpaquePointer](scheduledaudiofileregion/maudiofile.md)
  Must be a valid and already-open audio file object (of type `AudioFileID`), as declared in `AudioToolbox/AudioFile.h`.
- [var mCompletionProc: ScheduledAudioFileRegionCompletionProc?](scheduledaudiofileregion/mcompletionproc.md)
  may be `NULL`
- [var mCompletionProcUserData: UnsafeMutableRawPointer?](scheduledaudiofileregion/mcompletionprocuserdata.md)
- [var mFramesToPlay: UInt32](scheduledaudiofileregion/mframestoplay.md)
  The number of frames to play.
- [var mLoopCount: UInt32](scheduledaudiofileregion/mloopcount.md)
  `0` = do not loop
- [var mStartFrame: Int64](scheduledaudiofileregion/mstartframe.md)
  The frame offset into the file.
- [var mTimeStamp: AudioTimeStamp](scheduledaudiofileregion/mtimestamp.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct ScheduledAudioSlice](scheduledaudioslice.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/scheduledaudiofileregion)*