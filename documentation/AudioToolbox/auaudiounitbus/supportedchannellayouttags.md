# supportedChannelLayoutTags

**Framework**: Audio Toolbox  
**Kind**: property

An array of audio channel layout tags.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var supportedChannelLayoutTags: [NSNumber]? { get }
```

#### Discussion

The array contains [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) objects representing [`AudioChannelLayoutTag`](https://developer.apple.com/documentation/CoreAudioTypes/AudioChannelLayoutTag) values.

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
- [var contextPresentationLatency: TimeInterval](auaudiounitbus/contextpresentationlatency.md)
  Information about latency in the audio unit’s processing context.
- [var shouldAllocateBuffer: Bool](auaudiounitbus/shouldallocatebuffer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/supportedchannellayouttags)*