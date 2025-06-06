# kAudioOutputUnitProperty_StartTimestampsAtZero

**Framework**: Audio Toolbox  
**Kind**: var

A read/write `UInt32` value valid on the audio unit global scope.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var kAudioOutputUnitProperty_StartTimestampsAtZero: AudioUnitPropertyID { get }
```

## See Also

- [var kAudioOutputUnitProperty_ChannelMap: AudioUnitPropertyID](kaudiooutputunitproperty_channelmap.md)
- [var kAudioOutputUnitProperty_CurrentDevice: AudioUnitPropertyID](kaudiooutputunitproperty_currentdevice.md)
  A read/write audio device ID object, of type `AudioDeviceID`, valid on the audio unit global scope.
- [var kAudioOutputUnitProperty_EnableIO: AudioUnitPropertyID](kaudiooutputunitproperty_enableio.md)
  Specifies whether audio I/O is enabled for an I/O unit bus-scope combination.
- [var kAudioOutputUnitProperty_HasIO: AudioUnitPropertyID](kaudiooutputunitproperty_hasio.md)
- [var kAudioOutputUnitProperty_SetInputCallback: AudioUnitPropertyID](kaudiooutputunitproperty_setinputcallback.md)
  A read/write `AURenderCallbackStruct` data structure valid on the audio unit global scope. When an output unit has been enabled for input operation, this callback can be used to provide a single callback to the host application from the input I/O proc, in order to notify the host that input is available and may be obtained by calling the `AudioUnitRender` function.
- [var kAudioOutputUnitProperty_StartTime: AudioUnitPropertyID](kaudiooutputunitproperty_starttime.md)
  A write-only `AudioOutputUnitStartAtTimeParams` data structure valid on the audio unit global scope. When this property is set on an output unit, it will cause the next Start request (but no subsequent Starts) to use the AudioDeviceStartAtTime function, using the specified timestamp, passing false for `inRequestedStartTimeIsInput`.
- [var kAudioOutputUnitProperty_IsRunning: AudioUnitPropertyID](kaudiooutputunitproperty_isrunning.md)
  Indicates whether an audio unit is running (`TRUE`) or not (`FALSE`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiooutputunitproperty_starttimestampsatzero)*