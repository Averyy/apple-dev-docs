# shouldAllocateBuffer

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

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

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic) BOOL shouldAllocateBuffer;
```

*macOS*

```objc
@property (atomic) BOOL shouldAllocateBuffer;
```

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
- [var supportedChannelLayoutTags: [NSNumber]?](./supportedchannellayouttags.md)
  An array of audio channel layout tags.
- [var contextPresentationLatency: TimeInterval](./contextpresentationlatency.md)
  Information about latency in the audio unit’s processing context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/shouldallocatebuffer)*