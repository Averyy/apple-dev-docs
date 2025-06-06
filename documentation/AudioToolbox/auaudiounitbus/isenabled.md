# isEnabled

**Framework**: Audio Toolbox  
**Kind**: property

Determines whether the bus is active.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var isEnabled: Bool { get set }
```

#### Discussion

Hosts must enable input busses before using them. This allows an audio unit to be prepared to render a large number of inputs, but avoid the work of preparing to pull inputs which are not in use.

This version 3 property is bridged to the version 2 `kAudioUnitProperty_MakeConnection` and `kAudioUnitProperty_SetRenderCallback` APIs.

## See Also

- [func setFormat(AVAudioFormat) throws](auaudiounitbus/setformat(_:).md)
  Sets the bus’s audio format.
- [var format: AVAudioFormat](auaudiounitbus/format.md)
  The audio format and channel layout of audio being transferred on the bus.
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
- [var contextPresentationLatency: TimeInterval](auaudiounitbus/contextpresentationlatency.md)
  Information about latency in the audio unit’s processing context.
- [var shouldAllocateBuffer: Bool](auaudiounitbus/shouldallocatebuffer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/isenabled)*