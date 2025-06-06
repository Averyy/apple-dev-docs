# shouldAllocateBuffer

**Framework**: Audio Toolbox  
**Kind**: property

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var shouldAllocateBuffer: Bool { get set }
```

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
- [var contextPresentationLatency: TimeInterval](auaudiounitbus/contextpresentationlatency.md)
  Information about latency in the audio unit’s processing context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/shouldallocatebuffer)*