# ParameterValueStream

**Framework**: AudioDriverKit  
**Kind**: case

A format for a side-chain of 32-bit floating-point data.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
ParameterValueStream
```

#### Discussion

The data in this kind of stream flows to or from an Audio Unit to send a high density of parameter value control information. An Audio Unit typically runs a [`ParameterValueStream`](audiodriverkit/iouseraudioformatid/parametervaluestream.md) at the sample rate of the AudioUnit’s audio data. It can also use some integer divisor of this rate, such as a half or a third of the audio’s sample rate. The sample rate of the [`IOUserAudioStreamBasicDescription`](audiodriverkit/iouseraudiostreambasicdescription.md) describes this relationship.

This format uses no flags.

## See Also

- [MIDIStream](audiodriverkit/iouseraudioformatid/midistream.md)
  A format for a stream of MIDI packet lists.
- [TimeCode](audiodriverkit/iouseraudioformatid/timecode.md)
  A format for a stream of time stamps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudioformatid/parametervaluestream)*