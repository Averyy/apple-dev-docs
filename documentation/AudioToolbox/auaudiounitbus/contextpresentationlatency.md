# contextPresentationLatency

**Framework**: Audio Toolbox  
**Kind**: property

Information about latency in the audio unit’s processing context.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var contextPresentationLatency: TimeInterval { get set }
```

#### Discussion

A host may set this property to describe the presentation latency, in seconds, of its input and/or output audio data. A value of `0` means either no latency or unknown latency.

A host should set this property on each active bus, since, for example, the audio routing path to each of multiple output busses may differ. The meaning of this property’s value differs between input and output busses, as described below:

- For  busses, this value describes how long ago the audio arriving on this bus was acquired.

For example, when reading from a file to the first audio unit in a chain, the input presentation latency is zero. For audio input from a device, this initial input latency is the presentation latency of the device itself (i.e. the device’s offset and latency). A second chained audio unit’s input presentation latency is the input presentation latency of the first unit, plus the processing latency of the first unit.

- For  busses, this value describes how long it will be before the output audio of an audio unit is presented.

For example, when writing to a file, the output presentation latency of the last audio unit in a chain is zero. When the audio from that audio unit is to be played to a device, then that initial presentation latency will be the presentation latency of the device itself (i.e. the I/O buffer size) plus the device’s safety offset and latency. A previously chained audio unit’s output presentation latency is the last unit’s presentation latency plus its processing latency.

For a given audio unit anywhere within a mixing graph, the input and output presentation latencies describe to that unit how long from the moment of generation it has taken for its input to arrive, and how long it will take for its output to be presented.

This version 3 property is bridged to the version 2 `kAudioUnitProperty_PresentationLatency` API.

> ❗ **Important**:  This property does not describe the same value as the audio unit’s [`latency`](auaudiounit/latency.md) property, with which the audio unit describes to the host any processing latency it introduces between its input and output.

 This property does not describe the same value as the audio unit’s [`latency`](auaudiounit/latency.md) property, with which the audio unit describes to the host any processing latency it introduces between its input and output.

## See Also

- [func setFormat(AVAudioFormat) throws](auaudiounitbus/setformat(_:).md)
  Sets the bus’s audio format.
- [var format: AVAudioFormat](auaudiounitbus/format.md)
  The audio format and channel layout of audio being transferred on the bus.
- [var isEnabled: Bool](auaudiounitbus/isenabled.md)
  Determines whether the bus is active.
- [var name: String?](auaudiounitbus/name.md)
  A name for the bus.
- [var index: Int](auaudiounitbus/index.md)
  The index of this bus in its containing array.
- [var busType: AUAudioUnitBusType](auaudiounitbus/bustype.md)
  The bus type.
- [var ownerAudioUnit: AUAudioUnit](auaudiounitbus/owneraudiounit.md)
  The audio unit that owns the bus.
- [var supportedChannelLayoutTags: [NSNumber]?](auaudiounitbus/supportedchannellayouttags.md)
  An array of audio channel layout tags.
- [var shouldAllocateBuffer: Bool](auaudiounitbus/shouldallocatebuffer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/contextpresentationlatency)*