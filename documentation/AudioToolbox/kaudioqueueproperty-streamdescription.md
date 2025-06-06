# kAudioQueueProperty_StreamDescription

**Framework**: Audio Toolbox  
**Kind**: var

An audio queue’s data format.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var kAudioQueueProperty_StreamDescription: AudioQueuePropertyID { get }
```

#### Discussion

Value is a read-only [`AudioStreamBasicDescription`](https://developer.apple.com/documentation/CoreAudioTypes/AudioStreamBasicDescription) structure, indicating an audio queue’s data format. Primarily useful for obtaining a complete ASBD when recording, in cases where you initially specify a sample rate of `0`.

## See Also

- [var kAudioQueueDeviceProperty_NumberChannels: AudioQueuePropertyID](kaudioqueuedeviceproperty_numberchannels.md)
  Value is a read-only `UInt32` value representing the number of channels in the audio hardware device associated with an audio queue.
- [var kAudioQueueDeviceProperty_SampleRate: AudioQueuePropertyID](kaudioqueuedeviceproperty_samplerate.md)
  Value is a read-only `Float64` value representing the sampling rate of the audio hardware device associated with an audio queue.
- [var kAudioQueueProperty_ChannelLayout: AudioQueuePropertyID](kaudioqueueproperty_channellayout.md)
  Describes an audio queue channel layout.
- [var kAudioQueueProperty_ConverterError: AudioQueuePropertyID](kaudioqueueproperty_convertererror.md)
  Value is a  read-only `UInt32` value that indicates the most recent error (if any) encountered by the audio queue’s internal encoding/decoding process.
- [var kAudioQueueProperty_CurrentDevice: AudioQueuePropertyID](kaudioqueueproperty_currentdevice.md)
  The unique identifier (UID) of the audio hardware device.
- [var kAudioQueueProperty_CurrentLevelMeter: AudioQueuePropertyID](kaudioqueueproperty_currentlevelmeter.md)
  A read-only array of level meter status structures.
- [var kAudioQueueProperty_CurrentLevelMeterDB: AudioQueuePropertyID](kaudioqueueproperty_currentlevelmeterdb.md)
  Value is a read-only array of [`AudioQueueLevelMeterState`](audioqueuelevelmeterstate.md) structures, one array element per audio channel. The member values in the structure are in decibels.
- [var kAudioQueueProperty_DecodeBufferSizeFrames: AudioQueuePropertyID](kaudioqueueproperty_decodebuffersizeframes.md)
  Value is a read/write `UInt32` value that is the size of the buffer into which a playback (output) audio queue decodes buffers. A larger buffer provides more reliability and  better long-term performance at the expense of memory and decreased responsiveness in some situations.
- [var kAudioQueueProperty_EnableLevelMetering: AudioQueuePropertyID](kaudioqueueproperty_enablelevelmetering.md)
  Value is a read/write `UInt32` value that indicates whether audio level metering is enabled for an audio queue. `0` = metering off, `1` = metering on.
- [var kAudioQueueProperty_EnableTimePitch: AudioQueuePropertyID](kaudioqueueproperty_enabletimepitch.md)
- [var kAudioQueueProperty_IsRunning: AudioQueuePropertyID](kaudioqueueproperty_isrunning.md)
  Value is a read-only `UInt32` value indicating whether or not the audio queue is running. A nonzero value means running; `0` means stopped. A notification is sent when the associated audio queue starts or stops, which may occur sometime after the [`AudioQueueStart(_:_:)`](audioqueuestart(_:_:).md) or [`AudioQueueStop(_:_:)`](audioqueuestop(_:_:).md) function is called.
- [var kAudioQueueProperty_MagicCookie: AudioQueuePropertyID](kaudioqueueproperty_magiccookie.md)
  Value is a read/write void pointer to a block of memory, which you set up, containing an audio format magic cookie. If the audio format you are playing or recording to requires a magic cookie, you must set a value for this property before enqueuing any buffers.
- [var kAudioQueueProperty_MaximumOutputPacketSize: AudioQueuePropertyID](kaudioqueueproperty_maximumoutputpacketsize.md)
  Value is a read-only`UInt32` value that is the size, in bytes, of the largest single packet of data in the output format. Primarily useful when encoding VBR compressed data.
- [var kAudioQueueProperty_TimePitchAlgorithm: AudioQueuePropertyID](kaudioqueueproperty_timepitchalgorithm.md)
- [var kAudioQueueProperty_TimePitchBypass: AudioQueuePropertyID](kaudioqueueproperty_timepitchbypass.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueproperty_streamdescription)*