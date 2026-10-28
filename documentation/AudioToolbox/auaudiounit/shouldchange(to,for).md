# shouldChange(to:for:)

**Framework**: Audio Toolbox  
**Kind**: method  
**Role**: Instance Method

This is called when you set the format on a bus.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
func shouldChange(to format: AVAudioFormat, for bus: AUAudioUnitBus) -> Bool
```

```objc
- (BOOL) shouldChangeToFormat:(AVAudioFormat *) format forBus:(AUAudioUnitBus *) bus;
```

## Return Value

- [`true`](../../Swift/true.md) if the new format will be set on the bus.

## Discussion

- [`false`](../../Swift/false.md) if the new format will not be set on the bus.

## Discussion

The bus has already checked that the format meets its channel constraints. The audio unit can override this method to check the format before allowing it to be set on the bus.

The default implementation returns [`false`](../../Swift/false.md) if the audio unit’s [`renderResourcesAllocated`](./renderresourcesallocated.md) value is [`true`](../../Swift/true.md).

## Parameters

- `format`: The proposed new format.
- `bus`: The bus on which the format will be changed.

## See Also

### Customizing the Audio Unit Behavior
- [class func registerSubclass(AnyClass, as: AudioComponentDescription, name: String, version: UInt32)](./registersubclass%28_,as,name,version%29.md)
  Registers an audio unit subclass.
- [func setRenderResourcesAllocated(Bool)](./setrenderresourcesallocated%28_%29.md)
  Sets the Boolean value of the [`renderResourcesAllocated`](./renderresourcesallocated.md) property.
- [var internalRenderBlock: AUInternalRenderBlock](./internalrenderblock.md)
  The block which you must provide, via a getter, in order to implement rendering.
- [var midiOutputBufferSizeHint: Int](./midioutputbuffersizehint.md)
- [typealias AUInternalRenderBlock](../auinternalrenderblock.md)
  A block to render the audio unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/shouldchange(to:for:))*