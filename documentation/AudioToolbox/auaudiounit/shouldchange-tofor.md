# shouldChange(to:for:)

**Framework**: Audio Toolbox  
**Kind**: method

This is called when you set the format on a bus.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
func shouldChange(to format: AVAudioFormat, for bus: AUAudioUnitBus) -> Bool
```

#### Return Value

- [`true`](https://developer.apple.com/documentation/Swift/true) if the new format will be set on the bus.

#### Discussion

- [`false`](https://developer.apple.com/documentation/Swift/false) if the new format will not be set on the bus.

#### Discussion

The bus has already checked that the format meets its channel constraints. The audio unit can override this method to check the format before allowing it to be set on the bus.

The default implementation returns [`false`](https://developer.apple.com/documentation/Swift/false) if the audio unit’s [`renderResourcesAllocated`](auaudiounit/renderresourcesallocated.md) value is [`true`](https://developer.apple.com/documentation/Swift/true).

## Parameters

- `format`: The proposed new format.
- `bus`: The bus on which the format will be changed.

## See Also

- [class func registerSubclass(AnyClass, as: AudioComponentDescription, name: String, version: UInt32)](auaudiounit/registersubclass(_:as:name:version:).md)
  Registers an audio unit subclass.
- [func setRenderResourcesAllocated(Bool)](auaudiounit/setrenderresourcesallocated(_:).md)
  Sets the Boolean value of the [`renderResourcesAllocated`](auaudiounit/renderresourcesallocated.md) property.
- [var internalRenderBlock: AUInternalRenderBlock](auaudiounit/internalrenderblock.md)
  The block which you must provide, via a getter, in order to implement rendering.
- [var midiOutputBufferSizeHint: Int](auaudiounit/midioutputbuffersizehint.md)
- [typealias AUInternalRenderBlock](auinternalrenderblock.md)
  A block to render the audio unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/shouldchange(to:for:))*