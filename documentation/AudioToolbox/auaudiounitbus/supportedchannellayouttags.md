# supportedChannelLayoutTags

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

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

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<NSNumber *> * supportedChannelLayoutTags;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSArray<NSNumber *> * supportedChannelLayoutTags;
```

#### Discussion

The array contains [`NSNumber`](../../Foundation/nsnumber.md) objects representing [`AudioChannelLayoutTag`](../../CoreAudioTypes/audiochannellayouttag.md) values.

## See Also

### Bus Methods and Properties
- [func setFormat(AVAudioFormat) throws](./setformat%28_%29.md)
  Sets the bus’s audio format.
- [var format: AVAudioFormat](./format.md)
  The audio format and channel layout of audio being transferred on the bus.
- [var isEnabled: Bool](./isenabled.md)
  Determines whether the bus is active.
- [var name: String?](./name.md)
  A name for the bus.
- [var index: Int](./index.md)
  The index of this bus in its containing array.
- [var busType: AUAudioUnitBusType](./bustype.md)
  The bus type.
- [var ownerAudioUnit: AUAudioUnit](./owneraudiounit.md)
  The audio unit that owns the bus.
- [var contextPresentationLatency: TimeInterval](./contextpresentationlatency.md)
  Information about latency in the audio unit’s processing context.
- [var shouldAllocateBuffer: Bool](./shouldallocatebuffer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/supportedchannellayouttags)*