# isEnabled

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

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

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, getter=isEnabled) BOOL enabled;
```

*macOS*

```objc
@property (atomic, getter=isEnabled) BOOL enabled;
```

#### Discussion

Hosts must enable input busses before using them. This allows an audio unit to be prepared to render a large number of inputs, but avoid the work of preparing to pull inputs which are not in use.

This version 3 property is bridged to the version 2 `kAudioUnitProperty_MakeConnection` and `kAudioUnitProperty_SetRenderCallback` APIs.

## See Also

### Bus Methods and Properties
- [func setFormat(AVAudioFormat) throws](./setformat%28_%29.md)
  Sets the bus’s audio format.
- [var format: AVAudioFormat](./format.md)
  The audio format and channel layout of audio being transferred on the bus.
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
- [var shouldAllocateBuffer: Bool](./shouldallocatebuffer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/isenabled)*