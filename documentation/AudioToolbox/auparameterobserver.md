# AUParameterObserver

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

A block called after the value of a parameter changes.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
typealias AUParameterObserver = (AUParameterAddress, AUValue) -> Void
```

```c
typedef void (^)(unsigned long long, float) AUParameterObserver;
```

## Discussion

The block takes the following parameters:

- **address**: The address of the parameter.
- **value**: The current value of the parameter.

## See Also

### Related Documentation
- [func token(byAddingParameterObserver: AUParameterObserver) -> AUParameterObserverToken](./auparameternode/token%28byaddingparameterobserver%29.md)
  Adds an observer for a single parameter or all parameters in a group.
### Audio Unit Types
- [struct ScheduledAudioFileRegion](./scheduledaudiofileregion.md)
- [struct ScheduledAudioSlice](./scheduledaudioslice.md)
- [typealias ScheduledAudioFileRegionCompletionProc](./scheduledaudiofileregioncompletionproc.md)
- [typealias ScheduledAudioSliceCompletionProc](./scheduledaudioslicecompletionproc.md)
- [typealias MIDIChannelNumber](./midichannelnumber.md)
  MIDI Channel, 0~15 (channels 1 through 16, respectively).
- [typealias AUAudioObjectID](./auaudioobjectid.md)
- [typealias AUMIDICIProfileChangedBlock](./aumidiciprofilechangedblock.md)
- [typealias AUAudioChannelCount](./auaudiochannelcount.md)
  A number of audio channels.
- [typealias AUAudioFrameCount](./auaudioframecount.md)
  A number of audio sample frames.
- [typealias AUAudioUnitStatus](./auaudiounitstatus.md)
  A result code returned from an audio unit’s render function.
- [typealias AUEventListenerProc](./aueventlistenerproc.md)
- [typealias AUEventListenerRef](./aueventlistenerref.md)
- [typealias AUEventSampleTime](./aueventsampletime.md)
  Expresses time as a sample count.
- [typealias AUImplementorValueObserver](./auimplementorvalueobserver.md)
  A block called to notify the audio unit implementation of changes to a parameter value.
- [typealias AUImplementorValueProvider](./auimplementorvalueprovider.md)
  A block called to fetch a parameter’s current value from the audio unit implementation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparameterobserver)*