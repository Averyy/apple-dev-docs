# AudioUnitPropertyListenerProc

**Framework**: Audio Toolbox  
**Kind**: typealias

Called by the system when the value of a specified audio unit property has changed.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias AudioUnitPropertyListenerProc = (UnsafeMutableRawPointer, AudioUnit, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement) -> Void
```

#### Return Value

A result code.

#### Discussion

If you named your callback function `MyAudioUnitPropertyListenerProc`, you would declare it like this:

##### Discussion

You register your `AudioUnitPropertyListenerProc` callback function using the [`AudioUnitAddPropertyListener(_:_:_:_:)`](audiounitaddpropertylistener(_:_:_:_:).md) function.

## Parameters

- `inRefCon`: Custom data that you provided when registering your callback with the audio unit.
- `inUnit`: The audio unit upon which the specified property value has changed.
- `inID`: The property whose value has changed.
- `inScope`: The scope of the property whose value has changed.
- `inElement`: The element ID on the scope of the property whose value has changed.

## See Also

- [struct ScheduledAudioFileRegion](scheduledaudiofileregion.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitpropertylistenerproc)*