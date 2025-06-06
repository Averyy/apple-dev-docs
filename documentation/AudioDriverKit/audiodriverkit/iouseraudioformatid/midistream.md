# MIDIStream

**Framework**: AudioDriverKit  
**Kind**: case

A format for a stream of MIDI packet lists.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
MIDIStream
```

#### Discussion

This format describes a stream of [`MIDIPacketList`](https://developer.apple.com/documentation/CoreMIDI/MIDIPacketList) instances where the time stamps in the [`MIDIPacketList`](https://developer.apple.com/documentation/CoreMIDI/MIDIPacketList) are sample offsets in the stream. The [`mSampleRate`](audiodriverkit/iouseraudiostreambasicdescription/msamplerate.md) field describes how the stream passes time. This allows an Audio Unit that receives or generates this stream to define the time for any MIDI event within this list. It does so by using the sample rate, the number of frames it renders and the sample offsets within the [`MIDIPacketList`](https://developer.apple.com/documentation/CoreMIDI/MIDIPacketList).

This format uses no flags.

## See Also

- [ParameterValueStream](audiodriverkit/iouseraudioformatid/parametervaluestream.md)
  A format for a side-chain of 32-bit floating-point data.
- [TimeCode](audiodriverkit/iouseraudioformatid/timecode.md)
  A format for a stream of time stamps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudioformatid/midistream)*