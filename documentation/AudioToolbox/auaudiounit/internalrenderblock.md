# internalRenderBlock

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

The block which you must provide, via a getter, in order to implement rendering.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var internalRenderBlock: AUInternalRenderBlock { get }
```

```objc
@property (nonatomic, readonly) AUInternalRenderBlock internalRenderBlock;
```

## See Also

### Customizing the Audio Unit Behavior
- [class func registerSubclass(AnyClass, as: AudioComponentDescription, name: String, version: UInt32)](./registersubclass%28_,as,name,version%29.md)
  Registers an audio unit subclass.
- [func shouldChange(to: AVAudioFormat, for: AUAudioUnitBus) -> Bool](./shouldchange%28to,for%29.md)
  This is called when you set the format on a bus.
- [func setRenderResourcesAllocated(Bool)](./setrenderresourcesallocated%28_%29.md)
  Sets the Boolean value of the [`renderResourcesAllocated`](./renderresourcesallocated.md) property.
- [var midiOutputBufferSizeHint: Int](./midioutputbuffersizehint.md)
- [typealias AUInternalRenderBlock](../auinternalrenderblock.md)
  A block to render the audio unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/internalrenderblock)*