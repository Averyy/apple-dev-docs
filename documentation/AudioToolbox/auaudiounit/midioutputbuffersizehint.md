# midiOutputBufferSizeHint

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
var midiOutputBufferSizeHint: Int { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic) NSInteger MIDIOutputBufferSizeHint;
```

*macOS*

```objc
@property (atomic) NSInteger MIDIOutputBufferSizeHint;
```

## See Also

### Customizing the Audio Unit Behavior
- [class func registerSubclass(AnyClass, as: AudioComponentDescription, name: String, version: UInt32)](./registersubclass%28_,as,name,version%29.md)
  Registers an audio unit subclass.
- [func shouldChange(to: AVAudioFormat, for: AUAudioUnitBus) -> Bool](./shouldchange%28to,for%29.md)
  This is called when you set the format on a bus.
- [func setRenderResourcesAllocated(Bool)](./setrenderresourcesallocated%28_%29.md)
  Sets the Boolean value of the [`renderResourcesAllocated`](./renderresourcesallocated.md) property.
- [var internalRenderBlock: AUInternalRenderBlock](./internalrenderblock.md)
  The block which you must provide, via a getter, in order to implement rendering.
- [typealias AUInternalRenderBlock](../auinternalrenderblock.md)
  A block to render the audio unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/midioutputbuffersizehint)*