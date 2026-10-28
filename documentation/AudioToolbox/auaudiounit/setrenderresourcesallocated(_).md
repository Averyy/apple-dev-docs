# setRenderResourcesAllocated(_:)

**Framework**: Audio Toolbox  
**Kind**: method  
**Role**: Instance Method

Sets the Boolean value of the [`renderResourcesAllocated`](./renderresourcesallocated.md) property.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
func setRenderResourcesAllocated(_ flag: Bool)
```

```objc
- (void) setRenderResourcesAllocated:(BOOL) flag;
```

## Discussion

In the base class implementation of the [`allocateRenderResources()`](./allocaterenderresources%28%29.md) method, the value of the [`renderResourcesAllocated`](./renderresourcesallocated.md) property is set to [`true`](../../Swift/true.md). If the [`allocateRenderResources()`](./allocaterenderresources%28%29.md) method fails in a subclass, you must use this method to set the value of the [`renderResourcesAllocated`](./renderresourcesallocated.md) property to [`false`](../../Swift/false.md).

## Parameters

- `flag`: A Boolean value that determines whether the audio unit has allocated its required rendering resources..

## See Also

### Customizing the Audio Unit Behavior
- [class func registerSubclass(AnyClass, as: AudioComponentDescription, name: String, version: UInt32)](./registersubclass%28_,as,name,version%29.md)
  Registers an audio unit subclass.
- [func shouldChange(to: AVAudioFormat, for: AUAudioUnitBus) -> Bool](./shouldchange%28to,for%29.md)
  This is called when you set the format on a bus.
- [var internalRenderBlock: AUInternalRenderBlock](./internalrenderblock.md)
  The block which you must provide, via a getter, in order to implement rendering.
- [var midiOutputBufferSizeHint: Int](./midioutputbuffersizehint.md)
- [typealias AUInternalRenderBlock](../auinternalrenderblock.md)
  A block to render the audio unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/setrenderresourcesallocated(_:))*